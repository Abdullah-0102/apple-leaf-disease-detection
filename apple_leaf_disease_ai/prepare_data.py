import os
import shutil
import random
from pathlib import Path

# Set random seed for reproducibility
random.seed(42)

# Classes in our dataset
CLASSES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy"
]

def prepare_splits(base_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    base_path = Path(base_dir).resolve()
    
    # Check if files have already been split
    if (base_path / "train").exists() and (base_path / "val").exists() and (base_path / "test").exists():
        print("[!] Train/Val/Test directories already exist. Skipping split preparation.")
        # Print stats of existing split
        for split in ["train", "val", "test"]:
            print(f"Split: {split}")
            for c in CLASSES:
                c_path = base_path / split / c
                count = len(list(c_path.glob("*.JPG"))) + len(list(c_path.glob("*.jpg")))
                print(f"  - {c}: {count} images")
        return

    print("Beginning dataset cleaning and train/val/test splitting...")
    
    # Dictionary to hold the list of clean color images per class
    class_images = {c: [] for c in CLASSES}
    
    for c in CLASSES:
        c_path = base_path / c
        if not c_path.exists():
            print(f"[!] Error: Directory {c_path} does not exist.")
            continue
            
        # Get all image files in the directory
        all_files = list(c_path.glob("*"))
        for f in all_files:
            if f.is_file():
                # We only want standard color images (exclude masked and other formats)
                # Color images in PlantVillage are JPGs and do not contain '_final_masked'
                name = f.name
                if name.lower().endswith(('.jpg', '.jpeg', '.png')) and "_final_masked" not in name:
                    class_images[c].append(f)
                    
        print(f"Class '{c}': Found {len(class_images[c])} standard color images (ignored masked files).")

    # Create split directories
    splits = ["train", "val", "test"]
    for split in splits:
        for c in CLASSES:
            (base_path / split / c).mkdir(parents=True, exist_ok=True)

    # Perform splitting
    for c, images in class_images.items():
        # Shuffle the list
        random.shuffle(images)
        
        n_images = len(images)
        n_train = int(n_images * train_ratio)
        n_val = int(n_images * val_ratio)
        n_test = n_images - n_train - n_val
        
        train_imgs = images[:n_train]
        val_imgs = images[n_train:n_train+n_val]
        test_imgs = images[n_train+n_val:]
        
        print(f"Splitting '{c}' ({n_images} total) -> {len(train_imgs)} train | {len(val_imgs)} val | {len(test_imgs)} test")
        
        # Copy files to split directories
        for img in train_imgs:
            shutil.copy2(img, base_path / "train" / c / img.name)
        for img in val_imgs:
            shutil.copy2(img, base_path / "val" / c / img.name)
        for img in test_imgs:
            shutil.copy2(img, base_path / "test" / c / img.name)

    # Clean up the original directories if they contain files, but keep them if they are the root of splits
    # To keep things clean, we will delete the original non-split folders after verification
    print("\n[+] Verification of splits:")
    for split in splits:
        print(f"Split: {split}")
        for c in CLASSES:
            c_path = base_path / split / c
            count = len(list(c_path.glob("*")))
            print(f"  - {c}: {count} images")

    # Ask to clean up original unsorted folders
    print("\nCleaning up unsorted directories at root level...")
    for c in CLASSES:
        orig_path = base_path / c
        if orig_path.exists():
            # Delete files inside the original path
            for f in orig_path.glob("*"):
                if f.is_file():
                    f.unlink()
            # Remove directory
            orig_path.rmdir()
            print(f"Removed original directory: {c}")
            
    print("\n[+] Data split preparation complete!")

if __name__ == "__main__":
    prepare_splits("./dataset")
