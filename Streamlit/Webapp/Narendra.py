import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS

def app():

    st.header("Analysis for Narendra Modi")
    st.write("Narendra Damodardas Modi, born 17 September 1950 is an Indian politician serving as the 14th and current prime minister of India since 2014. Modi was the chief minister of Gujarat from 2001 to 2014 and is the Member of Parliament from Varanasi. He is a member of the Bharatiya Janata Party and of the Rashtriya Swayamsevak Sangh, a right-wing Hindu nationalist paramilitary volunteer organisation. He is the first prime minister to have been born after India's independence in 1947 and the second prime minister not belonging to the Indian National Congress to have won two consecutive majorities in the Lok Sabha, or the lower house of India's parliament. He is also the longest serving prime minister from a non-Congress party.")
    # Data

    df = pd.read_csv('narendramodi.csv')

    st.image("Narendra.jpeg", width = 200)
    pd.options.display.max_colwidth = 2000
    st.write(
    """
     **Most positive sentiment tweet**
    """
    )
    df_positive = (df[(df['compound'] == df['compound'].max())])
    st.write(df_positive[:]['text'].values[0])

    st.write(
    """
    **Most negative sentiment tweet**
    """
    )
    pd.options.display.max_colwidth = 2000
    df_positive = (df[(df['compound'] == df['compound'].min())])
    st.markdown("""{}""".format(df_positive[:]['text'].values[0]))

    st.write(
    """
    **Most re-tweeted tweet**
    """
    )
    df_positive = (df[(df['retweet_count'] == df['retweet_count'].max())])
    st.write(df_positive[:]['text'].values[0])

    st.write(
    """
    **Favourite tweet of all times**
    """
    )
    df_positive = (df[(df['favorite_count'] == df['favorite_count'].max())])
    st.write(df_positive[:]['text'].values[0])

    mean_value = (df['compound'].mean())

    st.write(
    """
    **Average Sentiment associated with Tweets**
    """
    )
    st.write(mean_value)


    words = ''
    for tweet in df.text.head(30000):
        words= words + tweet
    stopwords_add = STOPWORDS
    stopwords_add.update(["RT", "Michelle", "Obama", "MichelleObama","https","Barack","BarackObama","Joe","Biden","Joe Biden", "President","Tim","Cook","Tim Cook","Apple","Narendra","Modi","Narendra Modi"," Prime minister","Potus","White House","narendramodi","Tim","Cook","CEO","Co","iPhone"])
    wordcloud = WordCloud(stopwords=stopwords_add, background_color='white', width=400 , height=200).generate(words)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot()
