# Multiple Linear Regression: Toyota Corolla Price Prediction

## Overview
This project applies **Multiple Linear Regression (MLR)** to predict the **price of Toyota Corolla cars** based on various attributes like age, mileage, fuel type, horsepower, engine capacity, and weight. The dataset undergoes **exploratory data analysis (EDA), preprocessing, model building, evaluation, and regularization (Lasso & Ridge Regression).**

## Dataset
The dataset includes the following variables:
- **Age**: Age of the car (years)
- **KM**: Accumulated kilometers on the odometer
- **FuelType**: Type of fuel (Petrol, Diesel, CNG)
- **HP**: Horsepower of the car
- **Automatic**: Transmission type (Yes=1, No=0)
- **CC**: Engine capacity (cubic centimeters)
- **Doors**: Number of doors
- **Weight**: Car weight (kg)
- **Quarterly_Tax**: Quarterly tax in Euros
- **Price**: Target variable (car price in Euros)

## Project Workflow
1. **Exploratory Data Analysis (EDA)**: Visualizations and summary statistics.
2. **Data Preprocessing**:
   - Handling missing values
   - Encoding categorical variables
   - Feature scaling
3. **Model Development**:
   - Building **Multiple Linear Regression Models**
   - Training on **80% of the dataset** and testing on **20%**
   - Interpreting model coefficients
4. **Model Evaluation**:
   - Computing **R² score** and other relevant metrics.
5. **Regularization Techniques**:
   - Applying **Lasso and Ridge Regression** to reduce multicollinearity.
6. **Discussion**:
   - Assumptions made

## Installation & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/multiple-linear-regression-toyota.git
   cd multiple-linear-regression-toyota
