import os

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv


def main() -> None:
    print("Starting connection test...")

    # Load environment variables from .env
    load_dotenv()

    # Get connection string
    db_url = os.getenv("DATABASE_URL")
    print(f"DATABASE_URL from env: {repr(db_url)}")

    if not db_url:
        print("No DATABASE_URL found in environment. Please check your .env file.")
        return

    # Normalize postgres URL prefix for SQLAlchemy
    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    try:
        # Create engine
        engine = create_engine(db_url)
        print("Engine created successfully. Running test query...")

        # Simple test query – you can change this to a table that exists in your DB
        query = "SELECT 1 AS ok;"

        df = pd.read_sql(query, engine)

        print("✅ Connection succeeded! Sample result:")
        print("-" * 30)
        print(df)

    except Exception as e:
        print("❌ Error while connecting or running query:")
        print(e)


if __name__ == "__main__":
    main()