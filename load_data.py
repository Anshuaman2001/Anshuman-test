import pandas as pd
import sqlite3
df = pd.read_csv('products.csv')
conn = sqlite3.connect('products.db')
df.to_sql('products', conn, if_exists='replace', index=False)
result = conn.execute('SELECT * FROM products LIMIT 5;')
for row in result:
    print(row)
conn.close()