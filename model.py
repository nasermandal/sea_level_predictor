import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import os
from io import StringIO

# dataset loading
csv_file = 'SeaLevelsSince1880.csv'

# making sure the file is loaded
if not os.path.isfile(csv_file):
    raise FileNotFoundError(f"CSV file not found: {csv_file}")

# normalize line endings (handles \r\n vs \n)
with open(csv_file, 'r', encoding='utf-8') as f:
    content = f.read().replace('\r\n', '\n')

# loading into df as tab-separated
df = pd.read_csv(StringIO(content), sep='\t')

# dropping not required columns, since irelevant
df.drop(columns=[col for col in ['adjlev_noaa', 'rownames'] if col in df.columns], inplace=True)

# checking 'adjlev' is numeric and drop NaNs
df['adjlev'] = pd.to_numeric(df['adjlev'], errors='coerce')
df.dropna(subset=['adjlev'], inplace=True)

# prep feature and label
X = df[['year']].astype(float)
y = df['adjlev']

# split the data train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# fitting  the model
model = LinearRegression()
model.fit(X_train, y_train)

# saving the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to model.pkl.")

