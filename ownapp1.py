import streamlit as st

st.sidebar.title('Menu')
add_selectbox = st.sidebar.selectbox('Options',
	('Home','Resources')
)
add_slider = st.sidebar.slider(
    'Filter by Minutes',
    0.0, 100.0, (0.0, 75.0)
)
