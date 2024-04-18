import streamlit as st

st.set_page_config(page_title="Features Definitions", layout="centered")

st.title("Spotify Definitions")
st.header("Audio Features")
st.write("")
st.write(
    "As mentioned in the introduction, Spotify has developed an algorithm to extract the audio features from the tracks in their platform. The information is available here: https://developer.spotify.com/documentation/web-api/reference/get-audio-features."
)
st.write("")
st.write(
    "I am just going to paraphrase and summarise as best as I can the information in this section:"
)
st.write("")
st.subheader("Acousticness")
st.write("")
st.write(
    "This is a confidence measure of whether the track is acoustic or not, i.e. the track mainly uses acoustic guitars (like in MTV Unplugged sessions). It is ranged between 0 and 1."
)
st.write("")
st.subheader("Danceability")
st.write("")
st.write(
    "This is a fun one, as it determines if the track is best suited for dancing or not based on other track's characteristics (tempo, for instance). It is also ranged from 0 to 1."
)
st.write("")
st.subheader("Duration")
st.write("")
st.write(
    "The total duration of the track. Originally captured in milliseconds, but converted to minutes in integer units (meaning that a track duration of 4:30 will be seen as 4.5)."
)
st.write("")
st.subheader("Energy")
st.write("")
st.write(
    "This feature represents the perception of intensity and activity that a track has. So a higher energy song has a higher dynamic range, loudness, and so on. It is ranged between 0 and 1."
)
st.write("")
st.subheader("Explicit")
st.write("")
st.write(
    "This feature indicates if the track contains explicit content (i.e. mature themes/words)."
)
st.write("")
st.subheader("Instrumentalness")
st.write("")
st.write(
    'Instrumentalness determines if the track is entirely instrumental (meaning without vocals/lyrics) or not. This is also ranged between 0 and 1, so the closer to 1, the less "vocal" the track is (i.e. most electronic music). On the other side, the lower this value is, the most likely the track is vocal (i.e. a rap song).'
)
st.subheader("Key")
st.write("")
st.write(
    'All music is written based on a "key", which for the sake of simplyfing the term, means the set of chords/notes the track must/should follow (note the SHOULD). These originally come in numeric form, but have been transformed into letters as normally are known in the musical context: C, C#, D, D#, E, F, G, G#, A, A#, B (Do, Re, Mi, Fa, Sol, La, Si). The "#" symbol is read as "sharp", so "F#" is pronounced "Ef-sharp".'
)
st.write("")
st.subheader("Liveness")
st.write("")
st.write(
    "Here the algortihm detects if there is any audience present in the recording, therefore indicating if it is a live track or not (like in a concert). It is ranged from 0 to 1."
)
st.write("")
st.subheader("Loudness")
st.write("")
st.write(
    'Every track is recorded with certain "loudness", which could be interpreted as the physical strength of the sound. For example: the loudness is higher in a construction site than in a library. The range of this feature in the dataset is from -60 to 0 db (decibels)'
)
st.write("")
st.subheader("Mode")
st.write("")
st.write(
    'This goes in hand with the key feature. Every key has a "major" or a "minor" scale, which also determines which chords or notes to use in a song. In this case, Spotify calls the scale "mode".'
)
st.write("")
st.subheader("Speechiness")
st.write("")
st.write(
    'This detects the presence of spoken words."Spoken" is meant literally, like reading a book or speaking in a podcast, not singing. This feature is ranged between 0 and 1, so the closer to 1, the more likely the track is either a book or a podcast or a passage of some kind.'
)
st.write("")
st.subheader("Tempo")
st.write("")
st.write(
    "Here the algorithm counts the beats per minute a track has. So, it is the speed or pace of any given song (which most likely you have followed tapping with your foot or your hand). This is a free number."
)
st.write("")
st.subheader("Time Signature")
st.write("")
st.write(
    'In musical terms, a time signature means how many beats you have to fit in a bar (or measure). Most popular music uses a 4/4 time signature, which is the one most people follow using the "slaps" or "hits" of the drums.'
)
st.write("")
st.subheader("Valence")
st.write(
    'This feature detects the "positiveness" transmitted by a track. So the higher the value, the happier/cheerier the song is. This is ranged from 0 to 1.'
)
