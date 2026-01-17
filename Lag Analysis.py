import pandas as pd
# Load demographic updates
df_demo = pd.read_csv("demographic.csv")  # replace with your actual filename
# Load biometric updates
df_bio = pd.read_csv("biometric.csv")  # replace with your actual filename


# Convert date_updated to datetime in both datasets
df_demo['date'] = pd.to_datetime(df_demo['date'], dayfirst=True, errors='coerce')
df_bio['date'] = pd.to_datetime(df_bio['date'], dayfirst=True, errors='coerce')


# Count demographic updates per district
demo_counts = df_demo.groupby(['state', 'district']).size().reset_index(name='demographic_updates')

# Count biometric updates per district
bio_counts = df_bio.groupby(['state', 'district']).size().reset_index(name='biometric_updates')

# Merge both counts
update_summary = pd.merge(demo_counts, bio_counts, on=['state', 'district'], how='outer').fillna(0)

# Last demographic update per district
last_demo_update = df_demo.groupby(['state', 'district'])['date'].max().reset_index()
last_demo_update.rename(columns={'date': 'last_demo_update'}, inplace=True)

# Last biometric update per district
last_bio_update = df_bio.groupby(['state', 'district'])['date'].max().reset_index()
last_bio_update.rename(columns={'date': 'last_bio_update'}, inplace=True)

# Merge into one table
lag_table = pd.merge(last_demo_update, last_bio_update, on=['state', 'district'], how='outer')

# Exclude districts with asterisk in their name (Edge cases)
lag_table = lag_table[~lag_table['district'].str.contains(r'\*', regex=True)]

print(lag_table.head())


# Example welfare scheme deadline
deadline = pd.to_datetime("2026-01-01")  

# Compute days between last update and deadline
lag_table['demo_lag_days'] = (deadline - lag_table['last_demo_update']).dt.days
lag_table['bio_lag_days'] = (deadline - lag_table['last_bio_update']).dt.days

#Minimum lage days
lag_table['overall_lag'] = lag_table[['demo_lag_days', 'bio_lag_days']].min(axis=1)

# Flag districts where updates happened after deadline
lag_table['high_risk'] = lag_table['overall_lag'] < 0

# Count of high-risk districts
print("Number of high-risk districts:", lag_table['high_risk'].sum())

# Show high-risk districts
print(lag_table[lag_table['high_risk']])

#PLOTTING
import matplotlib.pyplot as plt

# Bar chart of lags per district
plt.figure(figsize=(12,6))
plt.bar(lag_table['district'], lag_table['overall_lag'])
plt.axhline(0, color='red', linestyle='--', label='Deadline')
plt.xticks(rotation=90)
plt.ylabel('Lag in Days (Deadline - Last Update)')
plt.title('Welfare Exclusion Risk by District in Uttar Pradesh')
plt.legend()
plt.tight_layout()
plt.show()

lag_table.to_csv("up_update_lag_summary.csv", index=False)






