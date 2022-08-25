import streamlit

streamlit.title('My Parents Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free Range Eggs')
streamlit.text ('Avacado Toast')

streamlit.header('Make your Own Smoothie')

import Pandas

My_Furit_List=Pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(My_Furit_List)
