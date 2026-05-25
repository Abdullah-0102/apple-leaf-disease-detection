# Apple Leaf Disease AI

A Deep Learning and Computer Vision project for detecting and classifying diseases in apple leaves. This project aims to identify common apple leaf conditions (e.g., Apple Scab, Black Rot, Cedar Apple Rust, and Healthy leaves) using modern deep learning architectures.

## Project Structure

The project is organized as follows:

```text
apple_leaf_disease_ai/
├── dataset/          # Raw and processed image datasets
├── notebooks/        # Jupyter notebooks for experimentation and exploration
├── outputs/          # Training outputs, logs, and plots
├── models/           # Trained model checkpoints (.h5, .pth, etc.)
├── reports/          # Generated analysis, metrics, and documentation
├── demo/             # Web/Desktop demo application code
├── images/           # Images for README and documentation
├── requirements/     # Segmented requirements (e.g., dev, prod, colab)
├── main.ipynb        # Main entry-point notebook for end-to-end training
├── README.md         # Project documentation (this file)
└── requirements.txt  # Consolidated python package requirements
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- CUDA-compatible GPU (recommended for training)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd apple-leaf-disease-AI/apple_leaf_disease_ai
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Workflow

1. **Data Collection & Preparation**: Place raw leaf images into the `dataset/` directory, split into train/val/test directories.
2. **Exploration**: Run the Jupyter notebooks in `notebooks/` or `main.ipynb` to visualize data distribution and apply image preprocessing.
3. **Training**: Train the models using `main.ipynb`. The best weights will be saved to `models/`.
4. **Evaluation**: Check the logs and performance graphs saved in `outputs/`.
5. **Deployment**: Run the web/local application located in `demo/` to classify user-uploaded leaf images.

## License

This project is licensed under the MIT License.
