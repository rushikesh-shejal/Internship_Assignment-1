import streamlit as st
from datetime import date

st.title("Person Details")

name = st.text_input("Enter your name:")


age = st.number_input("Enter your age:", min_value=1, max_value=100, step=1)


dob = st.date_input("Select your date of birth:", value=date(2000, 1, 1))

hobbies = st.multiselect(
    "Select your hobbies:",
    ["Reading", "Traveling", "Gaming", "Cooking", "Sports"]
)



if st.button("Submit"):
    
    if not name.strip():
        st.error("Please enter your name.")
    else:
        st.success("Form submitted successfully!")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Date of Birth:** {dob.strftime('%d-%m-%Y')}")
        st.write(f"**Hobbies:** {', '.join(hobbies) if hobbies else 'None'}")
        
