# import time
# t=time.strftime('%H:%M:%S')
# print(t)
# hour=int(time.strftime('%H'))
# if(hour>=0 and hour<12):
#     print('good morning sir')
# elif(hour>=12 and hour<17):
#     print('good afternoon sir')
# elif(hour>=17 and hour<0):
#     print('good night sir')

# string format time is used to convert time into strings

# import time
# t=time.strftime('%H:%M:%S')
# print(t)
# t=time.strftime('%H')
# print(t)
# t=time.strftime('%M')
# print(t)
# t=time.strftime('%S')
# print(t)
 
# AIzaSyA2fvsbW0Ma8Jc37qGTk1z-4F4HgGjnhm8

import streamlit as st
import google.generativeai as genai

Gemini_key = "AIzaSyA2fvsbW0Ma8Jc37qGTk1z-4F4HgGjnhm8"

name = st.text_input("Enter your name")
                
if name:

    if Gemini_key:
        genai.configure(api_key = Gemini_key)

        model = genai.GenerativeModel("gemini-1.5-flash")

        st.text(f"Hello it is working\nCarry on")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        user_input = st.chat_input("Ask CoderGroup.ai")
        if user_input:

            st.chat_message("user").markdown(user_input)

            gemini_response = model.generate_content(user_input).parts[0].text
            
            with st.chat_message("assistant"):
                st.markdown(gemini_response)
            
            st.session_state.messages.append({"role":"user", "content": user_input})
            st.session_state.messages.append({"role":"model", "content": gemini_response})


 