# 📬 MailMind – Your AI-Powered Gmail Summarizer & Life Organizer

MailMind is a personal **multimodal AI assistant** that reads your Gmail inbox, summarizes important emails, extracts tasks & deadlines, and helps you stay productive — all powered by **Gemini 1.5 Flash** and the **Agno Agent SDK**.

---

## 🚀 Features

✅ **Gmail Summarization**  
Uses Google's Gemini API to summarize the most recent emails and extract only what matters.

✅ **Task & Deadline Extraction**  
Parses out tasks, meetings, or reminders from your messages to help you stay on top of things.

✅ **Agent-Based Design (Agno SDK)**  
Each AI agent has a role: summarizer, extractor, scheduler, recommender (planned).

✅ **Modular & Scalable**  
Easily expandable with calendar sync, voice interface, productivity suggestions, and more.

---

## 🧠 How It Works

1. Authenticates with Gmail and fetches the latest messages  
2. Feeds the content to a Gemini-powered agent using Agno SDK  
3. Agent extracts tasks, summaries, or routines from the messages  
4. Future expansion includes calendar updates, habit reminders, and personalized advice

---

## 🛠️ Tech Stack

- **Python**
- **Gemini 1.5 Flash API** (Google)
- **Agno SDK** (for agent orchestration)
- **Gmail API** (OAuth2)
- `.env` for API key security
- CLI interface (Streamlit or voice UI planned)

---

## 📸 

<img width="1522" height="449" alt="image" src="https://github.com/user-attachments/assets/714fa327-8853-4c71-8bd1-490690e3247d" />

---

## 📦 Setup Instructions

```
# Clone the repo
git clone [https://github.com/BhagyeshPatil2004/MailMind.git](https://github.com/BhagyeshPatil2004/Gmail_Summarizer_Agent-MailMind)
cd MailMind

# Install dependencies
pip install -r requirements.txt

# Add your Gemini API key in a .env file
GEMINI_API=your_api_key_here

# Run the agent
python main.py

```

## 📝Note!
If "gmail_agent.py" not works Use "If-gmail_agent-not-work-use-This.py" this may help you.

## ⭐ Show Your Support!
If you like this project:

🌟 Star the repo

🪄 Suggest features in new Features,Projects.

🔁 Share with your peers
