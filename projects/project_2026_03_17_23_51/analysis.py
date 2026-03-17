
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

print("\nStatistics:")
print(df.describe())
