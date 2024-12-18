# we will often times use an app.py instead of a workbook so here is just a placeholder for that kind of file as well!
import streamlit as st

st.title('This is my fancy app!')

st.header("This is a header")
st.subheader('This is a subheader')

st.text('This is some text.')


# 1. Layout elements
col1,col2 = st.columns(2)
col1.write('This is thing 1')
col2.write('This is thing 2')

# 2. Images
st.subheader('Images')
st.image('https://i.redd.it/on-a-scale-of-1-10-how-derpy-is-she-v0-z8gtdwu5n5zb1.jpg?width=3024&format=pjpg&auto=webp&s=345e7e1d5b45f20c733e497a9f746f4cbd3a61da',
         width=200,
         caption='A thinly veiled excuse for a cute corg!')


import numpy as np

img_data = np.random.random((200,200))
st.image(img_data, 
         caption='Random numpy data')

st.header('Altair in Streamlit')
import altair as alt

mobility_url = 'https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv'

scatters = alt.Chart(mobility_url).mark_point().encode(
    x = 'Mobility:Q',
    y=alt.Y('Population:Q', scale=alt.Scale(type='log')),
    color=alt.Color('Income:Q',
                    scale=alt.Scale(scheme='sinebow'),
                    bin=alt.Bin(maxbins=5))
)
scatters

st.markdown("""Add in altair charts with layout elements
 """)

col1,col2 = st.columns([0.7, 0.25])
col1.altair_chart(scatters, theme='streamlit',
                  use_container_width=True)
col2.markdown("Here is some text on the side of the plot.")
col2.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAXjp6mzNlkMEEiMomUfTEMiX8NHpopoyyXg&s')