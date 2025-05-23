import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import os

csv_file = 'SeaLevelsSince1880.csv'

# (tab-separated file)
df = pd.read_csv(csv_file, sep='\t')

# i'm dropping columns, since not needed
for col in ['adjlev_noaa', 'rownames']:
    if col in df.columns:
        df = df.drop(col, axis=1)

#df['adjlev'] = pd.to_numeric(df['adjlev'], errors='coerce')
df = df.dropna(subset=['adjlev'])

# definition of the independent X  and depedent variable y 
X = df[['year']]
y = df['adjlev']

# Lets split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# here I'm fitting the  linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# here, I'm saving the trained model model.pkl
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to model.pkl.")
