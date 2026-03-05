import streamlit as st
import pandas as pd
import joblib

model = joblib.load('hdb_model.pkl')
model_columns = joblib.load('model_columns.pkl')

#Setting up webpage
st.title("Singapore HDB Resale Price Predictor")
st.write("Enter the flat details below to get an estimated resale price.")

#User Input portion
town = st.selectbox("Select Town", ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH', 'BUIKIT TIMAH', 'BUKIT PANJANG', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST', 'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL', 'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN'])
sqm = st.number_input("Input Flat Size (sqm)", min_value=30, max_value=200, value=90)
age = st.number_input("Input Flat Age (years)", min_value=0, max_value=99, value=10)
floor_rank = st.number_input("Input Floor Rank (1 = Lvl 1-3, 2 = Lvl 4-6, 3 = Lvl 7-10, 4 = Lvl 11-13)", min_value=1, max_value=20, value=5)

#Creating prediction button
if st.button("Predict Price"):
    input_data = pd.DataFrame({'floor_area_sqm': [sqm], 'flat_age': [age], 'storey_rank': [floor_rank]})
    
    town_col = f"town_{town}"
    for col in model_columns:
        if col == town_col:
            input_data[col] = 1
        elif col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[model_columns]

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Resale Price: ${prediction:,.2f}")