#TASK2
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('../db/lesson.db')

query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""


df = pd.read_sql_query(query, conn)


conn.close()


df['cumulative'] = df['total_price'].cumsum()


plt.figure(figsize=(10, 6))
plt.plot(df['order_id'], df['cumulative'], marker='o', linestyle='-', color='green')


plt.title('Cumulative Revenue Over Orders')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue')
plt.grid(True)
plt.tight_layout()


plt.show()

#TASK3
import plotly.express as px
import plotly.data as pldata
import pandas as pd
import webbrowser


df = pldata.wind(return_type='pandas')


print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))


df['strength'] = df['strength'].str.replace(r'[^\d.]', '', regex=True).astype(float)


fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title='Wind Strength vs. Frequency by Direction')


fig.write_html('wind.html')
webbrowser.open('wind.html')