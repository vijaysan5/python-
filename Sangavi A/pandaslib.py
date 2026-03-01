import pandas as pd
import numpy as np

# Creating a Series
""" print("Series:")
data = [10, 20, 30, 40, 50]
a = pd.Series(data)
print(a)
s = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])
print(s)
print("Data type of Series:", s.dtype)
print("Index of Series:", s.index)
print("Values of Series:", s.values)
print("Shape of Series:", s.shape)
print("Number of dimensions of Series:", s.ndim)
print("Size of Series:", s.size)
print("Is Series empty?:", s.empty) """

# Creating a DataFrame
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data_dict)
print("\nDataFrame:")
print(df)

# Reading & Writing Files
""" df.to_excel('example.xlsx',index=False)
df.to_csv('example.csv', index=False)
print("file saved") """
df = pd.read_csv('example.csv')
print("\nRead CSV:")
print(df)

# DataFrame Information
""" print("\nInfo:")
print(df.info())
print("\nDescription:")
print(df.describe())
print("\nColumns:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
print("Index:", df.index)
print("Values:")
print(df.values)
print("Shape:", df.shape)
print("Number of dimensions:", df.ndim)
print("Size:", df.size)
print("Is empty:", df.empty) """

# Selecting Data
""" print("\nSelecting Column:")
print(df['Name'])
print("\nSelecting Row:")
print(df.loc[1])
print("\nSelecting with Condition:")
print(df[df['Age'] > 30])
print("\nSelecting by Index:")
print(df.iloc[1]) """

# Adding a Column
df['Bonus'] = df['Salary'] * 0.10
print("\nUpdated DataFrame:")
print(df) 

# Deleting a Column
df.drop('Bonus', axis=1, inplace=True)
print("\nAfter Dropping Column:")
print(df)

df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]})
print("Original DataFrame:")
print(df)

df = df.rename(columns={'A': 'aa'})
print("Modified DataFrame:")
print(df)

















# Handling Missing Values
""" df.loc[2, 'Age'] = np.nan
df.fillna(np.mean(df['Age']))
print("\nAfter Handling NaN:")
print(df)
print("\nDrop Missing Values:")
print(df.dropna())

# Sorting Data
df_sorted = df.sort_values(by='Salary', ascending=False)
print("\nSorted DataFrame:")
print(df_sorted)

# Duplicates
print("\nAfter Dropping Duplicates:")
print(df.drop_duplicates())

# Applying Functions
def add_hike(salary):
    return salary * 1.05

df['Hiked Salary'] = df['Salary'].apply(add_hike)
print("\nAfter Applying Function:")
print(df)

# Renaming Columns
df.rename(columns={'Age': 'Years'}, inplace=True)
print("\nRenamed Columns:")
print(df)

# Reset and Set Index
df_reset = df.reset_index()
print("\nReset Index:")
print(df_reset)

df.set_index('Name', inplace=True)
print("\nSet Index:")
print(df) """

""" 
# Merging DataFrames 
df2 = pd.DataFrame({'Name': ['Alice', 'Charlie'], 'Department': ['HR', 'IT']})
merged_df = pd.merge(df, df2, on='Name', how='left')
print("\nMerged DataFrame:")
print(merged_df)

# Grouping Data
grouped = df.groupby('Age').sum()
print("\nGrouped Data:")
print(grouped)

# Pivot Table
pivot_df = df.pivot_table(values='Salary', index='Age', aggfunc=np.mean)
print("\nPivot Table:")
print(pivot_df)
 """
