import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import os
from io import StringIO

# Path to the dataset
csv_file = 'SeaLevelsSince1880.csv'

# Ensure the file exists
if not os.path.isfile(csv_file):
    raise FileNotFoundError(f"CSV file not found: {csv_file}")

# Read file and normalize line endings (handles \r\n vs \n)
with open(csv_file, 'r', encoding='utf-8') as f:
    content = f.read().replace('\r\n', '\n')

# Load into DataFrame as tab-separated
df = pd.read_csv(StringIO(content), sep='\t')

# Drop optional columns if they exist
df.drop(columns=[col for col in ['adjlev_noaa', 'rownames'] if col in df.columns], inplace=True)

# Ensure 'adjlev' is numeric and drop NaNs
df['adjlev'] = pd.to_numeric(df['adjlev'], errors='coerce')
df.dropna(subset=['adjlev'], inplace=True)

# Prepare feature and label
X = df[['year']].astype(float)
y = df['adjlev']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to model.pkl.")

