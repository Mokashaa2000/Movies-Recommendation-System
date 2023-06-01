import pandas as pd
#import numpy as np
import streamlit as st
import joblib
from scipy.sparse import csr_matrix
import scipy
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",150)
pd.set_option("expand_frame_repr", False)
pd.option_context("mode.dtype_backend","pyarrow")
filename = "piv.csv"
df =pd.read_csv(filename)
df = df.set_index("title")
titles = df.index.tolist()
modelname = "Completed_model.joblib"
model = joblib.load(modelname)



st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpapercave.com/w/wp1945897");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )




st.write('''
    ## Movies Recommendation system
    
    this is a movierecommendation system web app that use collabrative filtering to recommend movies base on other's
    people ratings


    ## Dataset
    the dataset used in this system is the small version of Movie Lens dataset which contains 100,000 ratings and 3,600 tag applications applied to 9,000 movies by 600 users

    ## Algorithm Used
    for this model I decided to keep the model as simple as possible.
    this model was built using Knearest neighbors and with cosine similarity applied.



''')


user_inbut = st.selectbox("Kindly Choose a Movie ",titles)
user_inbut= str(user_inbut)

st.write("You selected: ",user_inbut)

number = st.selectbox("How many Recommendations you'd like me to generate ? ",list(range(1,16)))
st.write("You selected: ",number)


choose = df[df.index == user_inbut].values.reshape(1,-1)

distances, indices = model.kneighbors(choose,n_neighbors=number)

def generate():
    distances, indices = model.kneighbors(choose,n_neighbors=number+1)
    for i in range(0,len(distances.flatten())):

        if i==0:
            st.write("I Recommend that you watch \n")
            pass
        else:
            st.write(f"{i}: {df.index[indices.flatten()[i]]} movie")

if st.button("Click To Generate Recommendations"):

    generate()
