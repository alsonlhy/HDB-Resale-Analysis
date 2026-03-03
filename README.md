# Singapore HDB Resale Market Analysis 🏙️

## Overview
This project explores the dynamics of Singapore's public housing (HDB) resale market using Python. By analyzing over 220,000 transaction records, this exploratory data analysis (EDA) visualizes spatial valuation differences, macroeconomic market shifts, and the economic reality of asset depreciation (lease decay) in real estate.

This is my first data analysis portfolio project, built to demonstrate foundational skills in data manipulation, visualization, and extracting actionable insights from raw data.

## Data Source
The dataset used is the **"Resale flat prices based on registration date from Jan-2017 onwards"**, publicly sourced from the Singapore Government's open data portal: [data.gov.sg](https://data.gov.sg/). 

*(Note: The raw `.csv` file is excluded from this repository due to size constraints, but the data can be freely downloaded from the link above).*

## Tools & Libraries Used
* **Python 3**
* **Pandas**: For data cleaning, feature engineering (calculating price per sqm and flat age), and time-series grouping.
* **Matplotlib & Seaborn**: For generating static, comprehensive data visualizations.
* **Jupyter Notebook**: For interactive, step-by-step analysis.

## Key Insights Discovered
1. **Geospatial Valuation (The Location Premium):** A cross-sectional analysis reveals that the **Central Area** commands the highest premium per square meter, while non-mature estates like **Choa Chu Kang** provide the most accessible entry points for buyers.
2. **Macro-Market Trends & External Shocks:** Time-series tracking of average prices exposes a distinct market surge post-2020. Prices escalated rapidly from hovering around 4,500 SGD/sqm to nearing 7,000 SGD/sqm, reflecting the supply-chain disruptions and BTO construction delays caused by the global pandemic.
3. **Asset Depreciation (The 99-Year Lease Decay):** A scatter plot correlation confirms the "lease decay" phenomenon. There is a clear, visually verifiable negative correlation between the chronological age of a flat and its price per square meter.

## Future Scope (Coming Soon)
* **Predictive Modeling:** The next phase of this project involves building a Machine Learning model (Linear Regression via `scikit-learn`) to predict the estimated resale value of a flat based on its town, size, and remaining lease.

## How to Run This Project
1. Clone this repository to your local machine.
2. Ensure you have Python installed along with the required libraries (`pandas`, `matplotlib`, `seaborn`, `jupyter`).
3. Download the dataset from data.gov.sg and place the `.csv` in the root directory.
4. Open `hdb_analysis.ipynb` in VS Code or Jupyter Notebook and run the cells sequentially.