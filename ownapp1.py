import streamlit as st
import pandas as pd
import numpy as np
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
if st.button('Start'):
	st.write('Gonna,have a wonderful cooking experience')
`else:
	st.write('wanna cook')
st.write('You selected:', options)
