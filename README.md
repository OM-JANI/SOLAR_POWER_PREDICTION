# ☀️ Solar Power Prediction System

A machine learning-powered web application that predicts solar power production based on weather parameters using Linear Regression and advanced ensemble models (XGBoost and Random Forest).

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Performance](#model-performance)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

This project provides an end-to-end solution for predicting solar power production using weather data. It includes:
- Data analysis and preprocessing pipeline
- Multiple machine learning models (Linear Regression, XGBoost, Random Forest)
- Interactive web interface for real-time predictions
- Comprehensive Jupyter notebook with exploratory data analysis

## ✨ Features

- **Real-time Predictions**: Web-based interface for instant solar power predictions
- **Multiple ML Models**: Comparison between Linear Regression, XGBoost, and Random Forest
- **Hyperparameter Tuning**: Optimized models using GridSearchCV
- **Data Preprocessing**: RobustScaler for handling outliers
- **User-Friendly UI**: Clean, responsive web interface with gradient design
- **Comprehensive Analysis**: Detailed Jupyter notebook with EDA and model evaluation

## 📁 Project Structure

```
solar-power-prediction/
│
├── data/
│   └── Solar_dataset.csv          # Solar power production dataset (8760 hourly records)
│
├── notebooks/
│   └── Project1_Code.ipynb        # Jupyter notebook with full analysis and model training
│
├── src/
│   ├── train_model.py             # Script to train and save the Linear Regression model
│   └── app.py                     # Flask web application
│
├── templates/
│   └── index.html                 # HTML template for the web interface
│
├── models/
│   └── solar_model.pkl            # Trained model (generated after running train_model.py)
│
├── requirements.txt               # Python dependencies
├── .gitignore                    # Git ignore file
└── README.md                     # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/solar-power-prediction.git
   cd solar-power-prediction
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Training the Model

Before running the web application, train the model:

```bash
cd src
python train_model.py
```

This will:
- Load the solar dataset
- Train a Linear Regression model
- Save the trained model to `models/solar_model.pkl`
- Display training and test R² scores

### Running the Web Application

1. **Start the Flask server**
   ```bash
   cd src
   python app.py
   ```

2. **Access the application**
   - Open your browser and navigate to: `http://localhost:5000`
   - Enter the following weather parameters:
     - Wind Speed (m/s)
     - Sunshine Duration (hours)
     - Air Pressure (hPa)
     - Solar Radiation (W/m²)
     - Air Temperature (°C)
     - Relative Humidity (%)
   - Click "Predict Power Output" to see the prediction

### Exploring the Jupyter Notebook

To explore the full analysis and model comparison:

```bash
jupyter notebook notebooks/Project1_Code.ipynb
```

The notebook includes:
- Data loading and exploration
- Feature engineering (datetime features, seasons)
- Outlier detection and handling
- Multiple model training and comparison
- Performance metrics visualization

## 📊 Dataset

**Source**: Solar power production data from 2017

**Features**:
- `WindSpeed`: Wind speed in m/s
- `Sunshine`: Sunshine duration in hours
- `AirPressure`: Atmospheric pressure in hPa
- `Radiation`: Solar radiation in W/m²
- `AirTemperature`: Air temperature in °C
- `RelativeAirHumidity`: Relative humidity in %
- `Date-Hour(NMT)`: Timestamp (not used in model)

**Target Variable**:
- `SystemProduction`: Solar power production in kW

**Dataset Size**: 8,760 hourly records (1 full year)

## 📈 Model Performance

### Linear Regression (Web App Model)
- Simple, fast predictions
- Good baseline performance
- Ideal for real-time web application

### Advanced Models (Jupyter Notebook)

**XGBoost Regressor**:
- MAE: 198.44
- RMSE: 460.72
- R² Score: 0.8927
- NRMSE: 0.1072

**Random Forest Regressor**:
- MAE: 208.82
- RMSE: 470.82
- R² Score: 0.8880
- NRMSE: 0.1120

**Hyperparameter Optimization**:
- XGBoost: GridSearchCV with 27 parameter combinations
- Random Forest: GridSearchCV with 9 parameter combinations
- Cross-validation: 3-fold CV
- Scoring metric: Negative Mean Absolute Error

## 🛠️ Technologies Used

### Backend
- **Python 3.8+**
- **Flask**: Web framework
- **scikit-learn**: Machine learning models and preprocessing
- **XGBoost**: Gradient boosting
- **pandas**: Data manipulation
- **NumPy**: Numerical computations

### Frontend
- **HTML5/CSS3**: User interface
- **Jinja2**: Template engine

### Data Science
- **Jupyter Notebook**: Interactive analysis
- **Matplotlib/Seaborn**: Data visualization
- **RobustScaler**: Outlier-resistant preprocessing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- Dataset source: Solar power production monitoring system
- Inspired by renewable energy prediction challenges
- Thanks to the open-source community for the amazing tools

---

**Note**: Make sure to train the model using `train_model.py` before running the Flask application. The model file (`solar_model.pkl`) is not included in the repository and needs to be generated locally.
