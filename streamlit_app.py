import streamlit
import snowflake.connector
from urllib.error import URLError
import pandas 
import requests

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




# write your own comment -what does the next line do? 


fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list;")
my_data_row = my_cur.fetchall()
streamlit.header("Fruit list contains: ")
streamlit.dataframe(my_data_row)

fruit_choice2 = streamlit.text_input('Add fruit to list: ')
streamlit.write("Thanks for adding " + fruit_choice2 + "to list :\)") 
my_cur.execute("Insert into fruit_load_list values(" + fruit_choice2 + " from streamlit)")
