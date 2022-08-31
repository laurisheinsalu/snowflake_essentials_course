import streamlit
import pandas
import snowflake.connector

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My Parents New Healthy Diner')


streamlit.header('Breakfast Menu')

streamlit.text('Eggs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

import requests


# write your own comment -what does the next line do? 


fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list;")
my_data_row = my_cur.fetchall()
streamlit.header("Fruit list contains: ")
streamlit.dataframe(my_data_row)

fruit_choice2 = streamlit.text_input('Insert fruit: ')
streamlit.write('The user entered ', fruit_choice2)
my_data_row.append(fruit_choice2)
streamlit.text(my_data_row)
# fruityvice_response2 = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice2)
# fruityvice_normalized2 = pandas.json_normalize(fruityvice_response2.json())
# write your own comment - what does this do?
# streamlit.dataframe(fruityvice_normalized2)
