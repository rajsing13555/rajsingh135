import os
import random
import datetime

topics = [
"Sales Forecasting",
"Customer Churn Prediction",
"Financial Risk Analysis",
"Marketing Analytics",
"Business Profit Forecast",
"Project Management Risk Analysis",
"Customer Segmentation",
"Employee Productivity Analytics"
]

topic = random.choice(topics)

date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")

folder = f"projects/project_{date}"

os.makedirs(folder, exist_ok=True)

readme = f"""
# {topic}

Auto Generated Data Science Project

Domain:
AI
Machine Learning
Data Analysis
Business Analytics
Project Management

Tools Used:
Python
Pandas
"""

with open(f"{folder}/README.md","w") as f:
    f.write(readme)

code = """
import pandas as pd

# Sample Dataset
data = {
    'budget':[10000,20000,30000,40000],
    'team_size':[3,5,7,10],
    'profit':[2000,4000,7000,10000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\\nStatistics:")
print(df.describe())
"""

with open(f"{folder}/analysis.py","w") as f:
    f.write(code)

print("Project Created Successfully")
