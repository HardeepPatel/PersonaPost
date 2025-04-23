# ✨ PersonaPost

> 🧠 *Create high-quality LinkedIn posts that sound just like you – in seconds.*

<img src="resources/tool.jpg"/>

## 📌 Overview

**GenAI Post Generator** helps LinkedIn influencers automate the process of writing new posts by learning from their existing writing style.  
Let’s say **Mohan**, a popular influencer, wants help writing future content. He can:

1. Upload his past LinkedIn posts 🗂️  
2. The tool will extract writing patterns: topics, language, length, and tone 📊  
3. Mohan can then select the desired attributes and click "Generate" ⚙️  
4. A new post is generated using few-shot learning with similar past posts, keeping his unique voice intact 🗣️✨

---

## 🏗️ Technical Architecture

<img src="resources/architecture.jpg"/>

1. **Stage 1:** Extract metadata (topic, language, length, tone) from previous posts using NLP techniques 🔍  
2. **Stage 2:** Feed selected parameters into the model to generate a new post, using a few-shot learning approach to replicate writing style 🧾➡️📝

---

## 🚀 Getting Started

### 🔐 Step 1: API Key
Get your **GROQ API Key** from here:  
👉 https://console.groq.com/keys

Then create a `.env` file and add:
```env
GROQ_API_KEY=your_api_key_here
```

---

### 📦 Step 2: Install Dependencies
Run the following command to install required packages:
```bash
pip install -r requirements.txt
```

---

### ▶️ Step 3: Launch the App
Start the Streamlit app with:
```bash
streamlit run main.py
```

---

## 🛡️ License & Terms

This project is licensed under the **MIT License**.  
However:

- **🚫 Commercial use is strictly prohibited** without prior written permission from the author (https://github.com/codebasics).
- **✅ Attribution is required** in all copies or substantial portions of the software.

---

## 🧾 Credits

Built with ❤️ from inspiration from **Codebasics Inc.**  & **Dhaval Patel**
💡🤖
