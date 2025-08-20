# analysis.py
# Simple analysis and plotting for Inventory Turnover Ratio - 2024 Quarterly Data
import pandas as pd
import matplotlib.pyplot as plt

quarters = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
values = [1.77, 6.2, 9.05, 12.17]
industry_target = 8.0

df = pd.DataFrame({'quarter': quarters, 'inventory_turnover': values})
average = df['inventory_turnover'].mean()

print('Quarterly inventory turnover:')
print(df.to_string(index=False))
print(f'Computed average: {average:.2f}')

# Plot
fig, ax = plt.subplots(figsize=(6,6))
ax.plot(df['quarter'], df['inventory_turnover'], marker='o', linewidth=2)
ax.axhline(industry_target, linestyle='--', linewidth=1.2)
ax.set_title('Inventory Turnover Ratio — 2024 Quarterly Trend')
ax.set_ylabel('Inventory Turnover Ratio')
for i, v in enumerate(values):
    ax.annotate(f"{v:.2f}", (quarters[i], values[i]), textcoords='offset points', xytext=(0,6), ha='center')
ax.legend(['Turnover', f'Industry Target = {industry_target}'])
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('inventory_turnover_trend.png', dpi=150)
print('Saved inventory_turnover_trend.png')