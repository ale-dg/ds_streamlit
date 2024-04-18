import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import warnings

warnings.filterwarnings("ignore")

pio.templates.default = "plotly_dark"

pd.set_option("display.precision", 2)

df = pd.read_csv("pages/csv_files/clean_data.csv")
df["artist_track"] = df["first_artist"] + " - " + df["name"]


def fun_subplots_plotly(df, col):

    mean_val = df[col].mean()
    median_val = df[col].median()
    fig = make_subplots(rows=1, cols=2, column_widths=[0.75, 0.25])

    fig.add_trace(
        go.Histogram(
            x=df[col], name=f"Histogram {col}", marker={"color": "#EBA0AC"}, nbinsx=50
        ),
        row=1,
        col=1,
    )

    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=-1,
        x1=1,
        y0=mean_val,
        y1=mean_val,
        row=1,
        col=2,
        line={"color": "#A6E3A1", "width": 3, "dash": "dot"},
    )

    fig.add_shape(
        type="line",
        xref="paper",
        yref="y",
        x0=-1,
        x1=1,
        y0=median_val,
        y1=median_val,
        row=1,
        col=2,
        line={"color": "#CBA6F7", "width": 3, "dash": "dot"},
    )

    fig.add_annotation(
        xref="paper",
        x=-0.7,
        y=mean_val,
        showarrow=True,
        arrowhead=2,
        text=f"Mean = {mean_val:.2f}",
        row=1,
        col=2,
    )

    fig.add_annotation(
        xref="paper",
        x=0.7,
        y=median_val,
        showarrow=True,
        arrowhead=2,
        text=f"Median = {median_val:.2f}",
        row=1,
        col=2,
    )

    fig.add_trace(
        go.Box(y=df[col], name=f"Boxplot {col}", marker={"color": "#F9E2AF"}),
        row=1,
        col=2,
    )

    fig.update_layout(
        title={"text": f"Distribution Plot {col}", "font": {"size": 24}},
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1,
        },
    )
    fig.update_yaxes(title_text="Count", row=1, col=1)
    fig.update_yaxes(title_text=f"{col}", row=1, col=2)
    fig.update_xaxes(title_text=f"{col}", row=1, col=1)
    fig.update_xaxes(title_text="", row=1, col=2)

    return fig


st.set_page_config(page_title="Overall Analysis", layout="wide")

st.title("Overall Information")
st.write("")
st.header("A very general overview")
st.write("")
st.write("")

st.write(
    "Here I am going to show the overall information of all the data, and in the subsequent sections I will go through each decade beginning from 1950."
)

st.write("")

st.write(
    "I will be plotting the information in different types of graphs, including an explanation and what it represents based on the definitions we have reviewed in the previous section. You can hover over the information to see specific numbers should you want to do it, zoom over certain information, etc."
)

st.write("")

st.write(
    "But first things first... Below a graph showing how many tracks are per decade:"
)

st.write("")

fig = px.bar(
    data_frame=(
        df["decade"].value_counts().sort_values(ascending=False).reset_index(drop=False)
    ),
    y="decade",
    x="count",
    color="count",
    color_continuous_scale=px.colors.sequential.Sunset,
    text_auto=True,
)

fig.update_layout(
    title={"text": "Total songs per decade", "font": {"size": 24}},
    xaxis_title="Count",
    yaxis_title="Decades",
    coloraxis_colorbar={
        "title": "Count",
        "thicknessmode": "pixels",
        "thickness": 20,
        "lenmode": "pixels",
        "len": 300,
        "yanchor": "top",
        "xanchor": "right",
        "y": 1.2,
        "x": 0.95,
        "orientation": "h",
    },
    margin={"r": 10},
)
st.plotly_chart(fig, use_container_width=True)

st.write("")

st.write(
    'A bit quite obvious once plotted: the 1950s are the less represented decade and the 2010s are the most represented. This to me makes sense as recently has become easier to record a song and upload it to Spotify than it was in the 50s to record a LP and place it on the radio (you can look for the term "payola", should you want to dig into why it was difficult back in those days).'
)

