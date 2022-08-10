import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS

def app():

    st.header("Analysis for Barack Obama")
    # Data
    st.write("Barack Hussein Obama II born August 4, 1961 is an American politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, he was the first African-American president of the United States. Obama previously served as a U.S. senator from Illinois from 2005 to 2008 and as an Illinois state senator from 1997 to 2004.")
    df = pd.read_csv('BarackObama.csv')

    st.image("Barack.jpeg", width = 200)
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
