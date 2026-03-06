import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq 
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.agent_toolkits import create_sql_agent

# 1. Load environment variables
load_dotenv()

# Get Database URL and format it correctly
db_url = os.getenv("DATABASE_URL")
if db_url and db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

# Get the Groq API Key explicitly
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    print("❌ ERROR: Groq API Key not found in .env file!")
    exit()

# 2. Connect to the database (Supabase) via LangChain
db = SQLDatabase.from_uri(
    db_url,
    include_tables=['customers', 'products', 'orders', 'order_items', 'categories', 'employees'], 
    sample_rows_in_table_info=3 
)

# 3. Initialize the language model (Groq with Llama 3 70B)
llm = ChatGroq(
    temperature=0,
    #model_name="llama-3.3-70b-versatile", 
    model_name="llama-3.1-8b-instant",
    api_key=groq_api_key
)

# 4. Create the toolkit 
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# 5. Create the Agent
# We use agent_type="openai-tools" because it's the most stable protocol 
# for tool calling, even when using Groq/Llama.
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type="openai-tools", # <--- Changed this from tool-calling
    max_iterations=15,
    handle_parsing_errors=True
)

# 6. Run a test question
if __name__ == "__main__":
    question = "How many customers do we have in total?"
    print(f"\nQuestion asked: {question}\n")
    print("-" * 50)
    
    # Execute the agent
    response = agent_executor.invoke({"input": question})
    
    print("-" * 50)
    print("\n✅ Final answer returned to the user:")
    print(response["output"])