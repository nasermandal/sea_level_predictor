import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from io import StringIO
import os

csv_file = 'SeaLevelsSince1880.csv'
with open(csv_file, 'r', encoding='utf-8') as f:
    content = f.read().replace('\r\n', '\n')
df = pd.read_csv(StringIO(content), sep='\t')


df.drop(columns=[col for col in ['adjlev_noaa', 'rownames'] if col in df.columns], inplace=True)
df['adjlev'] = pd.to_numeric(df['adjlev'], errors='coerce')
df.dropna(subset=['adjlev'], inplace=True)

X = df[['year']].astype(float)
y = df['adjlev']
_, X_test, _, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

with open("model.pkl", "rb") as f:    
    model = pickle.load(f)
y_pred = model.predict(X_test)
print(" Model Performance:")
print(" - MSE:", mean_squared_error(y_test, y_pred))
print(" - R² Score:", r2_score(y_test, y_pred))

