# 💬 E-commerce ChatBot (Gen AI RAG Project using LLaMA 3.3 & GROQ)

This is a **Proof of Concept (POC)** for an intelligent chatbot specifically designed for an **e-commerce platform**. The chatbot enhances user experience by understanding natural language queries and identifying user intent with precision. It uses **Retrieval-Augmented Generation (RAG)** with **LLaMA 3.3** via the **GROQ API** to deliver accurate and real-time responses.

🔍 It integrates with the platform’s database, enabling dynamic interactions such as fetching products or answering platform-related FAQs.

---

## 📹 Demo Video

🎥 [Watch Demo Video](https://youtu.be/rhh1rkA4w28)

---

## 📸 Screenshots

| Chat UI with Query | FAQ Response |
|--------------------|---------------|
| ![Chat UI](app/resources/Chatbot_UI) |![FAQ](app/resources/FAQ) |

---

## 📁 Folder Structure

```
.
├── app/              # All the chatbot code (Streamlit app, logic, routing)
├── web-scraping/     # Web scraper for e-commerce product data
```

---

## 💡 Supported Intents

The chatbot currently supports two main types of user intents:

1. **FAQ Intent**  
   Responds to general questions about the platform's policies and services.  
   _Example:_  
   > Is online payment available?

2. **SQL Intent**  
   Executes live queries on the product database to return relevant results.  
   _Example:_  
   > Show me all Nike shoes below ₹3000

---

## 🧠 Architecture

```
User Query ➡️ Router ➡️ (FAQ or SQL) ➡️ GROQ (LLaMA 3.3) ➡️ Response ➡️ Chat Interface
```

![FAQ](app/resources/architecture-diagram)

---

## ⚙️ Set-up & Execution

1. **Install Dependencies**

   ```bash
   pip install -r app/requirements.txt
   ```

2. **Create a `.env` file inside the `app/` folder with your GROQ credentials:**

   ```
   GROQ_MODEL=llama-3.3-70b-versatile
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Run the Streamlit app**

   ```bash
   streamlit run app/main.py
   ```

---

## 🧑‍💻 Created by

**rohesen** 👨‍💻  
_This project is part of a learning journey with Codebasics._

---

## 📜 License & Terms

This project is licensed under the **MIT License**.

However, please note the following:

- **❌ Commercial use is strictly prohibited** without **prior written permission** from the author.
- ✅ You must give **attribution** in all copies or substantial portions of the software.

> © Codebasics Inc. All rights reserved.

---

Feel free to ⭐️ star the repo or raise an issue if you find this useful or want to collaborate!
