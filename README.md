# UIDAI-Data-Hackathon-26
Code files, datasets and result files from the project

#TITLE
Welfare Exclusion Early-Warning System using Aadhaar Update Data (Uttar Pradesh)

# PROBLEM STATEMENT
Many government welfare schemes depend on Aadhaar authentication. Beneficiaries are often excluded when demographic or biometric details are outdated at the time of benefit disbursal. Despite the availability of Aadhaar update data, there is no simple analytical mechanism to identify regions where delayed updates may cause welfare exclusion.

This project analyzes Aadhaar demographic and biometric update timelines to identify districts at higher risk of exclusion due to late updates.

# DATASET DESCRIPTION
Aadhaar Demographic Update Dataset (aggregated)
Aadhaar Biometric Update Dataset (aggregated)
Taken from the hackathon site

# ANALYSIS OBJECTIVE
The objective of this project is to:
Identify districts where Aadhaar updates occur after a defined scheme deadline
Compute update lag to flag high-risk regions
Provide an early-warning signal for potential welfare exclusion

# KEY METRICS
Lag Metric: lag_days = update_date – scheme_deadline
Negative lag → update after deadline (high risk)
Positive lag → update before deadline (lower risk)

# RESULTS AND INSIGHTS
Several districts showed negative lag values, indicating updates occurred after the assumed benefit cycle
Certain districts exhibited extreme lag values, suggesting irregular update patterns
These regions may require targeted Aadhaar update drives or deadline extensions

# TOOLS USED
Python
Pandas
Matplotlib
VS Code

# LIMITATIONS 
Scheme deadline is assumed due to lack of official records
The dataset provided does not contain data over a continuous date
