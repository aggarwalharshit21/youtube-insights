import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from googleapiclient.discovery import build
from textblob import TextBlob
from config import API_KEY

st.set_page_config(page_title="YouTube Analyzer", layout="wide")


def get_youtube():
    return build("youtube", "v3", developerKey=API_KEY)


def fetch_video_details(video_id):
    youtube = get_youtube()
    req = youtube.videos().list(part="snippet,statistics", id=video_id)
    res = req.execute()

    if not res["items"]:
        return None

    item = res["items"][0]
    snippet = item["snippet"]
    stats = item["statistics"]

    return {
        "title": snippet["title"],
        "channel": snippet["channelTitle"],
        "views": int(stats.get("viewCount", 0)),
        "likes": int(stats.get("likeCount", 0)),
        "comments": int(stats.get("commentCount", 0))
    }


def fetch_channel(cid):
    youtube = get_youtube()
    req = youtube.channels().list(part="snippet,statistics", id=cid)
    res = req.execute()

    if not res["items"]:
        return None

    item = res["items"][0]
    stats = item["statistics"]

    return {
        "channel_name": item["snippet"]["title"],
        "subscribers": int(stats.get("subscriberCount", 0)),
        "views": int(stats.get("viewCount", 0)),
        "videos": int(stats.get("videoCount", 0)),
        "created": item["snippet"]["publishedAt"]
    }


def fetch_trending(country="US"):
    youtube = get_youtube()
    req = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode=country,
        maxResults=20
    )
    res = req.execute()

    data = []
    for item in res["items"]:
        snippet = item["snippet"]
        stats = item["statistics"]
        data.append({
            "title": snippet["title"],
            "channel": snippet["channelTitle"],
            "views": int(stats.get("viewCount", 0)),
            "likes": int(stats.get("likeCount", 0)),
            "comments": int(stats.get("commentCount", 0))
        })

    return pd.DataFrame(data)


def fetch_comments(video_id):
    youtube = get_youtube()
    req = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )
    res = req.execute()

    return [
        item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        for item in res["items"]
    ]


def analyze_sentiment(comments):
    result = {"positive": 0, "negative": 0, "neutral": 0}

    for c in comments:
        polarity = TextBlob(c).sentiment.polarity
        if polarity > 0.1:
            result["positive"] += 1
        elif polarity < -0.1:
            result["negative"] += 1
        else:
            result["neutral"] += 1

    return result


st.title("🔥 YouTube Insights Analyzer (Web App)")

mode = st.sidebar.selectbox(
    "Choose an option",
    ["Video Analysis", "Channel Stats", "Trending Videos", "Comment Sentiment AI"]
)

if mode == "Video Analysis":
    ids = st.text_input("Enter Video IDs (comma-separated)")
    if st.button("Analyze"):
        videos = ids.replace(" ", "").split(",")
        data = [fetch_video_details(v) for v in videos]
        df = pd.DataFrame([d for d in data if d])
        df["engagement"] = (df["likes"] / df["views"]) * 100
        st.write(df)
        st.bar_chart(df.set_index("title")["views"])

elif mode == "Channel Stats":
    cid = st.text_input("Enter Channel ID")
    if st.button("Fetch Stats"):
        st.write(fetch_channel(cid))

elif mode == "Trending Videos":
    country = st.text_input("Enter Country Code (IN, US, UK)")
    if st.button("Fetch Trending"):
        df = fetch_trending(country.upper())
        st.write(df)
        st.bar_chart(df.set_index("title")["views"])

elif mode == "Comment Sentiment AI":
    vid = st.text_input("Enter Video ID")
    if st.button("Analyze"):
        comments = fetch_comments(vid)
        result = analyze_sentiment(comments)
        st.write(result)
        st.bar_chart(result)
