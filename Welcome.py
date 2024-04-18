import streamlit as st

import streamlit as st

st.set_page_config(page_title="Spotify Exploration", layout="centered")

st.title("Spotify Analysis")
st.header("Welcome! 👋")
st.write("")
st.write(
    "Thank you for visiting Streamlit site! If you are uncertain of the purpose of this site, let me give you a brief explanation here."
)
st.write("")
st.write(
    'Music 🎶🎶 has been all around us since remote times. Even there have been archaeological findings where some items have been believed to be used as musical instruments.Even so, the last centuries have been marked with the most "access" to music in time. This access has been changing considerably with the invention of the LP, the cassette, the CD and so on, and currently we are in the streaming era.'
)
st.write("")
st.write(
    "Now, what has interested me is the change in music styles and its characteristics in the last years, especially since the 1950s. A lot of great musicians, songwriters, producers, etc, have passed from that time and, most interestingly, most of them based on the roots of the Blues music style."
)
st.write("")
st.write(
    "Fortunately for me, Spotify has invested great resources in developing an algorithm to retrieve some audio features from the tracks uploaded in their platform. On the left you will find which features will be. Also, thanks to the open community, some developers have scrapped these features for a lot of songs and made them available as datasets in Kaggle.com, where you can find them and download them. Reworking this information, I was able to get around 140,000 songs with its features for showing if these features change over time or not."
)
st.write("")
st.write(
    "Hope you find this information as interesting as I did! If you would like to get a glimpse on how I have generated some of the graphs, you can visit a notebook I have created in Kaggle here: https://www.kaggle.com/code/aldggr/some-fun-visualisations, where you can leave any comments and any feedback is more than welcome."
)
