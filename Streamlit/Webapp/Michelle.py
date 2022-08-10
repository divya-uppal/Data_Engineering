import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS

def app():
    st.header("Analysis for Michelle Obama")
    st.write("Michelle LaVaughn Robinson Obama bborn January 17, 1964 is an    American attorney and author who served as first lady of the United States from 2009 to 2017. She was the first African-American woman to serve in this position. She is married to former President Barack Obama.")
    # Data
    df_mo = pd.read_csv('MichelleObama.csv')
    df_bo = pd.read_csv('BarackObama.csv')
    df_jb = pd.read_csv('JoeBiden.csv')
    df_nm = pd.read_csv('narendramodi.csv')
    df_tc = pd.read_csv('tim_cook.csv')

    st.image("Michelle.jpeg", width = 200)
    pd.options.display.max_colwidth = 2000
    st.write(
    """
     **Most positive sentiment tweet**
    """
    )
    df_positive = (df_mo[(df_mo['compound'] == df_mo['compound'].max())])
    st.write(df_positive[:]['text'].values[0])

    st.write(
    """
    **Most negative sentiment tweet**
    """
    )
    pd.options.display.max_colwidth = 2000
    df_positive = (df_mo[(df_mo['compound'] == df_mo['compound'].min())])
    st.markdown("""{}""".format(df_positive[:]['text'].values[0]))

    st.write(
    """
    **Most re-tweeted tweet**
    """
    )
    df_positive = (df_mo[(df_mo['retweet_count'] == df_mo['retweet_count'].max())])
    st.write(df_positive[:]['text'].values[0])

    st.write(
    """
    **Favourite tweet of all times**
    """
    )
    df_positive = (df_mo[(df_mo['favorite_count'] == df_mo['favorite_count'].max())])
    st.write(df_positive[:]['text'].values[0])

    mean_value = (df_mo['compound'].mean())

    st.write(
    """
    **Average Sentiment associated with Tweets**
    """
    )
    st.write(mean_value)


    words = ''
    for tweet in df_mo.text.head(30000):
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
