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
