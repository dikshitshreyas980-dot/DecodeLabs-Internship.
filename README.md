# Data Classification Using AI – Iris Flower Classification

![Project Banner](static/img/heatmap.png) <!-- Just a placeholder aesthetic image -->

This repository contains a complete, professional, and beginner-friendly Machine Learning project for the **DecodeLabs Artificial Intelligence Internship** (Project 2). It demonstrates a complete supervised machine learning workflow using the Iris dataset and the K-Nearest Neighbors (KNN) algorithm, deployed with a Flask backend and a modern web dashboard.

---

## 🎯 Project Objective
To build a supervised machine learning classification system using the Iris dataset, demonstrating data loading, preprocessing, shuffling, train-test splitting, feature scaling, model training, prediction, evaluation, visualization, and live testing via an interactive dashboard.

## 📊 Dataset Details
We use the classic **Iris Dataset** from `scikit-learn`:
- **Samples**: 150 total records.
- **Features (4)**: Sepal Length, Sepal Width, Petal Length, Petal Width (all continuous numerical in cm).
- **Target Classes (3)**: Setosa, Versicolor, Virginica.
- **Distribution**: 50 samples per class (perfectly balanced).

## 🚀 Machine Learning Workflow

1. **Data Loading**: Iris data is loaded via `sklearn.datasets`.
2. **Shuffling & Splitting**: The dataset is shuffled and split into 80% training data (120 samples) and 20% testing data (30 samples) using `stratify=y` to maintain class balance.
3. **Feature Scaling**: Distance-based algorithms like KNN are highly sensitive to unscaled data. We use `StandardScaler` to normalize features (mean=0, variance=1). Crucially, the scaler is fit *only* on the training data to prevent data leakage.
4. **K-Value Optimization**: Instead of hardcoding K=5, the training script performs **Cross-Validation on the training set** for K=1 to K=20. The optimal K is selected based on the lowest validation error rate, avoiding overfitting on the final test set.
5. **Model Training**: A `Pipeline` (Scaler + KNN) is trained on the full training set using the best K.
6. **Evaluation**: The model is tested on the unseen 20% test set. We evaluate using Accuracy, Precision, Recall, F1-Score, and a Confusion Matrix.
7. **Serialization**: The entire Pipeline is saved using `joblib` so that live predictions use the exact same preprocessing parameters as training.

## 🧠 Educational Concepts

### Why K-Nearest Neighbors (KNN)?
KNN is a simple, intuitive, distance-based algorithm. Given a new flower's measurements, it calculates the distance to all points in the training set, finds the 'K' closest neighbors, and assigns the new flower to the majority class among those neighbors.

### Why StandardScaler?
Since KNN calculates distances (usually Euclidean), features with larger ranges (e.g., thousands) will dominate features with smaller ranges (e.g., decimals). `StandardScaler` standardizes all features to the same scale, ensuring they contribute equally to distance calculations.

### The "Accuracy Mirage"
Accuracy is simply the percentage of correct predictions. In highly imbalanced datasets (e.g., 99% Class A, 1% Class B), predicting 'Class A' every time yields 99% accuracy but fails entirely to identify Class B. 
By calculating **Precision**, **Recall**, **F1-Score**, and viewing the **Confusion Matrix**, we get a true understanding of model performance across *all* classes, avoiding the "Accuracy Mirage".

---

## 🛠️ Project Architecture

```text
iris-classification-ai/
│
├── app.py                     # Flask web server and API
├── requirements.txt           # Python dependencies
├── Procfile                   # Production deployment configuration (Gunicorn)
├── .gitignore
│
├── model/
│   ├── train_model.py         # The complete ML training pipeline script
│   └── model.pkl              # Serialized scaler + KNN model
│
├── data/
│   ├── dataset_info.json      # Dataset metadata
│   ├── k_analysis.json        # Cross-validation metrics
│   └── metrics.json           # Final test evaluation metrics
│
├── templates/
│   └── index.html             # The modern web dashboard
│
├── static/
│   ├── css/style.css          # Vanilla CSS styling
│   ├── js/script.js           # Chart.js visualization and API fetching
│   └── img/                   # Seaborn-generated correlation & pair plots
│
└── tests/
    └── test_app.py            # Unit tests for the application
```

---

## 💻 Local Installation & Execution

**1. Clone the repository and navigate to the folder:**
```bash
git clone <your-github-repo-url>
cd iris-classification-ai
```

**2. Create a virtual environment:**
```bash
python -m venv venv
```

**3. Activate the virtual environment:**
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

**4. Install dependencies:**
```bash
pip install -r requirements.txt
```

**5. Train the Model:**
*(This generates the visual plots, metrics, and `model.pkl`)*
```bash
python model/train_model.py
```

**6. Run the Application locally:**
```bash
python app.py
```
*Navigate to `http://127.0.0.1:5000` in your browser.*

---

## 🧪 Testing

To ensure the API and application work as expected, a suite of unit tests is included.
Run the tests using:
```bash
python -m unittest discover tests
```

---

## 🌍 GitHub & Deployment

### GitHub Setup
1. Create a new empty repository on GitHub.
2. Initialize git locally (if not already done): `git init`
3. Add files: `git add .`
4. Commit: `git commit -m "Initial commit"`
5. Link remote: `git remote add origin <your-repo-url>`
6. Push: `git push -u origin main`

### Deployment (e.g., Render)
This project is configured to run in a production environment using **Gunicorn**.
1. Create an account on [Render](https://render.com/).
2. Click **New +** -> **Web Service**.
3. Connect your GitHub repository.
4. Render will automatically detect it as a Python environment.
5. Build Command: `pip install -r requirements.txt`
6. Start Command: `gunicorn app:app` (This uses the `Procfile`)
7. Click **Create Web Service**.

---

## ✅ Project Submission Checklist

- [x] Dataset loaded and understood
- [x] Data shuffled
- [x] 80/20 train-test split (stratified)
- [x] StandardScaler applied (fit only on train data)
- [x] K optimized via Cross-Validation
- [x] KNN implemented
- [x] Accuracy calculated
- [x] Precision calculated
- [x] Recall calculated
- [x] F1-score calculated
- [x] Confusion matrix generated
- [x] Accuracy Mirage explained in UI
- [x] Interactive prediction implemented
- [x] Project tested
- [x] README completed and GitHub-ready

---
*Created for the DecodeLabs Internship program.*
