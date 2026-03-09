# 📊 Agentic BI

> Chat with your database using plain English — powered by LangChain, Groq & Streamlit

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-SQL%20Agent-1C3C3C?logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Llama%203-F55036?logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 💬 **Natural language queries** — ask questions about your data in plain English
- 📈 **Auto-generated charts** — request bar charts, line graphs, and more
- 🔒 **Read-only & secure** — no INSERT, UPDATE, DELETE, or DROP ever executed
- 🛡️ **Prompt injection protection** — built into the system prompt
- 🧠 **Business insights** — every response ends with an actionable insight
- 💾 **Chat history** — charts and answers persist across the conversation

---

## 🖥️ Demo

```
You:       "Who are my top 3 customers by sales? Show a bar chart."
Assistant: The top 3 customers are John Doe, Jane Smith, and Bob Johnson.
           [bar chart rendered]
           Business insight: These 3 customers account for 70% of total sales.
```

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| AI Agent | LangChain SQL Agent (`tool-calling`) |
| LLM | Groq — `llama-3.3-70b-versatile` |
| Database | Supabase (PostgreSQL) |
| Charts | Plotly Express & Graph Objects |
| Config | python-dotenv |

---

## 📁 Project Structure

```
data-ai-assistant/
├── app.py            # Streamlit UI — chat interface, chart rendering, session history
├── agent.py          # LangChain SQL agent — LLM, toolkit, executor
├── .env              # Environment variables (never committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/data-ai-assistant.git
cd data-ai-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgres://user:password@host:5432/dbname
GROQ_API_KEY=your_groq_api_key_here
DEBUG=false
```

> **Note:** The app automatically converts `postgres://` → `postgresql://` for SQLAlchemy compatibility.

### 4. Run the app

```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501**

---

## ⚙️ Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABASE_URL` | ✅ | PostgreSQL connection string (Supabase → Settings → Database) |
| `GROQ_API_KEY` | ✅ | API key from [console.groq.com](https://console.groq.com) → API Keys |
| `DEBUG` | ❌ | Set to `true` to enable verbose agent logging in terminal |

---

## 💬 Example Questions

```
"How many customers do we have in total?"
"Who are the top 5 customers by revenue? Show a bar chart."
"Show me monthly sales as a line chart."
"Which product category has the highest average order value?"
"Compare sales performance across regions."
```

---

## 🔒 Security

- ✅ **Read-only** — agent cannot run `INSERT`, `UPDATE`, `DELETE`, or `DROP`
- ✅ **Prompt injection protected** — system prompt rejects persona-change attempts
- ✅ **No credential leaking** — API keys and connection strings never appear in responses
- ✅ **No metadata exposure** — internal table structure is not revealed to users

---

## ⚠️ Groq Free Tier Limits

The free tier allows **100,000 tokens/day**. If you hit the limit:

**Option A** — Switch to a smaller model in `agent.py`:
```python
model_name="llama-3.1-8b-instant"  # ~4x fewer tokens per request
```

**Option B** — Disable verbose logging:
```env
DEBUG=false
```

**Option C** — Upgrade at [console.groq.com/settings/billing](https://console.groq.com/settings/billing)

---

## 🐛 Known Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| `px.DataFrame` error | LLM confuses `px` (Plotly) with `pd` (Pandas) | Auto-corrected with `code.replace()` before `exec` |
| Charts lost on page refresh | Streamlit rerenders wipe widget state | Charts saved in `st.session_state` and replayed |
| Vague axis labels | LLM uses generic `x`/`y` labels | Be explicit: *"with Customer Name on the x-axis"* |

---

## 📦 Requirements

```txt
streamlit
langchain
langchain-community
langchain-groq
plotly
pandas
sqlalchemy
psycopg2-binary
python-dotenv
groq
```

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

*Built with LangChain + Groq + Streamlit*
