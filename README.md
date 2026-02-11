
#Laptop Price Prediction using Machine Learning

## 📌 Project Overview

This project aims to predict the price of a laptop based on its specifications such as RAM, storage, processor type, screen size, and other features.

Machine Learning algorithms are used to analyze patterns between laptop features and their prices to estimate the correct price accurately.

## 🎯 Problem Statement

The goal of this project is to build a regression model that can predict the price of a laptop based on its specifications.

This helps:

* Customers estimate fair price
* Sellers set competitive pricing
* Businesses analyze pricing trends

---

##  Dataset Information

The dataset contains laptop specifications such as:

* RAM (GB)
* Storage (GB)
* Processor
* Screen Size
* Weight
* Other hardware specifications
* Target Variable: **Price**

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit (for deployment)

---

## 🛠️ Project Workflow

### 1️⃣ Data Loading

* Loaded dataset using Pandas

### 2️⃣ Data Understanding

* head(), tail()
* info()
* describe()
* Checked dataset shape

### 3️⃣ Data Preprocessing

* Handled missing values
* Removed duplicate rows
* Dropped unnecessary columns
* Converted categorical variables to numerical using LabelEncoder

### 4️⃣ Feature Selection

* Independent variables (X)
* Dependent variable (y → Price)

### 5️⃣ Feature Scaling

* Used StandardScaler for normalization

### 6️⃣ Model Training

Trained multiple regression models:

* Linear Regression
* Support Vector Regression (SVR)
* Decision Tree Regressor
* Random Forest Regressor
* Polynomial Regression

### 7️⃣ Model Evaluation

Used evaluation metrics:

* MAE (Mean Absolute Error)
* MSE (Mean Squared Error)
* RMSE (Root Mean Squared Error)
* R² Score

### 8️⃣ Model Saving

Saved:

* Best trained model (.pkl file)
* Scaler (.pkl file)

---

## 📈 Model Performance

The models were compared using R² score and error metrics.
The best-performing model was selected for deployment.

---

## 🌐 Deployment

The project is deployed using **Streamlit**.

To run locally:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Laptop_Price_Prediction/
│
├── app.py
├── Laptop_price.csv
├── linear_regression_model.pkl
├── scaler.pkl
├── train_model.py
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

* Use OneHotEncoder instead of LabelEncoder
* Apply Hyperparameter tuning (GridSearchCV)
* Add more real-world features
* Deploy on cloud platforms
* Add feature importance visualization

---

## 👩‍💻 Author

** Bhavanasri**

Machine Learning Enthusiast
Aspiring Data Scientist

---



```
🔗 Live App: https://your-streamlit-link
```


