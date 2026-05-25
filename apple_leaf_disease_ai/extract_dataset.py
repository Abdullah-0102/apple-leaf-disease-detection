import os
import zipfile
import argparse
from pathlib import Path

# Target folders we want to extract
TARGET_FOLDERS = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy"
]

def find_zip_files(search_dir):
    """Search for potential Kaggle download zip files in the given directory."""
    potential_names = ["archive.zip", "plantvillage-dataset.zip", "plantvillage.zip"]
    found_zips = []
    
    # Check common names first
    for name in potential_names:
        p = Path(search_dir) / name
        if p.exists():
            found_zips.append(p)
            
    # If not found, list any zip file containing 'plant' or 'archive' in its name
    if not found_zips:
        for p in Path(search_dir).glob("*.zip"):
            name_lower = p.name.lower()
            if "plant" in name_lower or "archive" in name_lower:
                found_zips.append(p)
                
    return found_zips

def main():
    parser = argparse.ArgumentParser(description="Extract Apple Leaf Disease categories from PlantVillage zip archive.")
    parser.add_argument("--zip_path", type=str, help="Path to the downloaded PlantVillage zip file.")
    parser.add_argument("--dest_dir", type=str, default="./dataset", help="Destination directory to extract folders to.")
    args = parser.parse_args()

    dest_path = Path(args.dest_dir).resolve()
    
    # 1. Resolve zip path
    zip_path = None
    if args.zip_path:
        zip_path = Path(args.zip_path)
    else:
        # Check parent folder (usually the user's Downloads folder, since workspace is a subdirectory)
        parent_dir = Path(__file__).resolve().parent.parent.parent
        print(f"Scanning parent directory: {parent_dir} for dataset zip files...")
        zips = find_zip_files(parent_dir)
        if zips:
            zip_path = zips[0]
            print(f"Found potential dataset zip: {zip_path}")
        else:
            # Check current directory
            zips = find_zip_files(Path("."))
            if zips:
                zip_path = zips[0]
                print(f"Found potential dataset zip: {zip_path}")

    if not zip_path or not zip_path.exists():
        print("\n[!] Error: Could not find the PlantVillage zip file automatically.")
        print("Please download it from: https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset")
        print("Then, run this script specifying the path, for example:")
        print("  python extract_dataset.py --zip_path C:/Users/Abdullah Bin Imran/Downloads/archive.zip")
        return

    print(f"\nProcessing zip archive: {zip_path}")
    print(f"Destination: {dest_path}")
    
    os.makedirs(dest_path, exist_ok=True)

    extracted_count = 0
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Get all file paths in zip
        namelist = zip_ref.namelist()
        
        # We need to map zip members to our target categories.
        # Sometimes paths inside zip files look like 'plantvillage dataset/color/Apple___healthy/image.JPG'
        # or flat as 'Apple___healthy/image.JPG'
        for member in namelist:
            # Skip directory entries themselves
            if member.endswith('/'):
                continue
                
            parts = member.split('/')
            
            # Find if any part of the file path matches our target folders
            matched_folder = None
            for folder in TARGET_FOLDERS:
                if folder in parts:
                    matched_folder = folder
                    break
            
            if matched_folder:
                # We want to extract this file and place it under dest_path/matched_folder/filename
                filename = parts[-1]
                target_file_path = dest_path / matched_folder / filename
                
                # Ensure parent directory exists
                target_file_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Extract the file content and write it
                with zip_ref.open(member) as source_file, open(target_file_path, 'wb') as dest_file:
                    dest_file.write(source_file.read())
                    
                extracted_count += 1
                if extracted_count % 100 == 0:
                    print(f"Extracted {extracted_count} images...", end='\r')

    print(f"\n[+] Extraction complete! Extracted {extracted_count} images into:")
    for folder in TARGET_FOLDERS:
        folder_path = dest_path / folder
        count = len(list(folder_path.glob("*"))) if folder_path.exists() else 0
        print(f"  - {folder}/ ({count} images)")

if __name__ == "__main__":
    main()
