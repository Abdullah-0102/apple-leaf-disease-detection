# 🍎 Apple Leaf Disease Detection AI

<div align="center">

![Apple Leaf Disease Detection](https://img.shields.io/badge/Deep%20Learning-Computer%20Vision-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

**A state-of-the-art deep learning solution for automated detection and classification of diseases in apple leaves using CNN and modern computer vision techniques.**

[Features](#features) • [Quick Start](#quick-start) • [Results](#results) • [Project Structure](#project-structure) • [Contributing](#contributing)

</div>

---

## 📋 Overview

This project leverages **deep learning** and **computer vision** to automatically detect and classify diseases affecting apple leaves. The system can identify four distinct apple leaf conditions with high accuracy:

- ✅ **Apple Scab** - Fungal infection causing dark lesions
- ✅ **Black Rot** - Fungal disease with characteristic dark spots
- ✅ **Cedar Apple Rust** - Rust fungus affecting leaf tissue
- ✅ **Healthy Leaves** - Normal, disease-free leaves

---

## 🎯 Features

- **Multi-Model Comparison**: 4 different AI techniques for classification and clustering
- **Neural Networks**: MLP with custom architecture (4 hidden layers)
- **Ensemble Learning**: Random Forest with 100 estimators
- **Convolutional Networks**: Baseline CNN + optimized variants + Transfer Learning
- **Unsupervised Learning**: K-Means clustering with advanced extensions (PCA, Deep Features)
- **Comprehensive Evaluation**: Confusion matrices, accuracy metrics, ARI, NMI scores
- **Visualization Suite**: Learning curves, class distributions, heatmaps
- **Transfer Learning**: MobileNetV2 pre-trained models for advanced feature extraction
- **Complete Jupyter Notebook**: End-to-end pipeline with detailed documentation
- **Academic Rigor**: COMP40511 coursework requirements implementation

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8** or higher
- **CUDA-compatible GPU** (recommended for faster training)
- **pip** or **conda** package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Abdullah-0102/apple-leaf-disease-detection.git
   cd apple-leaf-disease-detection
   ```

2. **Create a virtual environment**:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r apple_leaf_disease_ai/requirements.txt
   ```

4. **Navigate to project directory**:
   ```bash
   cd apple_leaf_disease_ai
   ```

### Running the Model

Open and run the main notebook:
```bash
jupyter notebook main.ipynb
```

This will guide you through:
- Data loading and preprocessing
- Model training
- Performance evaluation
- Disease classification

---

## 📊 Results

### Model Performance Comparison

Our implementation compares four AI techniques as specified in the COMP40511 coursework:

| Model Type | Architecture | Test Accuracy |
|------------|--------------|---------------|
| Neural Network (Flat) | Multilayer Perceptron (MLP) | **64.30%** |
| Ensemble (Flat) | Random Forest (100 estimators) | **78.50%** |
| Convolutional (Spatial) | Baseline CNN | **84.76%** |
| Convolutional (Spatial) | Adjusted/Optimized CNN | **79.33%** |

**Best Model**: Baseline CNN with **84.76% test accuracy** ✅

*Complete metrics available in [outputs/model_performance_comparison.csv](apple_leaf_disease_ai/outputs/model_performance_comparison.csv)*

### Key Findings

- **CNN superiority**: Deep learning models (CNN) significantly outperform flat models (MLP, Random Forest)
- **Spatial information matters**: Convolutional architecture captures leaf texture and spatial features effectively
- **Model complexity**: The baseline CNN achieves better results than the overly-tuned adjusted CNN, suggesting good generalization
- **Ensemble underperformance**: Random Forest on flattened pixels shows limitations without spatial feature extraction

### Advanced Extensions Implemented

1. **Transfer Learning with MobileNetV2**: Pre-trained CNN for feature extraction
2. **PCA-based Clustering**: Dimensionality reduction for unsupervised learning
3. **Deep Feature Clustering**: Using MobileNetV2 embeddings for advanced clustering analysis

---

## 📁 Project Structure

```
apple-leaf-disease-detection/
│
├── apple_leaf_disease_ai/
│   ├── dataset/                          # Apple leaf image datasets
│   │   ├── train/                        # Training images
│   │   │   ├── Apple___Apple_scab/
│   │   │   ├── Apple___Black_rot/
│   │   │   ├── Apple___Cedar_apple_rust/
│   │   │   └── Apple___healthy/
│   │   ├── val/                          # Validation images
│   │   │   └── [4 disease classes]
│   │   └── test/                         # Test images
│   │       └── [4 disease classes]
│   │
│   ├── outputs/                          # Training outputs
│   │   ├── model_performance_comparison.csv
│   │   ├── class_distribution.png
│   │   ├── sample_images.png
│   │   ├── cnn_confusion_matrix.png
│   │   ├── mlp_confusion_matrix.png
│   │   ├── rf_confusion_matrix.png
│   │   ├── cnn_learning_curves.png
│   │   ├── mlp_learning_curves.png
│   │   ├── kmeans_elbow_curve.png
│   │   └── kmeans_crosstab_heatmap.png
│   │
│   ├── models/                           # Trained model checkpoints
│   │   └── apple_leaf_disease_cnn.h5    # Best performing model
│   │
│   ├── reports/                          # Documentation
│   │   ├── Technical_Report.pdf
│   │   └── GenAI_Acknowledgement_Form.pdf
│   │
│   ├── main.ipynb                        # Complete pipeline notebook
│   ├── extract_dataset.py                # Dataset extraction script
│   ├── prepare_data.py                   # Data preparation utilities
│   ├── test_project.py                   # Testing utilities
│   ├── requirements.txt                  # Python dependencies
│   └── README.md                         # Detailed documentation
│
├── .gitignore                            # Git ignore rules
├── README.md                             # Project overview (this file)
└── LICENSE                               # MIT License

```

---

## 🔧 Technical Stack

| Component | Technology |
|-----------|-----------|
| **Deep Learning Framework** | TensorFlow / PyTorch |
| **Computer Vision** | OpenCV, Pillow |
| **Data Processing** | NumPy, Pandas |
| **Visualization** | Matplotlib, Seaborn |
| **Model Deployment** | Flask / Streamlit |
| **Environment** | Jupyter Notebook, Python 3.8+ |

---

## 📈 Workflow

### COMP40511 Coursework Implementation

This project implements four core AI/ML techniques as part of the coursework requirements:

#### **Task 1: Multilayer Perceptron (MLP)** - Neural Network (Flat)
   - Custom-built MLP with 4 hidden layers (15 → 25 → 20 → 15 neurons)
   - Trained on flattened image pixels
   - Test Accuracy: **64.30%**
   - Baseline neural network approach without spatial awareness

#### **Task 2: Ensemble Model** - Random Forest Classifier
   - 100-tree ensemble on flattened image features
   - Max depth optimization for generalization
   - Test Accuracy: **78.50%**
   - Demonstrates ensemble learning vs single models

#### **Task 3: Deep Convolutional Neural Network (CNN)** - Spatial Architecture
   - **Baseline CNN**: 4 convolutional blocks with max pooling
     - Architecture: Conv32 → Conv64 → Conv128 → Conv128
     - Test Accuracy: **84.76%** ✅ **BEST MODEL**
   - **Adjusted CNN**: Hyperparameter tuning (lower learning rate, reduced dropout)
     - Test Accuracy: **79.33%**
   - **Advanced Extension**: Transfer Learning with MobileNetV2
     - Pre-trained ImageNet weights with fine-tuning
     - Demonstrates deep feature learning

#### **Task 4: Unsupervised Clustering** - K-Means
   - **Baseline K-Means**: Raw pixel clustering
   - **Advanced Extension 1**: PCA-reduced clustering (10 components)
     - Dimensionality reduction for noise removal
   - **Advanced Extension 2**: Deep Feature Clustering
     - MobileNetV2 embeddings for high-level feature clustering
   - Evaluation metrics: Adjusted Rand Index (ARI), Normalized Mutual Information (NMI)

### Full Pipeline Execution

1. **Run the main notebook**:
   ```bash
   cd apple_leaf_disease_ai
   jupyter notebook main.ipynb
   ```

2. **Data Processing**:
   - Images resized to 64×64 pixels
   - Normalized to [0, 1] range
   - Train/Val/Test splits prepared

3. **Model Training**:
   - All 4 techniques trained sequentially
   - Performance metrics computed
   - Confusion matrices generated
   - Learning curves visualized

4. **Results Analysis**:
   - Check `outputs/model_performance_comparison.csv`
   - View confusion matrices and learning curves
   - Best CNN weights saved to `models/apple_leaf_disease_cnn.h5`

---

## 🎓 Getting Started with the Project

### Run the Complete Pipeline

1. Navigate to the project directory:
   ```bash
   cd apple_leaf_disease_ai
   ```

2. Open the main Jupyter notebook:
   ```bash
   jupyter notebook main.ipynb
   ```

3. Execute cells sequentially:
   - **Cells 1-3**: Environment setup and imports
   - **Cells 4-6**: Data loading (Train/Val/Test splits)
   - **Cells 7-9**: Data visualization and exploration
   - **Cells 10-15**: Task 1 - MLP training and evaluation
   - **Cells 16-17**: Task 2 - Random Forest training and evaluation
   - **Cells 18-30**: Task 3 - CNN training and evaluation
   - **Cells 31-38**: Task 4 - K-Means clustering and analysis

### Expected Output

After running the notebook:
- ✅ Trained models saved to `models/`
- ✅ Performance metrics in `outputs/model_performance_comparison.csv`
- ✅ Visualizations: confusion matrices, learning curves, class distribution
- ✅ Best model: Baseline CNN (**84.76% accuracy**)

---

## 💡 Key Insights

- **Class Balance**: Dataset contains balanced distribution across all 4 classes
- **Data Augmentation**: Essential for improving model generalization
- **Transfer Learning**: Pre-trained models outperform custom architectures
- **GPU Acceleration**: Reduces training time by ~10x compared to CPU

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/improvement`)
3. **Commit** your changes (`git commit -m 'Add improvement'`)
4. **Push** to the branch (`git push origin feature/improvement`)
5. **Open** a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact & Support

- **Author**: Abdullah Bin Imran
- **Repository**: [GitHub](https://github.com/Abdullah-0102/apple-leaf-disease-detection)
- **Issues**: [Report bugs or request features](https://github.com/Abdullah-0102/apple-leaf-disease-detection/issues)

---

## 🙏 Acknowledgments

- Dataset sourced from public agricultural databases
- Inspired by modern computer vision and deep learning practices
- Built with TensorFlow and PyTorch communities

---

<div align="center">

**⭐ If you find this project helpful, please give it a star! ⭐**

Made with ❤️ for agriculture and AI

</div>
