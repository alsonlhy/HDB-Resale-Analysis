# Singapore HDB Resale Market Analysis 🏙️

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://hdb-resale-analysis.streamlit.app/])

## Overview
This project explores the dynamics of Singapore's public housing (HDB) resale market using Python. By analyzing over 220,000 transaction records, this exploratory data analysis (EDA) visualizes spatial valuation differences, macroeconomic market shifts, and the economic reality of asset depreciation (lease decay) in real estate.

This is my first data analysis portfolio project, built to demonstrate foundational skills in data manipulation, visualization, machine learning, and web deployment.

## Try the Live Web App
I have deployed the machine learning model as an interactive web application. You can input custom flat parameters (Town, Floor Area, Age, and Floor Rank) to generate real-time price predictions based on historical data. 
👉 **[Click here to view the live HDB Price Predictor app]([https://hdb-resale-analysis.streamlit.app/])**

## Data Source
The dataset used is the **"Resale flat prices based on registration date from Jan-2017 onwards"**, publicly sourced from the Singapore Government's open data portal: [data.gov.sg](https://data.gov.sg/). 

*(Note: The raw `.csv` file is excluded from this repository due to size constraints, but the data can be freely downloaded from the link above).*

## Tools & Libraries Used
* **Python 3**
* **Pandas**: For data cleaning, feature engineering (calculating price per sqm and flat age), and time-series grouping.
* **Matplotlib & Seaborn**: For generating static, comprehensive data visualizations.
* **Scikit-learn**: For engineering dummy variables, ordinal mapping, and building the Multiple Linear Regression model.
* **Streamlit**: For developing and deploying the interactive frontend web application.
* **Jupyter Notebook**: For interactive, step-by-step EDA and model training.

## Key Insights Discovered
1. **Geospatial Valuation (The Location Premium):** A cross-sectional analysis reveals that the **Central Area** commands the highest premium per square meter, while non-mature estates like **Choa Chu Kang** provide the most accessible entry points for buyers.
2. **Macro-Market Trends & External Shocks:** Time-series tracking of average prices exposes a distinct market surge post-2020. Prices escalated rapidly from hovering around 4,500 SGD/sqm to nearing 7,000 SGD/sqm, reflecting the supply-chain disruptions and BTO construction delays caused by the global pandemic.
3. **Asset Depreciation (The 99-Year Lease Decay):** A scatter plot correlation confirms the "lease decay" phenomenon. There is a clear, visually verifiable negative correlation between the chronological age of a flat and its price per square meter.

## Predictive Modeling (Machine Learning)
Built a Multiple Linear Regression model using `scikit-learn` to predict HDB resale prices based on floor area, flat age, town, and storey range. The foundational model achieved a Mean Absolute Error (MAE) of roughly $81,347, providing a baseline prediction within 10-15% of actual transaction values.

## Future Scope (Coming Soon)
To explore new ways to improve model accuracy via:
1. **External Data:** Integrating geographic APIs to calculate distance to the nearest MRT stations or top-tier primary schools.
2. **Outlier Filtering:** Removing the top 1% priced luxury flats to normalize the training data.
3. **Advanced Algorithms:** Testing non-linear models like **Random Forest** or **Gradient Boosting (XGBoost)** to better capture complex market dynamics.

## How to Run This Project Locally
1. Clone this repository to your local machine.
2. Ensure you have Python installed along with the required libraries (run `pip install -r requirements.txt`).
3. **To view the analysis:** Download the dataset from data.gov.sg, place the `.csv` in the root directory, and open `hdb_analysis.ipynb` in VS Code or Jupyter Notebook.
4. **To run the web app:** Open your terminal, navigate to the project folder, and run `python -m streamlit run app.py`.