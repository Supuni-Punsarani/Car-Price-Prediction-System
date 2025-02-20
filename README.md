
## 🚗 Car Price Prediction System  

A machine learning-based web application that predicts the resale price of a car based on various input parameters. Built using Flask, Python, and a trained ML model.  

### 📁 Project Structure  

```
Car-Price-Prediction-System/
│── App/  
│   ├── app.py               # Flask web application  
│   ├── index.html           # Frontend UI  
│   ├── car_price_model.pkl  # Trained machine learning model  
│   ├── features.pkl         # Feature encoding file  
│  
│── archive/  
│   ├── car data.csv          # Dataset used for training  
│  
│── Car Price Prediction.ipynb  # Jupyter Notebook with model training  
│── README.md                # Project documentation  
```

### 🚀 Features  

- Predicts car resale price based on key factors like age, fuel type, transmission, and ownership history.  
- Web-based UI using Flask and Bootstrap.  
- Pre-trained machine learning model for fast and accurate predictions.  

### 🛠 Installation  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/Supuni-Punsarani/Car-Price-Prediction-System.git
cd Car-Price-Prediction-System/App
```

2️⃣ **Set up a virtual environment (Optional but recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ **Install dependencies**  
```bash
pip install flask joblib numpy pandas scikit-learn
```

4️⃣ **Run the Flask app**  
```bash
python app.py
```

5️⃣ **Open in your browser**  
Navigate to: **`http://127.0.0.1:5000/`**  

---

### 📊 Dataset  
The dataset is stored in the **`archive/`** folder. It contains car details such as:  
- **Year**  
- **Present Price (Lakhs)**  
- **KMs Driven**  
- **Fuel Type (Petrol/Diesel/CNG)**  
- **Seller Type (Dealer/Individual)**  
- **Transmission (Manual/Automatic)**  
- **Owner (First/Second-hand)**  

The trained model uses this data to make predictions.  

---

### 🧠 Model Training  
The model was trained using **Linear Regression and Loss Regression** in the Jupyter Notebook:  
📌 **`Car Price Prediction.ipynb`**  

---

