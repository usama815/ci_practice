import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings 
warnings.filterwarnings("ignore")
import streamlit as st
st.title("power calculator")
st.write("This app calculates the power of a statistical test based on user inputs.")

n=st.number_input("Enter an integer:", value=1,step=1)
# calculate result
square=n**2
cube=n**3
fifth_power=n**5
# Display result]
st.write(f"the square of {n} is: {square}")
st.write(f"the cube of {n} is: {cube}")
st.write(f"the fifth_power of {n} is: {fifth_power})")