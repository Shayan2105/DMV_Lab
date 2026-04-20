import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import re

# -----------------------------
# Create Dataset (Embedded)
# -----------------------------
data = [
["TCS",3.8,"(59.9k Reviews)","Public","55 years old","Mumbai","1 Lakh+"],
["Accenture",4.1,"(38.3k Reviews)","Public","34 years old","Dublin","1 Lakh+"],
["Cognizant",3.9,"(34.9k Reviews)","Private","29 years old","Teaneck","1 Lakh+"],
["ICICI Bank",4,"(28.5k Reviews)","Public","29 years old","Mumbai","1 Lakh+"],
["Wipro",3.9,"(28.4k Reviews)","Public","78 years old","Bangalore","1 Lakh+"],
["HDFC Bank",3.9,"(27.8k Reviews)","Public","29 years old","Mumbai","1 Lakh+"],
["Infosys",3.9,"(26.1k Reviews)","Public","42 years old","Bangalore","1 Lakh+"],
["Capgemini",3.9,"(24.4k Reviews)","Public","56 years old","Paris","1 Lakh+"],
["Tech Mahindra",3.7,"(22.8k Reviews)","Public","37 years old","Pune","1 Lakh+"],
["Genpact",4,"(22.1k Reviews)","Public","26 years old","New York","1 Lakh+"],
["HCLTech",3.8,"(21.7k Reviews)","Public","32 years old","Noida","1 Lakh+"],
["Axis Bank",3.9,"(18.7k Reviews)","Public","30 years old","Mumbai","50k-1 Lakh"],
["Concentrix",4,"(17.6k Reviews)","Public","40 years old","Fremont","10k-50k"],
["IBM",4.1,"(17.4k Reviews)","Public","112 years old","Armonk","50k-1 Lakh"],
["Reliance Jio",4,"(16.9k Reviews)","Public","16 years old","Mumbai","50k-1 Lakh"],
["Amazon",4.2,"(16.7k Reviews)","Public","29 years old","Seattle","1 Lakh+"],
["L&T",4,"(16.1k Reviews)","Public","85 years old","Mumbai","1 Lakh+"],
["HDB Financial",4,"(15.1k Reviews)","Private","16 years old","Ahmedabad","10k-50k"],
["Reliance Retail",4,"(14.3k Reviews)","Private","17 years old","Mumbai","1 Lakh+"],
["Teleperformance",3.6,"(14k Reviews)","Private","45 years old","Paris","10k-50k"],
["Vodafone Idea",4.2,"(14k Reviews)","Public","5 years old","Gandhinagar","10k-50k"],
["Deloitte",4,"(11.8k Reviews)","Private","178 years old","London","50k-1 Lakh"],
["Kotak Bank",3.8,"(11.7k Reviews)","Public","20 years old","Mumbai","10k-50k"],
["BYJU'S",3.2,"(11.4k Reviews)","Private","12 years old","Bangalore","1k-5k"],
["Reliance Industries",4,"(11.1k Reviews)","Public","46 years old","Mumbai","50k-1 Lakh"],
["Bharti Airtel",4,"(10.4k Reviews)","Public","28 years old","Gurgaon","10k-50k"],
["Tata Motors",4.2,"(9.7k Reviews)","Public","78 years old","Pune","50k-1 Lakh"],
["Flipkart",4.1,"(8.3k Reviews)","Public","16 years old","Bangalore","10k-50k"],
["WNS",3.6,"(8.1k Reviews)","Private","27 years old","Mumbai","10k-50k"],
["Ernst & Young",3.7,"(8k Reviews)","Private","21 years old","London","10k-50k"],
["IndusInd Bank",3.8,"(7.7k Reviews)","Public","29 years old","Gurgaon","10k-50k"]
]

df = pd.DataFrame(data, columns=["name","ratings","reviews","ctype","years","hq","employees"])

# -----------------------------
# Data Cleaning
# -----------------------------

# Clean reviews
def clean_reviews(x):
    x = x.lower().replace("reviews","").replace("(","").replace(")","").strip()
    if "k" in x:
        return float(x.replace("k","")) * 1000
    return float(x)

df["reviews_clean"] = df["reviews"].apply(clean_reviews)

# Clean years
df["years_clean"] = df["years"].str.extract(r'(\d+)').astype(int)

# Convert employees
def emp_to_num(x):
    if "1 Lakh+" in x:
        return 100000
    elif "50k-1 Lakh" in x:
        return 75000
    elif "10k-50k" in x:
        return 30000
    elif "1k-5k" in x:
        return 3000
    else:
        return 1000

df["emp_clean"] = df["employees"].apply(emp_to_num)

# -----------------------------
# 1. Pie Chart (Employees)
# -----------------------------
plt.figure(figsize=(8,8))
plt.pie(df["emp_clean"], labels=df["name"], autopct='%1.1f%%')
plt.title("Employees Distribution")
plt.show()

# -----------------------------
# 2. Funnel Chart (Reviews)
# -----------------------------
df_rev = df.sort_values(by="reviews_clean", ascending=False)

fig = px.funnel(df_rev, x="reviews_clean", y="name",
                title="Company Reviews Funnel")
fig.show()

# -----------------------------
# 3. Bar Chart (Ratings)
# -----------------------------
plt.figure(figsize=(12,6))
plt.bar(df["name"], df["ratings"])
plt.xticks(rotation=90)
plt.title("Company Ratings")
plt.xlabel("Company")
plt.ylabel("Ratings")
plt.tight_layout()
plt.show()

# -----------------------------
# 4. Line Chart (Years)
# -----------------------------
df_year = df.sort_values(by="years_clean")

plt.figure(figsize=(12,6))
plt.plot(df_year["name"], df_year["years_clean"], marker='o')
plt.xticks(rotation=90)
plt.title("Company Age (Years)")
plt.xlabel("Company")
plt.ylabel("Years")
plt.tight_layout()
plt.show()
