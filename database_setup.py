import sqlite3

# Create a new SQLite database or connect to an existing one
conn = sqlite3.connect('recipes.db')
c = conn.cursor()

# Create a table for recipes
c.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        ingredients TEXT NOT NULL,
        instructions TEXT,
        rating INTEGER
    )
''')

conn.commit()
conn.close()

print("Database setup complete.")
