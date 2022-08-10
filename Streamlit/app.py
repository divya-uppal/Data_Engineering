import streamlit as st


from multipage import MultiPage
from Webapp import Michelle,Barack,Joe,Narendra,Tim
st.set_page_config(layout = "wide")
# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Sentiment analysis of tweet mentioning World Leaders")


st.sidebar.title("Sentiment Analysis of Tweets")
st.sidebar.markdown("This application is a Streamlit dashboard used to analyze sentiments of tweets linked to leaders of the world 🐦")

# Add all your applications (pages) here
app.add_page("Barack Obama", Barack.app)
app.add_page("Joe Biden", Joe.app)
app.add_page("Michelle Obama", Michelle.app)
app.add_page("Narendra Modi",Narendra.app)
app.add_page("Tim Cook",Tim.app)

# The main app
app.run()
