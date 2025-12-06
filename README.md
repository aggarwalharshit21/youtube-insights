![Banner](https://raw.githubusercontent.com/aggarwalharshit21/youtube-insights/main/banner.png)

# 🔥 YouTube Insights Analyzer (Python + Streamlit)

A powerful YouTube analytics tool that allows you to analyze **videos**, **channels**, **trending content**, and **comment sentiment** using the **YouTube Data API v3**.  
Includes both **CLI mode** and a **full interactive Streamlit Web App**.

---

# 🚀 Features

### ✅ **1. Video Insights Analysis**
- Fetches views, likes, comments  
- Engagement score calculation  
- Auto-generated insight charts  
- Save output to CSV  

### ✅ **2. Trending Videos (Country-wise)**
- Works for IN, US, UK…  
- Displays real-time trending videos  
- Interactive charts for trending performance  

### ✅ **3. Sentiment Analysis on Comments**
- Classifies comments as Positive / Negative / Neutral  
- Shows sentiment distribution chart  

### ✅ **4. Streamlit Web App**
- Beautiful UI  
- Input multiple video IDs  
- View dashboards instantly  

---

# 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python |
| API | YouTube Data API v3 |
| Web UI | Streamlit |
| Data | Pandas |
| Charts | Matplotlib |
| NLP | Basic sentiment scoring |
| Security | `.env` API key |

---

# 📦 Installation Guide

## 1️⃣ Clone the Repository

git clone https://github.com/aggarwalharshit21/youtube-insights.git
cd youtube-insights


2️⃣ Install Requirements
pip install -r requirements.txt


3️⃣ Add API Key (Secure)

Create a .env file:
YOUTUBE_API_KEY=YOUR_API_KEY_HERE


4️⃣ Run CLI Tool
python main.py


5️⃣ Run Streamlit App
streamlit run app.py


📸 Project Screenshots


🎥 Video Insights Dashboard
(Generated from Streamlit Web App)


📈 Trending Videos Dashboard
(Country-wise trending analytics)


😊 Sentiment Analysis Output
(Emotion distribution of real YouTube comments)


📁 Project Structure
youtube-insights/
│── app.py
│── main.py
│── config.py
│── requirements.txt
│── README.md
│── video_analysis.csv
│── trending_analysis.csv
│── banner.png
│── trending.png
│── sentiment.png
│── video_dashboard.png

🤝 Contribution
Pull requests are welcome!
Feel free to suggest improvements.

⭐ Support
If you found this project useful, please consider starring ⭐ the repository.
