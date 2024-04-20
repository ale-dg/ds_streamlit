import sklearn.preprocessing
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import warnings
import sklearn

warnings.filterwarnings("ignore")

pio.templates.default = "plotly_dark"

pd.set_option("display.precision", 2)

df = pd.read_csv("pages/csv_files/data_1950s.csv")
df["explicit"] = df["explicit"].map({0: "Not Explicit", 1: "Explicit"})


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


st.set_page_config(page_title="1950s Analysis", layout="wide")

st.title("Review of 1950s songs")

st.write("")

st.write(
    'We saw in the overall data that the 1950s were the least popular songs, the quieter ones, the most acoustic... but we need to contextualise this. Spotify is a recent platform for music which is mainly used by the younger part of the population at its fullest, meaning they vote for their artists, they follow them and so on. The older generations, in general, do not get so involved with these technologies, at the most they just push play and listen to their favourite tracks, hence the "older" music gets less "popular".'
)

st.write("")

st.write(
    'However, this does not mean this was a "bad" decade. The 1950s began to bring the music to the masses and we began to have a lot of different genres around. More instruments were being integrated in the music and a lot of legendary artists began to be recognised, together with their producers and their record labels.'
)

st.write("")

st.write("So, let me show you a summary of the features of the 1950s:")

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
    "speechiness",
    "tempo",
]

new_df = df[cols].mean()
new_df["loudness"] = (new_df["loudness"] * -1) / 10
new_df["tempo"] = new_df["tempo"] / 100
new_df = new_df.to_frame()
new_df = new_df.rename(
    index={"loudness": "loudness x 10", "tempo": "tempo x 100"}, columns={0: "mean"}
).sort_index()
new_df.index = new_df.index.str.capitalize()

fig = px.bar(
    data_frame=new_df,
    y=new_df.index,
    x="mean",
    orientation="h",
    color=new_df.index,
    color_discrete_sequence=px.colors.qualitative.Pastel1,
    text_auto=".2f",
)

fig.update_layout(
    title={"text": "Mean values per musical feature", "font": {"size": 24}},
    showlegend=False,
)

st.plotly_chart(fig, use_container_width=True)
del new_df

st.write(
    "So we can see *Acousticness* in the higher side, which might be explained by the fact this decade still depended on a lot of acoustic instruments (not just acoustic guitar), i.e. piano, violin, etc."
)

st.write("")

st.write(
    'In the "middle" are *Danceability* and *Valence*: the first one refers to the suitability of a track for dancing, so indeed there were some tracks from those days which were composed for dancing and some are still valid up to today. The latter refers to the positiveness or negativeness of a song (the lower, the more negative/sad/angry...), so a 0.5 average indicates a balance on this, but the data could be skewed.'
)

st.write("")

st.write(
    'On the lower side: Energy, Instrumentalness, Liveness and Speechiness. Energy refers to the "intensity" of a track, so if we compare most of the tracks of the 1950s genres against, say, the 1980s indeed they will seem less energetic. Instrumentalness refers to the lack of vocals in the track as the value in this feature increases, therefore it should not be strange the values are low as most songs contain vocals/lyrics. Liveness indicates the presence of an audience, so basically measures if the track was recorded live or not, hence it should also not be surprising most of the tracks are in the lower side as live recordings are not the norm. Finally, Speechiness measures the presence of spoken words in the track, for example a rap song will be high and an audiobook will be close or actually 1, a normal song will be in the lower side.'
)

st.write("")

fig = px.bar(
    data_frame=(df["explicit"].value_counts().reset_index(drop=False)),
    y="explicit",
    x="count",
    orientation="h",
    color="explicit",
    color_discrete_sequence=px.colors.qualitative.Pastel1,
    text_auto=True,
)

fig.update_layout(
    title={"text": "Count of explicit tracks", "font": {"size": 24}},
    xaxis_title="Count",
    yaxis_title="",
    showlegend=False,
)
st.plotly_chart(fig, use_container_width=True)

st.write("")

st.write(
    'As mentioned before, not so many tracks were considered "explicit" as there was not a mandatory "rating" system in place, but it is also true that barely any songs contained any explicit lyrics.'
)