st.write("")

st.write(
    "Now, below I will do some general analysis of all the features, nothing too specific as otherwise the page would be too large. As mentioned before, on each decade I will be digging a bit on each audio feature."
)

st.subheader("An overall oversight")
st.write("")

cols = [
    "valence",
    "acousticness",
    "danceability",
    "duration_min",
    "energy",
    "instrumentalness",
    "liveness",
    "loudness",
    "popularity",
    "speechiness",
    "tempo",
]

decade_mean = df.groupby("decade")[cols].mean()

fig = make_subplots(
    rows=4,
    cols=3,
    subplot_titles=(
        decade_mean.columns[0],
        decade_mean.columns[1],
        decade_mean.columns[2],
        decade_mean.columns[3],
        decade_mean.columns[4],
        decade_mean.columns[5],
        decade_mean.columns[6],
        decade_mean.columns[7],
        decade_mean.columns[8],
        decade_mean.columns[9],
        decade_mean.columns[10],
    ),
    vertical_spacing=0.1,
)

fig.add_trace(
    go.Bar(
        y=decade_mean.index,
        x=decade_mean.iloc[:, 0],
        name=decade_mean.columns[0],
        orientation="h",
    ),
    row=1,
    col=1,
)

fig.add_trace(
    go.Bar(
        y=decade_mean.index,
        x=decade_mean.iloc[:, 1],
        name=decade_mean.columns[1],
        orientation="h",
    ),
    row=1,
    col=2,
)

fig.add_trace(
    go.Bar(
        y=decade_mean.index,
        x=decade_mean.iloc[:, 2],
        name=decade_mean.columns[2],
        orientation="h",
    ),
    row=1,
    col=3,
)

fig.add_trace(
    go.Bar(
        y=decade_mean.index,
        x=decade_mean.iloc[:, 3],
        name=decade_mean.columns[3],
        orientation="h",
    ),
    row=2,
    col=1,
)

fig.add_trace(
    go.Bar(
        y=decade_mean.index,
        x=decade_mean.iloc[:, 4],
        name=decade_mean.columns[4],
        orientation="h",
    ),
    row=2,
    col=2,
)

fig.add_trace(
    go.Bar(
        y=decade_mean.index,
        x=decade_mean.iloc[:, 5],
        name=decade_mean.columns[5],
        orientation="h",
    ),
    row=2,
    col=3,
)

fig.add_trace(
    go.Bar(
        y=decade_mean.index,
        x=decade_mean.iloc[:, 6],
        name=decade_mean.columns[6],
        orientation="h",
    ),
    row=3,
    col=1,
)

fig.add_trace(
    go.Bar(
        y=decade_mean.index,
        x=decade_mean.iloc[:, 7],
        name=decade_mean.columns[7],
        orientation="h",
    ),
    row=3,
    col=2,
)

fig.add_trace(
    go.Bar(
        y=decade_mean.index,
        x=decade_mean.iloc[:, 8],
        name=decade_mean.columns[8],
        orientation="h",
    ),
    row=3,
    col=3,
)

fig.add_trace(
    go.Bar(
        y=decade_mean.index,
        x=decade_mean.iloc[:, 9],
        name=decade_mean.columns[9],
        orientation="h",
    ),
    row=4,
    col=1,
)

fig.add_trace(
    go.Bar(
        y=decade_mean.index,
        x=decade_mean.iloc[:, 10],
        name=decade_mean.columns[10],
        orientation="h",
    ),
    row=4,
    col=2,
)

fig.update_layout(
    title={"text": "Average Musical Values per Decade", "font": {"size": 22}},
    legend={
        "orientation": "v",
        "yanchor": "top",
        "y": 0.2,
        "xanchor": "right",
        "x": 0.9,
    },
    margin={"b": 10, "r": 10},
    height=980,
)

