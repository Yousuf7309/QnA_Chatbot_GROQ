# Simple Q&A Chatbot with Groq

This is a simple **Streamlit-based Q&A chatbot** built using **LangChain** and **Groq** models.  
The chatbot, named **Jarvis**, answers user queries with a joyful and friendly tone.

---

## 🚀 Features

- Built using **Streamlit** for a quick web-based interface.
- Integrated with **Groq’s LLaMA models** for generating responses.
- Customizable model, temperature, and token settings from the sidebar.
- Responds to questions in a conversational and cheerful manner.

---

## 🧠 Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **LangChain-Groq**
- **dotenv**

---

## 📁 Project Structure
QnA_Chatbot_GROQ/
│
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── .env # Environment variables (not uploaded)
└── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Yousuf7309/QnA_Chatbot_GROQ.git
cd QnA_Chatbot_GROQ

2. Create a virtual environment
python -m venv venv

Activate it

3. Install dependencies
pip install -r requirements.txt

4. Add environment variables
Create a .env file in the root directory and add:
LANGCHAIN_API_KEY=your_langchain_api_key_here
GROQ_API_KEY=your_groq_api_key_here

⚠️ Important: Do not upload the .env file to GitHub.

▶️ Run the Application
streamlit run app.py

Then open the app in your browser at:
http://localhost:8501


🧩 How It Works


The user enters a question in the text input field.


The app sends the query to the selected Groq model via LangChain.


The model returns a response which is displayed in the Streamlit interface.


The user can adjust the temperature and max tokens in the sidebar.



🧰 Requirements
streamlit
langchain
langchain_groq
langchain_core
python-dotenv


🌐 Deployment (Optional)
If you want to deploy this app to Streamlit Cloud:


Push your code to GitHub (without .env).


Go to https://share.streamlit.io.


Connect your GitHub repository.


Add your API keys under Secrets in Streamlit:
LANGCHAIN_API_KEY = your_langchain_api_key
GROQ_API_KEY = your_groq_api_key



Deploy 🚀



👨‍💻 Author
Mohammed Yousuf

⭐ Support
If you found this project helpful, consider giving it a star on GitHub ⭐


