# Agentic BI – Mock Data for Small Business

Python script to generate realistic mock data and tables for a small-business BI project.

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python3 generate_mock_data.py
```

By default this creates a `data/` folder with a SQLite file `small_business.db` and CSV files for each table.

### Parameters (optional)

| Parameter      | Default          | Description                  |
|----------------|------------------|------------------------------|
| `--customers`  | 150              | Number of customers          |
| `--categories` | 8                | Number of categories         |
| `--products`   | 45               | Number of products           |
| `--employees`  | 8                | Number of employees          |
| `--orders`     | 400              | Number of orders             |
| `--output-dir` | data             | Output directory             |
| `--db-name`    | small_business.db| DB file name                 |
| `--no-csv`     | -                | Disable CSV export           |

Example:

```bash
python3 generate_mock_data.py --customers 300 --orders 1000 --output-dir ./my_data
```

## Tables (schema)

- **categories** – product categories (food, beverages, cleaning, etc.)
- **customers** – customers (name, email, phone, city)
- **products** – products (name, category, price, cost, stock, SKU)
- **employees** – employees (name, role, hire date, salary)
- **orders** – orders (customer, employee, date, status, total)
- **order_items** – order line items (order, product, quantity, price, line total)

## Output

- `data/small_business.db` – SQLite database with all tables
- `data/*.csv` – one CSV file per table (for Excel, Power BI, etc.)

## Re-running

Each run **overwrites** the existing DB file in the same output directory. To keep past data, copy the files elsewhere or change `--output-dir` / `--db-name`.

## DATABASE_URL (PostgreSQL / Supabase)

You can store your PostgreSQL connection string in a `.env` file for use with SQLAlchemy or other tools:

```env
DATABASE_URL="postgresql://postgres.[your-project-ref]:[your-password]@aws-0-eu-central-1.pooler.supabase.com:6543/postgres"
```

Replace `"[your-project-ref]"` and `"[your-password]"` with your real Supabase project ref and password.
