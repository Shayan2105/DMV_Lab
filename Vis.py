import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("updated_pollution_dataset.csv")

# ------------------ BAR CHART ------------------
plt.figure(figsize=(8,5))
plt.bar(df["Air Quality"], df["Temperature"], color='teal', edgecolor='black')
plt.title("Average Temperature by Air Quality", fontsize=14)
plt.xlabel("Air Quality Category")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# ------------------ STAIR CHART ------------------
plt.figure(figsize=(8,5))
plt.step(range(len(df)), df["PM2.5"], where='mid', color='darkgreen', label="PM2.5 Levels")
plt.title("Step Chart of PM2.5 Levels", fontsize=14)
plt.xlabel("Observation Index")
plt.ylabel("PM2.5 Concentration")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# ------------------ LINE CHART ------------------
plt.figure(figsize=(8,5))
plt.plot(range(len(df)), df["Temperature"], marker='o', linestyle='-', color='crimson', label="Temperature")
plt.title("Temperature Trend", fontsize=14)
plt.xlabel("Observation Index")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# ------------------ PIE CHART ------------------
air_quality_counts = df["Air Quality"].value_counts()

plt.figure(figsize=(6,6))
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
plt.pie(air_quality_counts, labels=air_quality_counts.index,
        autopct='%1.1f%%', colors=colors, startangle=140,
        shadow=True)
plt.title("Air Quality Distribution", fontsize=14)
plt.tight_layout()
plt.show()

# ------------------ HISTOGRAM ------------------
plt.figure(figsize=(8,5))
plt.hist(df["PM10"], bins=10, color='mediumpurple', edgecolor='black')
plt.title("Distribution of PM10 Levels", fontsize=14)
plt.xlabel("PM10 Concentration")
plt.ylabel("Frequency")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# ------------------ OUTLIERS ------------------
df.boxplot()
plt.title("Outliers in Dataset")
plt.show()