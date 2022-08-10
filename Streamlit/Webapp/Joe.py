import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS

def app():

    st.header("Analysis for Joe Biden")
    st.write("Joseph Robinette Biden Jr.; born November 20, 1942 is an American politician who is the 46th and current president of the United States. A member of the Democratic Party, he previously served as the 47th vice president from 2009 to 2017 under President Barack Obama and represented Delaware in the United States Senate from 1973 to 2009.")
    # Data

    df = pd.read_csv('JoeBiden.csv')

    st.image("Joe.jpeg", width = 200)
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

    #st.write(
    #"""
    #**Favourite tweet of all times**
    #"""
    #)
    #df_positive = (df[(df['favorite_count'] == df['favorite_count'].max())])
    #st.write(df_positive[:]['text'].values[0])

    mean_value = (df['compound'].mean())

    st.write(
    """
    **Average Sentiment associated with Tweets**
    """
    )
    st.write(mean_value)


    words = ''
    for tweet in df.text.head(30000):
        words= words + str(tweet)
    stopwords_add = STOPWORDS
    stopwords_add.update(["RT", "Michelle", "Obama", "MichelleObama","https","Barack","BarackObama","Joe","Biden","Joe Biden", "President","Tim","Cook","Tim Cook","Apple","Narendra","Modi","Narendra Modi"," Prime minister","Potus","White House","narendramodi","Tim","Cook","CEO","Co","iPhone","JoeBiden"])
    wordcloud = WordCloud(stopwords=stopwords_add, background_color='white', width=400 , height=200).generate(words)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot()
