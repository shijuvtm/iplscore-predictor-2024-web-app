import streamlit as st
import pandas as pd
import os
def app():
   # Define the path to the Excel file
   EXCEL_FILE = 'user_data.xlsx'

   # Initialize the Excel file if it doesn't exist
   if not os.path.exists(EXCEL_FILE):
      df = pd.DataFrame(columns=['Username', 'Password'])
      df.to_excel(EXCEL_FILE, index=False)

   def save_user_data(username, password):
      # Load existing data
      df = pd.read_excel(EXCEL_FILE)

      # Add new user data
      new_data = pd.DataFrame({'Username': [username], 'Password': [password]})
      df = pd.concat([df, new_data], ignore_index=True)

      # Save back to Excel
      df.to_excel(EXCEL_FILE, index=False)

   # Streamlit login page
   st.title(':blue[User login]')

   username = st.text_input('Username')
   password = st.text_input('Password', type='password')

   if st.button('Login'):
      if username and password:
         save_user_data(username, password)
         st.success(f'Welcome, {username}!')
      else:
         st.error('Please enter both username and password')