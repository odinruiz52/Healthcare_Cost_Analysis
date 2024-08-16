import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('./data/healthcare_cost_cleaned.csv')

# Analysis: Average Total Payments by State
state_avg_payments = df.groupby('Provider State')['Average Total Payments'].mean().sort_index()

# Plot the Average Total Payments by State
plt.figure(figsize=(14, 8))
sns.barplot(x=state_avg_payments.index, y=state_avg_payments.values, palette='coolwarm')
plt.title('Average Total Payments by State', fontsize=18)
plt.xlabel('State', fontsize=14)
plt.ylabel('Average Total Payments', fontsize=14)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
