import numpy as np
import pandas as pd
from faker import Faker

n = 1500000
num_customers = 20000
num_products = 500
payment_modes = ["Card", " Card ", "caSh", "netbankIng", "Cod", "COD", "UPI"]
fake = Faker()

#test

order_ids = np.arange(2250000, 3750000)
customer_ids = np.random.randint(10001, num_customers+1, size = n)
product_ids = np.random.randint(1, num_products+1, size = n)
amounts = np.random.normal(loc = 2000, scale = 500, size = n)

payment_mode = np.random.choice(
    payment_modes, 
    size = n,
    p = [0.2, 0.05, 0.05, 0.3, 0.1, 0.1, 0.2])

start_date = pd.Timestamp("2024-01-01")
end_date = pd.Timestamp("2026-12-31")

days_range = (end_date - start_date).days
random_days = np.random.randint(0, days_range, size = n)

order_dates = start_date + pd.to_timedelta(random_days, unit = "D")

orders_df = pd.DataFrame({
    "order_id": order_ids,
    "customer_id": customer_ids,
    "product_id": product_ids,
    "amount": amounts,
    "payment_mode": payment_mode,
    "order_date": order_dates
})

print(len(orders_df))

orders_df.to_parquet("orders_04-22_2.parquet", engine = "pyarrow", index = False)