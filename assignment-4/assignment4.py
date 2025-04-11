import pandas as pd
import numpy as np
#TASK1
# This is for the first data1#
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 30],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}

df1 = pd.DataFrame(data1)
print("\ndata1")
print(df1)

# This is for the first data2#
data2 = {
    'Name': ['Frank', 'Grace', 'Helen', 'Ian', 'Jack'],
    'Age': [28, 33, 35, 29, 40],
    'Salary': [52000, 58000, 72000, 61000, 85000]
}

df2 = pd.DataFrame(data2)
print("\ndata2")
print(df2)

# This is for the first data3#
data3 = {
    'Name': ['Frank', 'Helen', 'Ian', 'Hima', 'Chaka'],
    'Age': [17, 93, 12, 57, 106],
    'Favorite Color': ['blue', 'pink', 'burgundy', 'red', 'turquoise']
}

df3 = pd.DataFrame(data3)
print("\ndata3")
print(df3)

#Perform the following selection operations on df1#
#Select the 'Name' column, and print the result.#
print("\nSelect the 'Name' column, and print the result")
print(df1["Name"])
#Select both 'Name' and 'Salary' columns, and print the result.#
print("\nSelect both 'Name' and 'Salary' columns, and print the result")
print(df1.loc[0:2,["Name","Salary"]])
#Slice the first three rows using integer-based indexing (iloc), and print the result#
print("\nSlice the first three rows using integer-based indexing (iloc), and print the result")
print(df1.iloc[:2])


#TASK2
import pandas as pd
import numpy as np

# This is for the first data1#
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 30],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}

df1 = pd.DataFrame(data1)


# This is for the first data2#
data2 = {
    'Name': ['Frank', 'Grace', 'Helen', 'Ian', 'Jack'],
    'Age': [28, 33, 35, 29, 40],
    'Salary': [52000, 58000, 72000, 61000, 85000]
}

df2 = pd.DataFrame(data2)


# This is for the first data3#
data3 = {
    'Name': ['Frank', 'Helen', 'Ian', 'Hima', 'Chaka'],
    'Age': [17, 93, 12, 57, 106],
    'Favorite Color': ['blue', 'pink', 'burgundy', 'red', 'turquoise']
}

df3 = pd.DataFrame(data3)


#Group df1 by 'Age' and aggregate the 'Salary' column:#


df1_grouped =df1.groupby("Age")["Salary"]


#Calculate the mean, sum, and count of the salary for each age group.#
mean_value = df1_grouped.mean()
sum_value = df1_grouped.sum()
count_value = df1_grouped.count()
print("\nCalculate the mean, sum, and count of the salary for each age group.")
print(mean_value,sum_value,count_value)

#Display the aggregated results.#
df11_grouped =df1.groupby("Age").agg({"Salary":["mean","sum","count"]})
print("\nDisplay the aggregated results.")
print(df11_grouped)

#TASK3
import pandas as pd
import numpy as np

# This is for the first data1#
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 30],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}

df1 = pd.DataFrame(data1)


# This is for the first data2#
data2 = {
    'Name': ['Frank', 'Grace', 'Helen', 'Ian', 'Jack'],
    'Age': [28, 33, 35, 29, 40],
    'Salary': [52000, 58000, 72000, 61000, 85000]
}

df2 = pd.DataFrame(data2)


# This is for the first data3#
data3 = {
    'Name': ['Frank', 'Helen', 'Ian', 'Hima', 'Chaka'],
    'Age': [17, 93, 12, 57, 106],
    'Favorite Color': ['blue', 'pink', 'burgundy', 'red', 'turquoise']
}

df3 = pd.DataFrame(data3)


df_1_3_merged = pd.merge(df1,df3, on="Name", how="outer", suffixes=['_left','_right'])

df_1_3_merged["Salary"] = df_1_3_merged["Salary"].fillna(15000)

df_1_3_merged["Favorite Color"] = df_1_3_merged["Favorite Color"].fillna("yellow")

df_1_3_merged['Age'] = np.where(df_1_3_merged['Age_left'].notna(),df_1_3_merged['Age_left'], df_1_3_merged['Age_right'])


print("\nDisplay the result")
print(df_1_3_merged)

df1_b = df1.set_index("Name")
df3_b = df3.set_index("Name")
joined_df = df1_b.join(df3_b, how='outer', lsuffix='_left', rsuffix='_right')
print("\nthis is joined")
print(joined_df)

#TASK4
import pandas as pd
import numpy as np

# This is for the first data1#
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 30],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}

df1 = pd.DataFrame(data1)

#Filter rows in df1 where 'Age' is greater than 30:
#Display the filtered rows.
filter_df1 = df1[df1["Age"]>30]

print("\nFilter rows in df1 where 'Age' is greater than 30")
print(filter_df1)

#TASK5
#Sort df1 by the 'Salary' column in descending order:
#Display the sorted DataFrame.
sorted_df = df1.sort_values(by='Salary', ascending=False)
print("\ndf1 sorted by 'Salary' in descending order:")
print(sorted_df)

#TASK6
#Rename columns in df1:
#Rename 'Age' to 'Employee Age' and 'Salary' to 'Employee Salary'. Do not use inplace=True, because then you wouldn't be able to do Task 9.
#Display the DataFrame with the renamed columns.

rename_df1 = df1.rename(columns={"Age":"Employee Age","Salary":"Employee Salary"})
print("\nRename columns in df1")
print(rename_df1)

#TASK7
#Apply a transformation to the 'Salary' column in df1:
#Increase the salary by 10% for each employee.
#Display the updated DataFrame.

updated_df = df1.copy()
updated_df["Salary"] = updated_df["Salary"] * 1.10

print("\ndf1 with Salary increased by 10%:")
print(updated_df)

#TASK8
#Concatenate df1 and df2 to add the rows of df2 to the end of df1
#Use ignore_index=True to reset the index.
#Display the result.

concatenated_df = pd.concat([df1, df2], ignore_index=True)
print("Concatenated DataFrame (df1 + df2):")
print(concatenated_df)

#TASK9
import pandas as pd
import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames: 
        print(os.path.join(dirname, filename))
        


result_result =("/kaggle/input/international-football-results-from-1872-to-2017/results.csv") 
football_results = pd.read_csv(result_result)
print("\n")
print(football_results.head())

results_1 =  football_results[[ 'home_team','away_team','home_score','away_score', 'date']]
#print("\ng")
#print(results_1.head())

results_2 = results_1.rename(columns={"home_team": "team","away_team":"opponent","home_score":"points_for","away_score":"points_against"})

print("\n")
print(results_2.head())



results_3 = results_1.rename(columns={"away_team": "team","home_team": "opponent","away_score": "points_for","home_score": "points_against"})

print("\n")
print(results_3.head())


football_results = pd.concat([results_2,results_3], ignore_index=True)
football_results = pd.concat([results_2, results_3], ignore_index=True)
print("\nfootball_results")
print(football_results.head())

points_against = football_results.groupby("team")["points_against"].mean()
print("\n")
print(points_against.sort_values(ascending=False).head(10))

#TASK10
tunisia_games = football_results[football_results['team'] == 'Tunisia']


tunisia_games['date'] = pd.to_datetime(tunisia_games['date'])


tunisia_recent_games = tunisia_games.sort_values(by='date', ascending=False)

print("\n")
print(tunisia_recent_games.head(10))




#This project was done on Kaggle notebook
https://www.kaggle.com/code/ernestmicheal/ctd-assignment-4