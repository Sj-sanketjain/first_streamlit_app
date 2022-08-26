import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free Range Eggs')
streamlit.text ('Avacado Toast')

streamlit.header('Make your Own Smoothie')
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected= streamlit.multiselect("Pick Some Fruit:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#create the repeatable block

def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
   fruityvice_normalized = pd.json_normalize(fruityvice_response.json())  # json to dataframe
   return fruityvice_normalized
#New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
 else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.write('The user entered ', fruit_choice)
    streamlit.dataframe(fruityvice_normalized) # print dataframe

except URLError as e:
 streamlit.error()

streamlit.text("The fruit load list contains:")
# snowflake-relate-functions
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return  my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

streamlit.stop()

fruit_add = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('The user entered ', fruit_add)

my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('test')")
