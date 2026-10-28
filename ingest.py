import pandas as pd
import duckdb
import random
from datetime import datetime, timedelta

# 1. Tạo dữ liệu giả lập (Extract)
data = []
start_date = datetime(2023, 10, 1)
for i in range(1, 101): # Tạo 100 đơn hàng
    date = start_date + timedelta(days=random.randint(0, 10))
    status = random.choice(['completed', 'completed', 'completed', 'returned', 'pending'])
    amount = random.randint(20000, 150000)
    data.append([i, date.strftime('%Y-%m-%d'), status, amount])

df = pd.DataFrame(data, columns=['order_id', 'order_date', 'status', 'amount'])

# 2. Kết nối tới DuckDB (Load)
con = duckdb.connect('jaffle_shop.db')

# 3. Đẩy dữ liệu vào bảng raw_orders_python
con.execute("CREATE OR REPLACE TABLE raw_orders_python AS SELECT * FROM df")

print("✅ Đã tạo và nạp 100 dòng dữ liệu vào bảng 'raw_orders_python' thành công!")
con.close()