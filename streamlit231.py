# -*- coding: utf-8 -*-
"""Streamlit231

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cwJ8vN6BxHn9vsxwJHuxTv2uV-UuRWUU
"""

# !pip install streamlit



# !streamlit hello

import streamlit as st 
from PIL import Image

import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import pandas as pd 
import numpy as np

import pandas as pd

# df=pd.read_csv('new_french.csv')
spanishdf=pd.read_csv('Spanish_cuisine.csv')
frenchdf=pd.read_csv('french_cuisine.csv')
italiandf=pd.read_csv('italian_csuisine.csv')
mexicandf=pd.read_csv('mexican_cuisine.csv')
polishdf=pd.read_csv('polish_cuisines.csv')

spanishdf = spanishdf[['Name','Description']]
frenchdf = frenchdf[['Name','Description']]
italiandf=italiandf[['Name','Description']]
mexicandf=mexicandf[['Name','Description']]
polishdf=polishdf[['Name','Description']]



# genre = st.radio(
#      "What's your favorite movie genre",
#      ('Comedy', 'Drama', 'Documentary'))

# if genre == 'Comedy':
#      st.write('You selected comedy.')
# else:
#      st.write("You didn't select comedy.")

genre = st.radio(
     "Choose the cuisine type to view the food glossary.",
     ('French', 'Spanish', 'Italian','Mexican','Polish'))

if genre == 'French':
    #  st.write(frenchdf.head())
    st.dataframe(frenchdf)
if genre ==  'Spanish':
    #  st.write(spanishdf.head())
     st.dataframe(spanishdf)
if genre == 'Italian':
    #  st.write(italiandf.head())
    st.dataframe(italiandf)
if genre ==  'Mexican':
    #  st.write(mexicandf.head())
    st.dataframe(mexicandf)
if genre ==  'Polish':
    st.dataframe(polishdf)
    #  st.write(polishdf.head())

st.markdown("# Self Exploratory Visualization on palmerpenguins")
st.markdown("Explore the dataset to know more about palmerpenguins")

# st.markdown(“**Penguins** are some of the most recognizable and beloved birds in the world and even have their own holiday: **World Penguin Day is celebrated every year on April 25**. Penguins are also amazing birds because of their physical adaptations to survive in unusual climates and to live mostly at sea. Penguins propel themselves through water by flapping their flippers.  Bills tend to be long and thin in species that are primarily fish eaters, and shorter and stouter in those that mainly eat krill.”)
# st.markdown(“The data presented are of 3 different species of penguins - **Adelie, Chinstrap, and Gentoo,** collected from 3 islands in the **Palmer Archipelago, Antarctica.**”)

# s= input('Enter your name')
# st.write('Enter your name')

# title = st.text_input('Movie title')
# st.write('The current movie title is', title)

# import numpy as np
# import matplotlib.pyplot as plt
 
  
# # creating the dataset
# data = {'C':20, 'C++':15, 'Java':30,
#         'Python':35}
# courses = list(data.keys())
# values = list(data.values())
  
# fig = plt.figure(figsize = (10, 5))
 
# # creating the bar plot
# plt.bar(courses, values, color ='maroon',
#         width = 0.4)
 
# plt.xlabel("Courses offered")
# plt.ylabel("No. of students enrolled")
# plt.title("Students enrolled in different courses")
# plt.show()

# st.pyplot(fig)

# st.bar_chart(data=df, width=0, height=0, use_container_width=True)