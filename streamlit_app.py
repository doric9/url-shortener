import streamlit as st
import pyshorteners

# Set the title
st.title("URL Shortener App")

# Get URL input
url = st.text_input("Enter a long URL:")

# Execute URL shortening when the button is pressed
if st.button("Shorten URL"):
    if url:
        # Shorten the URL
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        st.success(f"Short URL: {short_url}")
    else:
        st.error("Please enter a URL.")
