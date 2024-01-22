
import streamlit
python -m pip install snowflake-connector-python

streamlit.title('My parents new healthy dinner')
streamlit.header('🍕Breakfast Menu')
streamlit.text('🍓Omega 3 & Blueberry Oatmeal')
streamlit.text('🍸Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard-Boiled Free-Range Egg')
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
