import streamlit as st
import pandas as pd
import numpy as np
import time

st.write("# Hello👋,Welcome to the Ownrecipe!")

st.header("	Here you can make your favourite dish,in a easy step by step process followed by our instructions.")

st.sidebar.title('Menu')
add_selectbox = st.sidebar.selectbox('Options',
	('Home','Resources')
)
Minutes = st.sidebar.slider("In minutes",0,60,5)
st.header('Line chart')
chart_data = pd.DataFrame(
	np.random.randn(20,3),
	columns = ['a','b','c']
)
st.line_chart(chart_data)
st.header("Choose Your Food!")
option = st.selectbox(
	'Favourite Food',
	('Indian','Mexican','Chinese','Thai','Italian','Japanese','French')
)
st.write('Your favourite food is ',option)

st.header('Extra Toppings!')

st.write ('What would you like to add?')

oregano = st.checkbox('Oregano')
chilliflakes = st.checkbox('Chilliflakes')
cheese = st.checkbox('Cheese')

if oregano:
     st.write("Great! Here's some more ")

if chilliflakes: 
     st.write("Okay, There you go")

if cheese:
     st.write("Here you go ")
st.header('Snacks..! ')

options = st.multiselect(
     'Your most favorite snacks',
     ['Samosa', 'Bajji', 'Puff', 'Sweets'],
     ['Samosa', 'Sweets'])
st.write('You selected:', options)

if st.button('Start'):
     st.header('Gonna,have a wonderful cooking experience')
else:
     st.write('wanna cook')
	
st.title('Baking')
my_bar = st.progress(0)
for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.subheader('Milkshake')
with st.form('my_form'):
    st.subheader('**Make your Shake**')
    milk_type_val = st.selectbox('Milk Type',['Toned','Cream'])
    milk_temp_val = st.selectbox('Milk Temp',['Hot','Medium','Cold'])
    shake_type_val = st.selectbox('Shake Type',['Regular','Medium','Standard'])
    milk_val = st.select_slider('Milk Intensity',['Low','Medium','High'])
    own_cup_val = st.checkbox('Bring own cup')

    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        You have ordered:
        - Milk Type: '{milk_type_val}'
        - Milk Temp: '{milk_temp_val}'
        - Shake Type: '{shake_type_val}'
        - Milk Intesity: '{milk_val}'
        - Bring own cup: '{own_cup_val}'
        ''')
else:
    st.write('Make your Shake!')

st.subheader('Coffee')
form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ',selected_val)

	
st.title('Biryani')

st.header('Insert Biryani pic')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
	df = pd.read_csv(uploaded_file)
	st.subheader('DataFrame')
	st.write(df)
	st.subheader('Descriptive Statistics')
	st.write(df.describe())
else:
	st.info('☝️ Upload a CSV file')
