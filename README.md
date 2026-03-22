# 📊 Agentic BI

> Chat with your database using plain English — powered by LangChain, Groq & Streamlit

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.39-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-SQL%20Agent-1C3C3C?logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Qwen3--32B-F55036?logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E?logo=supabase&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 💬 **Natural language queries** — ask questions about your data in plain English
- 📈 **Auto-generated charts** — request bar charts, line graphs, pie charts, and more
- 🔒 **Read-only & secure** — no INSERT, UPDATE, DELETE, or DROP ever executed
- 🛡️ **Prompt injection protection** — built into the system prompt
- 🧠 **Business insights** — every chart response ends with an actionable insight
- 💾 **Persistent chat history** — charts and answers remain interactive across the entire conversation
- ☁️ **Cloud-ready** — uses Supabase (PostgreSQL) so it works for real users online
- 🎨 **Dark-mode friendly** — transparent chart backgrounds, consistent color palette

---

## 🖥️ Demo

```
You:       "Who are my top 5 customers by total spending? Show a bar chart."
Assistant: [bar chart rendered — chart first, then explanation]
           The top 5 customers by total spending are Jane Smith ($12,400), ...
           Business insight: These 5 customers account for 35% of total revenue.
```

```
You:       "What is the total revenue?"
Assistant: The total revenue is $1,114,594.01.
           Business insight: Strong overall performance — consider segmenting by category to identify growth areas.
```

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit 1.39 |
| AI Agent | LangChain SQL Agent (`openai-tools`) |
| LLM | Groq — `qwen/qwen3-32b` |
| Database | Supabase (PostgreSQL) |
| Charts | Plotly Express & Graph Objects |
| Config | python-dotenv |

---

## 📁 Project Structure

```
Agentic BI/
├── app.py                  # Streamlit UI — chat interface, chart rendering, session history
├── agent.py                # LangChain SQL agent — LLM, toolkit, executor
├── generate_mock_data.py   # Seeds Supabase with realistic mock business data
├── test_connection.py      # Quick sanity-check for DB + agent connectivity
├── data/
│   ├── customers.csv       # Exported after seeding (for reference)
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   ├── categories.csv
│   └── employees.csv
├── .env                    # Environment variables (never committed)
├── .env.example.           # Template for required environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🗄️ Database Schema

The app uses a Supabase PostgreSQL database with 6 tables:

| Table | Description |
|-------|-------------|
| `customers` | Customer profiles (name, email, city, join date) |
| `products` | Product catalog with price and category |
| `categories` | Product categories |
| `orders` | Order headers (date, status, assigned employee) |
| `order_items` | Line items linking orders → products + quantities |
| `employees` | Sales staff assigned to orders |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/agentic-bi.git
cd agentic-bi
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a Supabase project

1. Go to [supabase.com](https://supabase.com) and create a free project
2. Navigate to **Settings → Database**
3. Copy the **Connection string** (URI format)

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:[your-password]@db.[your-project-ref].supabase.co:5432/postgres
GROQ_API_KEY=your_groq_api_key_here
```

> **Get your Groq API key** at [console.groq.com](https://console.groq.com) → API Keys

> **Tip:** For the app (read queries only), you can create a read-only Supabase user. For seeding, use the full `postgres` user.

### 5. Seed the database with mock data

```bash
python generate_mock_data.py
```

This creates all 6 tables in your Supabase database and fills them with realistic mock business data (150 customers, 45 products, 400 orders, etc.).

> ⚠️ **Note:** The seed script **drops and recreates all tables** on each run. Use the full `postgres` user (not a read-only user) in your `.env` when seeding.

### 6. Run the app

```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501**

---

## ⚙️ Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABASE_URL` | ✅ | Supabase PostgreSQL connection string (Settings → Database → URI) |
| `GROQ_API_KEY` | ✅ | API key from [console.groq.com](https://console.groq.com) → API Keys |

---

## 🌐 Deploying to the Cloud

Because the app uses Supabase (a cloud PostgreSQL database), you can deploy it for real users:

### Streamlit Cloud (recommended — free)

1. Push your code to GitHub (make sure `.env` is in `.gitignore`)
2. Go to [share.streamlit.io](https://share.streamlit.io) → New app
3. Select your repo and set `app.py` as the entry point
4. Under **Advanced settings → Secrets**, add:
   ```toml
   DATABASE_URL = "postgresql://..."
   GROQ_API_KEY = "gsk_..."
   ```
5. Click **Deploy** — your app is live at a public URL

> Streamlit Cloud reads secrets the same way Python reads `.env`, so no code changes needed.

---

## 💬 Example Questions

**Plain text answers:**
```
"How many customers do we have?"
"What is the total revenue?"
"Which category has the most products?"
"What is the average order value?"
```

**Charts:**
```
"Show orders by status as a pie chart."
"Who are the top 5 customers by spending? Show a bar chart."
"Show monthly new customers as a line chart."
"Show average product price by category as a bar chart."
"Which employees generated the most revenue? Show a chart."
"Show the top 5 best-selling products by quantity sold."
```

---

## 🔒 Security

- ✅ **Read-only database user** — `ai_read_only` role with SELECT-only grants; `INSERT`, `UPDATE`, `DELETE`, and `DROP` are impossible at the database level
- ✅ **Row Level Security (RLS)** — Supabase RLS enabled on all 6 tables with explicit SELECT policies
- ✅ **Prompt injection protection** — regex guard scans every user message before it reaches the LLM; blocks "ignore previous instructions", `curl`, `os.system`, and similar patterns instantly
- ✅ **AST sandbox on `exec()`** — every LLM-generated Python code block is parsed with Python's `ast` module before execution; `import os`, `subprocess`, `eval`, `__import__` and other dangerous calls are blocked
- ✅ **Sanitized error messages** — full errors are logged server-side only; users see only safe generic messages
- ✅ **No verbose logging** — SQL queries and agent internals are never logged to production
- ✅ **No credential leaking** — API keys and connection strings are stored in `.env` / Streamlit secrets and never appear in responses or logs

---

## ⚠️ Groq Free Tier Limits

The free tier allows **6,000 tokens/min** and **100,000 tokens/day**. If you hit the limit:

**Option A** — Switch to a smaller model in `agent.py`:
```python
model_name="llama-3.1-8b-instant"  # ~4x fewer tokens per request
```

**Option B** — Upgrade at [console.groq.com/settings/billing](https://console.groq.com/settings/billing)

---

## 🐛 Known Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| `px.DataFrame` error | LLM confuses `px` (Plotly) with `pd` (Pandas) | Auto-corrected with `code.replace()` before `exec` |
| Charts lost on page refresh | Streamlit re-renders wipe widget state | Charts stored in `st.session_state` and re-executed on replay |
| Rate limit error (429) | Groq free tier: 6,000 tokens/min | Wait 30 seconds and retry |
| Seed script fails | Read-only DB user used for seeding | Use the full `postgres` user in `.env` when running `generate_mock_data.py` |

---

## 📦 Requirements

```txt
faker>=22.0.0
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
pandas>=2.0.0,<3.0
python-dotenv>=1.0.0
langchain==1.2.10
langchain-groq==1.1.2
langchain-community==0.4.1
plotly==6.6.0
streamlit==1.39.0
altair==5.5.0
```

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

*Built with LangChain + Groq (Qwen3-32B) + Supabase + Streamlit*
