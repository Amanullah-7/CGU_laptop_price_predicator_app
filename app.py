import streamlit as st
import numpy as np
import pickle
lr_model=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor App")
st.write("This app is created using the data taken from kaggle website.")
st.write("The prediction here is based on the data available, hence might not align perfectly with the real-life data.")

company=st.selectbox("Laptop Manufacturer",df['Company'].unique(),index=4)
typename=st.selectbox("Type of Laptop",df['TypeName'].unique(),index=1)
cpu=st.selectbox("Processor",df['Cpu'].unique(),index=0)
cpu_speed=st.slider("CPU Clock Speed",min_value=0.8,max_value=4.0,step=0.1,value=2.5)
ram=st.radio("Amount of RAM on the system",[4,6,8,12,16,24,32,64,128],index=2,horizontal=True)
gpu=st.selectbox("Graphics Card on the system",df['Gpu'].unique(),index=1)
os=st.selectbox("Operating System",df['OpSys'].unique(),index=2)
weight=st.slider("Weight of the laptop in kg",min_value=0.6,max_value=5,step=0.2,value=2.0)
ips=st.selectbox("Does the laptop display have IPS Panel?")
touchscreen=st.selectbox("does the laptop have a touchscreen?",["Yes","No"],index=1)
ssd=st.selectbox("Does the laptop have SSD?",["Yes",["No"]])
hdd=st.selectbox("What is the HDD storage of the laptop if laptop only have SSD select 0",[0,128,256,512,1024,2048],index=0)
screen_size=st.slider("Screen isze(in inches,measured diagonally)",min_value=10.0,max_value=18.5,step=0.1,value=15.6
                      )
