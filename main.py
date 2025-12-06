import pandas as pd
import matplotlib.pyplot as plt
from googleapiclient.discovery import build
from textblob import TextBlob
from config import API_KEY


def get_youtube():
    return build("youtube", "v3", developerKey=API_KEY)


def fetch_video_details(video_id):
    youtube = get_youtube()
    req = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )
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


def bulk_analyze(video_ids):
    data = []
    for vid in video_ids:
        d = fetch_video_details(vid)
        if d:
            data.append(d)
    return pd.DataFrame(data)


def fetch_channel_details(channel_id):
    youtube = get_youtube()
    req = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    )
    res = req.execute()

    if not res["items"]:
        return None

    item = res["items"][0]
    snippet = item["snippet"]
    stats = item["statistics"]

    return {
        "channel_name": snippet["title"],
        "subscribers": int(stats.get("subscriberCount", 0)),
        "total_views": int(stats.get("viewCount", 0)),
        "total_videos": int(stats.get("videoCount", 0)),
        "created_at": snippet["publishedAt"]
    }


def fetch_trending_videos(country="US", max_results=20):
    youtube = get_youtube()
    req = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode=country,
        maxResults=max_results
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

    comments = []
    for item in res["items"]:
        comments.append(item["snippet"]["topLevelComment"]["snippet"]["textDisplay"])

    return comments


def analyze_sentiment(comments):
    sentiment = {"positive": 0, "negative": 0, "neutral": 0}

    for text in comments:
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.1:
            sentiment["positive"] += 1
        elif polarity < -0.1:
            sentiment["negative"] += 1
        else:
            sentiment["neutral"] += 1

    return sentiment


def plot_sentiment(result):
    labels = list(result.keys())
    values = list(result.values())

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values)
    plt.title("Comment Sentiment Analysis")
    plt.tight_layout()
    plt.show()


def plot_views(df):
    plt.figure(figsize=(12, 5))
    plt.bar(df["title"], df["views"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Views Comparison")
    plt.tight_layout()
    plt.show()


def plot_likes(df):
    plt.figure(figsize=(12, 5))
    plt.plot(df["title"], df["likes"], marker="o")
    plt.xticks(rotation=45, ha="right")
    plt.title("Likes Comparison")
    plt.tight_layout()
    plt.show()


def plot_engagement(df):
    plt.figure(figsize=(12, 5))
    plt.bar(df["title"], df["engagement_score"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Engagement Score Comparison")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("🔥 YouTube Insights Analyzer 🔥\n")
    print("Choose an option:")
    print("1. Analyze Videos")
    print("2. Channel Statistics")
    print("3. Trending Videos by Country")
    print("4. Comment Sentiment Analysis (AI)")

    choice = input("Enter 1, 2, 3, or 4: ")

    if choice == "2":
        cid = input("Enter Channel ID: ")
        stats = fetch_channel_details(cid)
        print("\nChannel Stats:\n")
        print(stats)
        exit()

    if choice == "3":
        country = input("Enter Country Code (US, IN, UK): ").upper()
        df = fetch_trending_videos(country)
        df["engagement_score"] = (df["likes"] / df["views"]) * 100
        print("\nTrending Videos:\n")
        print(df)
        df.to_csv("trending_analysis.csv", index=False)
        plot_views(df)
        plot_engagement(df)
        exit()

    if choice == "4":
        vid = input("Enter Video ID: ")
        comments = fetch_comments(vid)
        result = analyze_sentiment(comments)
        print("\nSentiment Analysis:\n")
        print(result)
        plot_sentiment(result)
        pd.DataFrame({"comment": comments}).to_csv("comments.csv", index=False)
        exit()

    ids = input("Enter Video IDs (comma-separated): ").replace(" ", "").split(",")
    df = bulk_analyze(ids)
    df["engagement_score"] = (df["likes"] / df["views"]) * 100

    print("\nVideo Analysis:\n")
    print(df)

    df.to_csv("video_analysis.csv", index=False)
    plot_views(df)
    plot_likes(df)
    plot_engagement(df)
