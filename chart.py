#!/usr/bin/env python3
"""
Paperclip Stats - Simple chart example demonstrating matplotlib
"""

import matplotlib.pyplot as plt

# Sample data - paperclip inventory over time
weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6']
paperclips = [150, 230, 180, 290, 310, 450]
orders = [20, 35, 25, 40, 45, 60]

# Create the chart
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(weeks, paperclips, marker='o', linewidth=2, label='Total Paperclips', color='#2563eb')
ax.plot(weeks, orders, marker='s', linewidth=2, label='New Orders', color='#16a34a')

ax.set_xlabel('Week')
ax.set_ylabel('Count')
ax.set_title('Paperclip Inventory Tracker')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('chart.png', dpi=150)
print("Chart saved to chart.png")
