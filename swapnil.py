import streamlit as st
import joblib
import time
import pandas as pd
st.markdown("<h1 style='text-align: center;'>Hello World</h1>", unsafe_allow_html=True)
gv = open("dean.pkl","rb")
model = joblib.load(gv)
a= st.selectbox("Select  gender",['Select','Male','Female'])
b=st.number_input("Enter Age",min_value=1,value=1)
c= st.selectbox("Select maritial status",['Select','Married','Not married'])
d=st.number_input("Enter number of children",min_value=0,value=1)
st.info("Rate your education level between 1 to 5")
e=st.number_input("Enter eudcation level",min_value=1,value=1,max_value=5)
f=st.number_input("Enter number of family members",min_value=0,value=1)
g=st.number_input("Enter your total gained asset till now in Indian rupees",min_value=0,value=1)
h=st.number_input("Enter your durable asset till now Indian rupees",min_value=0,value=1)
i=st.number_input("Enter your living expenses in Indian rupees",min_value=0,value=1)
j=st.number_input("Enter your other expenses in Indian rupees",min_value=0,value=1)
k= st.selectbox("Do you receive salary",['Select','Yes','No'])
l= st.selectbox("Do you receive  income from your own farm",['Select','Yes','No'])
m= st.selectbox("Do you receive  income from any business other than your job and farm",['Select','Yes','No'])
n= st.selectbox("Do you categorize your work under primary labour category",['Select','Yes','No'])
o=st.number_input("Enter your investment in any field (if any) in Indian rupees",min_value=0,value=0)
if(a=="Male"):
    a=1
elif(a=="Female"):
    a=0
if(c=="Married"):
    c=1
elif(c=="Not married"):
    c=0

if(k=="Yes"):
    k=1
elif(k=="No"):
    k=0
if(l=="Yes"):
    l=1
elif(l=="No"):
    l=0
if(m=="Yes"):
    m=1
elif(m=="No"):
    m=0
if(n=="Yes"):
    n=1
elif(n=="No"):
    n=0
if st.button("Predict"):
    with st.spinner('Wait for it... '):
        time.sleep(3)
    z=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
    r=model.predict([z])[0]
    if(r==1):
        st.success("Sorry....But you need treatment")
    elif(r==0):
        st.balloons()
        st.success("Congratulations....You are normal")
    chart_data = pd.DataFrame(model.predict_proba([z])*100,columns=["not depressed",'depressed'],index=['Status'])
    st.markdown("<h3 style='text-align: center;'>Probabilty chart of prediction of model</h3>", unsafe_allow_html=True)
    st.bar_chart(chart_data,width=5)

            



