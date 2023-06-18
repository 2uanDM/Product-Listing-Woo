import pandas as pd

# create a sample dataframe
df = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob'],
    'Age': [25, 30, 35]
})

# get the first row in the dataframe
row_to_append = df.iloc[0]

# append a replicate of the first row
for i in range(10):
    print(len(df))
    df.loc[len(df)] = row_to_append
    print(len(df))

print(df)
