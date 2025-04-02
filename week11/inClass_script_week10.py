# we will often times use an app.py instead of a workbook so here is just a placeholder for that kind of file as well!
import streamlit as st

st.title('This is my app!')

st.header('Header')
st.subheader('subheader')

# add in images
st.subheader('Images')
st.image('https://i.redd.it/on-a-scale-of-1-10-how-derpy-is-she-v0-z8gtdwu5n5zb1.jpg?width=3024&format=pjpg&auto=webp&s=345e7e1d5b45f20c733e497a9f746f4cbd3a61da', 
         width=200, 
         caption='A thinly veiled excuse for a derpy corgi.')

import numpy as np
img_data = np.random.random((200,200))
st.image(img_data, caption='random data')

st.header('Altair in Streamlit')