import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load datasets ---
listings = pd.read_csv("listings.csv")
reviews = pd.read_csv("reviews.csv")
neighbourhoods = pd.read_csv("neighbourhoods.csv")


# --- Data Cleaning ---
listings = listings[pd.to_numeric(listings['price'], errors='coerce').notnull()]
listings['price'] = listings['price'].replace('[\$,]', '', regex=True).astype(float)
reviews['date'] = pd.to_datetime(reviews['date'], errors='coerce')

# --- 1. Top 10 Most Expensive Neighbourhoods ---
if 'neighbourhood' in listings.columns:
    top_neigh = listings.groupby('neighbourhood')['price'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10,6))
    top_neigh.plot(kind='bar', color='teal', edgecolor='black')
    plt.title("Top 10 Most Expensive Neighbourhoods", fontsize=14, fontweight='bold')
    plt.ylabel("Average Price ($)", fontsize=12)
    plt.xlabel("Neighbourhood", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# --- 2. Trend of Reviews Over Time ---
monthly_reviews = reviews.groupby(reviews['date'].dt.to_period('M')).size()
plt.figure(figsize=(12,6))
monthly_reviews.plot(kind='line', marker='o', color='blue')
plt.title("Trend of Reviews Over Time", fontsize=14, fontweight='bold')
plt.ylabel("Number of Reviews", fontsize=12)
plt.xlabel("Month", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --- 3. Reviews per Listing (Top 20) ---
if 'number_of_reviews' in listings.columns and 'name' in listings.columns:
    top_reviewed = listings[['name','number_of_reviews']].sort_values(by='number_of_reviews', ascending=False).head(20)
    plt.figure(figsize=(12,6))
    sns.barplot(data=top_reviewed, x='number_of_reviews', y='name', palette='viridis')
    plt.title("Top 20 Listings by Number of Reviews", fontsize=14, fontweight='bold')
    plt.xlabel("Number of Reviews", fontsize=12)
    plt.ylabel("Listing Name", fontsize=12)
    plt.tight_layout()
    plt.show()

# --- 4. Price Distribution ---
plt.figure(figsize=(10,6))
filtered_prices = listings[listings['price'] < 1000]['price']
sns.histplot(filtered_prices, bins=40, kde=True, color='purple', edgecolor='black')
plt.title("Distribution of Listing Prices (Under $1000)", fontsize=14, fontweight='bold')
plt.xlabel("Price ($)", fontsize=12)
plt.ylabel("Number of Listings", fontsize=12)
plt.tight_layout()
plt.show()









Extended analysis complete with review insights, price, and quality comparisons!")
