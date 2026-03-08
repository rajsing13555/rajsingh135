import os
import random
import datetime

projects = [
"Sales Forecasting",
"Customer Churn Prediction",
"Marketing Analytics",
"Financial Risk Analysis",
"Business Profit Forecast",
"Project Management Risk Analysis",
"Customer Segmentation",
"Employee Productivity Analytics"
]

topic = random.choice(projects)

date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")

folder = f"projects/portfolio_project_{date}"

os.makedirs(folder, exist_ok=True)

readme = f"""
# {topic}

Portfolio Data Science Project

Domain:
AI
Machine Learning
Business Analytics
Project Management
"""

with open(f"{folder}/README.md","w") as f:
    f.write(readme)

code = """
import pandas as pd

data = {
'budget':[10000,20000,30000],
'profit':[2000,4000,7000]
}

df = pd.DataFrame(data)

print(df.describe())
"""

with open(f"{folder}/analysis.py","w") as f:
    f.write(code)

print("Portfolio Project Created")
