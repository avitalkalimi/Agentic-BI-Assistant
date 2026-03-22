import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.agent_toolkits import create_sql_agent

# 1. Load environment variables
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    print("❌ ERROR: GROQ_API_KEY not found in .env file!")
    exit()

database_url = os.getenv("DATABASE_URL")
if not database_url:
    print("❌ ERROR: DATABASE_URL not found in .env file!")
    exit()

# SQLAlchemy requires 'postgresql://' not 'postgres://'
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

# 2. Connect to the Supabase PostgreSQL database
db = SQLDatabase.from_uri(
    database_url,
    include_tables=['customers', 'products', 'orders', 'order_items', 'categories', 'employees'],
    sample_rows_in_table_info=3
)

# 3. Initialize the language model
llm = ChatGroq(
    temperature=0,
    model_name="qwen/qwen3-32b",
    api_key=groq_api_key
)

# 4. Create the toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# 5. Create the Agent
# We use agent_type="openai-tools" because it's the most stable protocol
# for tool calling, even when using Groq/Qwen.
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=False,
    agent_type="openai-tools",
    max_iterations=15,
    handle_parsing_errors=True,
    max_execution_time=120
)

# 6. Run a test question
if __name__ == "__main__":
    question = "How many customers do we have in total?"
    print(f"\nQuestion asked: {question}\n")
    print("-" * 50)

    response = agent_executor.invoke({"input": question})

    print("-" * 50)
    print("\n✅ Final answer returned to the user:")
    print(response["output"])
