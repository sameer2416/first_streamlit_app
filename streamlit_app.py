import streamlit

streamlit.title('MY Parents New Healthy Diner')

streamlit.header('Breakfast Meanu')
streamlit.text('🥣  omega 3 & blueberry oatmeal')
streamlit.text('🥗 kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled free-Range Egg')
streamlit.text('🥑🍞 Avocado Tost')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#let's put a list here so they can pick he fruits they want to include
fruits_selected=streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
                                 
#display the table on the page
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
