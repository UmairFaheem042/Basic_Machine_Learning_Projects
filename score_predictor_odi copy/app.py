import pickle
import streamlit as st
import pandas as pd
import numpy as np

pipe = pickle.load(open("XGBRegressor_model.pkl", "rb"))

# Set the page configuration, including the tab title

st.set_page_config(
    page_title="Score Predictor",
    page_icon="🏏",
    layout="centered"  # Optional: Choose 'centered' or 'wide' layout
)
teams = [
    'Afghanistan',
    'Australia',
    'Bangladesh',
    'England',
    'India',
    'Ireland',
    'Pakistan',
    'New Zealand',
    'South Africa',
    'Sri Lanka',
    'West Indies',
    'Zimbabwe'
]

cities = ['Mirpur',
 'Harare',
 'London',
 'Colombo',
 'Bulawayo',
 'Sydney',
 'Abu Dhabi',
 'Rangiri',
 'Melbourne',
 'Sharjah',
 'Centurion',
 'Adelaide',
 'Perth',
 'Dubai',
 'Birmingham',
 'Auckland',
 'Johannesburg',
 'Brisbane',
 'Pallekele',
 'Wellington',
 'Dublin',
 'Southampton',
 'Hamilton',
 'Guyana',
 'Cardiff',
 'Durban',
 'Port Elizabeth',
 'Manchester',
 'Jamaica',
 'Nottingham',
 'Antigua',
 'Cape Town',
 'Belfast',
 'Trinidad',
 'Chandigarh',
 'Karachi',
 'Christchurch',
 'Hambantota',
 'Leeds',
 'Napier',
 'St Lucia',
 'Barbados',
 'Lahore',
 'Mumbai',
 'St Kitts',
 'Chester-le-Street',
 'Chittagong',
 'Ahmedabad',
 'Hobart',
 'Grenada',
 'Dhaka',
 'Jaipur',
 'Delhi',
 'Mount Maunganui',
 'Nagpur',
 'Visakhapatnam',
 'Chennai',
 'Bristol',
 'Nelson',
 'Canberra',
 'Bloemfontein',
 'Dunedin',
 'Fatullah',
 'St Vincent',
 'Kolkata',
 'Rajkot',
 'Bangalore',
 'Hyderabad',
 'Kanpur',
 'Potchefstroom',
 'Cuttack',
 'Kuala Lumpur',
 'Indore',
 'Pune',
 'Rawalpindi',
 'Benoni',
 'Paarl',
 'Multan',
 'Vadodara',
 'Ranchi',
 'East London',
 'Greater Noida',
 'Bridgetown',
 'Kochi',
 'Faisalabad',
 'Guwahati',
 'Dehra Dun',
 'Dominica',
 'Queenstown',
 'Bogra',
 'Kimberley',
 'Sylhet',
 'Chattogram',
 'Lucknow',
 'Taunton',
 'Darwin',
 'Margao',
 'Bengaluru',
 'Whangarei',
 'Gwalior'
]

st.title("Cricket Score Predictor - 50 Overs")

# Set up variables to track selections
bowling_team = None

col1, col2 = st.columns(2)
with col1:
 batting_team = st.selectbox(
  'Select Batting Team',
  sorted([team for team in teams if team != bowling_team])  # Exclude bowling team if selected
 )

# Filter the teams to exclude the selected batting team
# bowling_teams = [team for team in teams if team != batting_team]

with col2:
 bowling_team = st.selectbox(
  'Select Bowling Team',
  sorted([team for team in teams if team != batting_team])  # Exclude batting team if selected
 )

city = st.selectbox("Select City", sorted(cities))

col3, col4 = st.columns(2)
with col3:
    current_score = st.number_input("Current Score", min_value=0, step=1, format="%d")

with col4:
    wickets = st.number_input("Wickets Fell", min_value=0, max_value=9, step=1, format="%d")

col5, col6 = st.columns(2)
with col5:
    overs_completed = st.number_input("Overs Completed (min 5 overs)", min_value=5, max_value=49, step=1, format="%d")  # error checking here

with col6:
    last_five = st.number_input("Runs scored in last 5 overs", min_value=0, step=1, format="%d")

if st.button("Predict Score"):
  balls_left = 300 - (overs_completed * 6)
  wickets_left = 10 - wickets
  CRR = current_score / overs_completed

  input_df = pd.DataFrame(
   {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city], 'current_score': [current_score],
    'wickets_left': [wickets_left], 'balls_left':[balls_left], 'CRR': [CRR], 'last_five': [last_five]}
  )
  # st.table(input_df)
  result = pipe.predict(input_df)

  st.markdown(f"""
      <div style="display: flex; align-items: baseline;">
          <p style="font-size:1rem; color:rgba(255,255,255,0.5);">Predicted Score: </p>
          <h1 style="font-size:3.5rem; margin-left:10px;">{int(result[0])}</h1>
      </div>
      """, unsafe_allow_html=True)
