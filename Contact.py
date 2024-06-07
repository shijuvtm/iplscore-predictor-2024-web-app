import streamlit as st
import pandas as pd
from datetime import datetime
def app():
    # Function to save data to an Excel file
    def save_to_excel(data, filename='contact_data.xlsx'):
        try:
            # Try to load existing data
            df_existing = pd.read_excel(filename)
            df = pd.concat([df_existing, data], ignore_index=True)
        except FileNotFoundError:
            # If the file does not exist, create a new one
            df = data
        
        df.to_excel(filename, index=False)

    st.title("Contact")

    # Create the form
    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        
        submit_button = st.form_submit_button(label='Submit')

    # Handle form submission
    if submit_button:
        if name and email and message:  # Ensure no fields are empty
            data = pd.DataFrame({
                'Name': [name],
                'Email': [email],
                'Message': [message],
                'Timestamp': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
            })
            save_to_excel(data)
            st.write("Thank you for your message, {}!".format(name))
            st.write("We have received your message and will get back to you at {}.".format(email))
            st.write("Your message: {}".format(message))
        else:
            st.error("Please fill in all fields.")