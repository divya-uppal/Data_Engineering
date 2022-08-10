import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS

def app():

    st.header("Analysis for Tim Cook")
    st.write("Timothy Donald Cook, born November 1, 1960 is an American business executive and engineer who has been the chief executive officer of Apple Inc. since 2011. Cook previously served as the company's chief operating officer under its co-founder Steve Jobs.")
    # Data

    df = pd.read_csv('tim_cook.csv')

    st.image("Tim.jpeg", width = 200)
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