st.plotly_chart(fig, use_container_width=True)

del decade_mean

st.write(
    'We can observe several things: apparently, the most recent decade has been the saddest on terms of tracks... the new century has been the less acoustic (RIP MTV Unplugged), but overtime we have become more prone to dance. The duration of the songs has been around the same, but it has been decreasing the last decades and also the energy has been increasing over the decades, but the 2010s saw a reversal on the trend. The instrumentalness of the tracks has gone dramatically backwards decade after decade and the songs have been recorded "louder" (probably due to advancements on technology, but there is also a "loudness" war going on). Speechiness has been low overall, even though the graph seems like a dramatic reduction and the tempo has been around the same.'
)

st.write("")

st.write(
    'I did not mention the popularity because it is not really comparable. Spotify is mainly used by younger generations, and they (we) listen to more modern music than older generations, therefore the popularity of newer tracks will be higher than older tracks, especially when not so "known" songs are in the mix. When going in deep per decade we will rescale this to show a more accurate figure per decade.'
)

st.write("")

st.write(
    "Now let us see other features, such as the evolution of explicit songs and per key/scale."
)

df["explicit"] = df["explicit"].map({0: "Not Explicit", 1: "Explicit"})

fig = px.bar(
    data_frame=(
        df.groupby(["decade", "explicit"], as_index=False)["year"]
        .count()
        .rename(columns={"year": "count"})
    ),
    x="decade",
    y="count",
    color="explicit",
    color_discrete_sequence=px.colors.qualitative.Pastel1,
    text_auto=True,
)

fig.update_layout(
    title={"text": "Count of explicit tracks per decade", "font": {"size": 24}},
    barmode="group",
    xaxis_title="Decade",
    yaxis_title="Count",
    legend={"title": "Explicit"},
)

st.plotly_chart(fig, use_container_width=True)

st.write("")

st.write(
    'Well... apparently we have become more liberal with the lyrics overtime. Although, it is important to highlight that in 1985 there was a big Congressional hearing in the US regarding the "filthy" songs and the outcome was the labeling of songs/records with a rating system similar to the film industry, and many countries maybe had banned and/or had rules before or after that, so it is hard to say if the lyrics have become more "explicit" over time or simply they have become easier to identify based on the previously mentioned rating system.'
)

st.write("")

key_mode_decade = pd.pivot_table(
    data=df, index="key_mode", columns="decade", values="first_artist", aggfunc="count"
)

fig = px.imshow(
    key_mode_decade.T,
    aspect="auto",
    color_continuous_scale=px.colors.sequential.Sunset,
    text_auto=True,
)

fig.update_layout(
    title={"text": "Count of songs per key per decade", "font": {"size": 24}},
    coloraxis_colorbar={
        "title": "Count",
        "thicknessmode": "pixels",
        "thickness": 20,
        "lenmode": "pixels",
        "len": 500,
        "yanchor": "top",
        "xanchor": "right",
        "y": 1.2,
        "x": 0.99,
        "orientation": "h",
    },
    margin={"r": 10},
    width=1200,
    yaxis_title="Decade",
    xaxis_title="Key",
)

st.plotly_chart(fig, use_container_width=True)

del key_mode_decade

st.write("")

st.write(
    'It is evident that certain keys and modes have been mostly chosen through the decades. This is also a normal behaviour as the most used keys are "pleasent" to the ear and easy to follow, whereas other keys normally are more complex for both playing and to follow by ear and, sometimes, hard to play in most instruments used in popular music.'
)

st.write()

st.write(
    'Also the genre plays a role in the selection of the key: mainstream music normally use the most used keys seen in the graph above and genres such as jazz may even change key and scales through the song. Other factors such as the vocal range of the singer also play a BIG role: Whitney Houston, Mariah Carey, Beyoncé, Celine Dion, Freddie Mercury are examples of singers whose vocal ranges are so wide that they could sing in varied keys and they actually have different "genres" of songs (mostly mainstream, but you get the idea).'
)
