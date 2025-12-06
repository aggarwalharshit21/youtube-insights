![YouTube Insights Analyzer Banner](assets/banner.png)




# 🎥 YouTube Insights Analyzer  
### 🔥 Full-Stack YouTube Data Intelligence Tool (Python • Streamlit • NLP)

Analyze any YouTube video, channel, trending region, and user comments using a single unified system powered by:

✔ YouTube Data API  
✔ Python Data Analysis  
✔ Streamlit Web UI  
✔ AI-based Sentiment Analysis  

This is a **portfolio-grade project** showcasing real API integration, data processing, NLP, and dashboard design.

---

# 🚀 Features

### 🎬 **1. Video Performance Analyzer**
- Fetch views, likes, comments, channel name  
- Auto-calculate engagement score  
- Visual charts (bar, line)  
- Export CSV  

### 📺 **2. Channel Statistics**
- Subscribers  
- Total views  
- Total videos  
- Channel creation timestamp  

### 🌎 **3. Trending Videos (By Country)**
- Fetch top 20 trending videos  
- Engagement comparison  
- Data visualization  
- Country-based insights  

### 🤖 **4. Comment Sentiment Analysis (AI Powered)**
- Fetch top 100 comments  
- Natural Language Processing (TextBlob)  
- Positive / Negative / Neutral distribution  
- Sentiment chart + CSV export  

### 🖥 **5. Streamlit Web App UI**
- Clean sidebar menu  
- Interactive visualizations  
- One-click results  
- Web-based dashboard experience  

---

# 🏗️ Project Architecture

```
youtube-insights/
│── main.py                # Console analyzer (CLI)
│── app.py                 # Streamlit Web App UI
│── config.py              # API key storage
│── requirements.txt       # All dependencies
│── README.md              # Documentation
│── assets/
│     └── banner.png       # Project Banner
│── output/
      ├── video_analysis.csv
      ├── trending_analysis.csv
      └── comments.csv
```

---

# 🖼️ Screenshots

> (Add your screenshots here after running the app)  
> Create an "assets" folder and upload images.

### 📌 Video Insights Dashboard  
![Video Screenshot](assets/video_dashboard.png)

### 📌 Trending Analyzer  
![Trending Screenshot](assets/trending.png)

### 📌 Sentiment Analysis  
![Sentiment Screenshot](assets/sentiment.png)

---

# 📦 Installation

### 1️⃣ Clone the project

```sh
git clone https://github.com/aggarwalharshit21/youtube-insights.git
cd youtube-insights
```

### 2️⃣ Install dependencies

```sh
pip install -r requirements.txt
python -m textblob.download_corpora
```

### 3️⃣ Add your API key

Edit `config.py`:

```python
API_KEY = "YOUR_YOUTUBE_API_KEY"
```

---

# ▶️ Running the Console App

```sh
python main.py
```

Options:

```
1 → Video Analysis
2 → Channel Stats
3 → Trending Videos
4 → Sentiment Analysis (AI)
```

---

# 🌐 Running the Streamlit Web App

```sh
streamlit run app.py
```

Streamlit will auto-open in your browser.

---

# 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Programming | Python |
| API | YouTube Data API v3 |
| NLP | TextBlob |
| UI Framework | Streamlit |
| Visualization | Matplotlib |
| Data Processing | Pandas |

---

# 🌱 Future Enhancements

- Comment summarization using GPT  
- Predictive analytics (views prediction using ML)  
- Dark mode UI  
- Deploy on Streamlit Cloud / Render  
- Add thumbnail preview & video metadata  

---

# ⭐ Why This Project Stands Out

- Real-time data from YouTube  
- Shows both **data engineering + data analytics + AI skills**  
- Includes a rich UI dashboard  
- Highly scalable project architecture  
- Perfect for resumes, LinkedIn, and interviews  

---

# 👤 Author  
### **Harshit Aggarwal**  
If you like this project, please ⭐ star the repository on GitHub!