st.write("")

fig = px.bar(
    data_frame=(df["key_mode"].value_counts().reset_index(drop=False)),
    x="key_mode",
    y="count",
    color="key_mode",
    color_discrete_sequence=px.colors.qualitative.Pastel1,
    text_auto=True,
)

fig.update_layout(
    title={"text": "Count of tracks per key", "font": {"size": 24}},
    xaxis_title="Count",
    yaxis_title="",
    showlegend=False,
)
st.plotly_chart(fig, use_container_width=True)

st.write("")

st.write(
    "We can see the main key used was C - major, and the next ones are F and G major, with not so much difference between them."
)

st.write("")

st.write(
    "Now, I will plot the 50 most popular artists of the decade. I will filter the data based on how many tracks were released (minimum 30) and the popularity of the artist will be averaged."
)

st.write("")

scaler = sklearn.preprocessing.MinMaxScaler()

new_df = df.groupby(["first_artist"], as_index=False)["popularity"].agg(
    {"mean", "count"}
)

new_df["mean"] = scaler.fit_transform(new_df["mean"].to_numpy().reshape(-1, 1))

new_df = new_df.query("count >= 30")

new_df = (
    new_df.sort_values(by="mean", ascending=True)
    .drop("count", axis=1)
    .reset_index(drop=True)
    .tail(50)
)

fig = px.bar(
    data_frame=new_df,
    y="first_artist",
    x="mean",
    color="mean",
    color_continuous_scale=px.colors.sequential.Sunset,
    orientation="h",
    labels={"first_artist": "Artist", "mean": "Popularity"},
)

fig.update_layout(
    title={"text": "Top 50 artist by popularity", "font": {"size": 24}},
    coloraxis_colorbar={
        "title": "Popularity (mean)",
        "thicknessmode": "pixels",
        "thickness": 20,
        "lenmode": "pixels",
        "len": 300,
        "yanchor": "top",
        "xanchor": "right",
        "y": 1.05,
        "x": 0.95,
        "orientation": "h",
    },
    margin={"r": 10, "l": 10, "b": 10},
    height=1500,
    xaxis_title="Popularity",
    yaxis_title="Artist",
)

fig.update_yaxes(tickfont={"size": 14})
st.plotly_chart(fig, use_container_width=True)

artist_df = pd.DataFrame()

for i in new_df["first_artist"].unique():
    artist_df = pd.concat([artist_df, df.query("first_artist==@i")], axis=0)

artist_df = artist_df.reset_index(drop=True)

st.write(
    "You can select an artist in the top 50 if you would like to see the average value of the features of the tracks they have recorded in the decade:"
)

artist_list = artist_df["first_artist"].unique().tolist()
artist_list.sort()

select_artist = st.selectbox("Select artist:", artist_list)

artist_df = artist_df.groupby("first_artist", as_index=False)[cols].mean()

artist_df["loudness"] = (artist_df["loudness"] * -1) / 10
artist_df["tempo"] = artist_df["tempo"] / 100
artist_df = artist_df.rename(
    columns={"loudness": "loudness x 10", "tempo": "tempo x 100"}
)
artist_df.columns = artist_df.columns.str.capitalize()

plot_df = artist_df.query("First_artist == @select_artist")

plot_df = plot_df.T.iloc[1:, :].sort_index(ascending=True).reset_index(drop=False)


fig = px.bar(
    data_frame=plot_df,
    y="index",
    x=plot_df.columns[1],
    color="index",
    color_discrete_sequence=px.colors.qualitative.Pastel1,
    orientation="h",
    text_auto=".2f",
)

fig.update_layout(
    title={"text": f"Features for artist {select_artist}", "font": {"size": 24}},
    legend={"title": "Feature"},
    xaxis_title="Value",
    yaxis_title="Feature",
)

st.plotly_chart(fig, use_container_width=True)

st.write("")

st.write(
    "Now, just for your review, you can review the extended data of each feature below, plotted as histogram and boxplot"
)

st.write("")

cols.sort()

for i in cols:
    fig = fun_subplots_plotly(df, i)
    st.plotly_chart(fig, use_container_width=True)
    st.write("")
