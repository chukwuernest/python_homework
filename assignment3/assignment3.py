# TASK1A
import pandas as pd
 
data={
"Name": ['Alice', 'Bob', 'Charlie'],
"Age": [25, 30, 35],
"City": ['New York', 'Los Angeles', 'Chicago']}

task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

# TASK1B
import pandas as pd
data = {
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [25, 30, 35],
    "City": ['New York', 'Los Angeles', 'Chicago']
}


task1_data_frame = pd.DataFrame(data)


print("Original DataFrame:")
print(task1_data_frame)


task1_with_salary = task1_data_frame.copy()


task1_with_salary["Salary"] = [70000, 80000, 90000]


print("\nDataFrame with Salary column:")
print(task1_with_salary)

# TASK1C
import pandas as pd


data = {
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [25, 30, 35],
    "City": ['New York', 'Los Angeles', 'Chicago']
}


task1_data_frame = pd.DataFrame(data)


print("Original DataFrame:")
print(task1_data_frame)


task1_with_salary = task1_data_frame.copy()


task1_with_salary["Salary"] = [70000, 80000, 90000]


print("\nDataFrame with Salary column:")
print(task1_with_salary)


task1_older = task1_with_salary.copy()


task1_older["Age"] += 1


print("\nDataFrame with Age incremented:")
print(task1_older)

# TASK1D
import pandas as pd


data = {
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [25, 30, 35],
    "City": ['New York', 'Los Angeles', 'Chicago']
}


task1_data_frame = pd.DataFrame(data)


print("Original DataFrame:")
print(task1_data_frame)


task1_with_salary = task1_data_frame.copy()


task1_with_salary["Salary"] = [70000, 80000, 90000]


print("\nDataFrame with Salary column:")
print(task1_with_salary)


task1_older = task1_with_salary.copy()


task1_older["Age"] += 1


print("\nDataFrame with Age incremented:")
print(task1_older)


task1_older.to_csv("employees.csv", index=False)


print("\nDataFrame saved to employees.csv")

# TASK2
import pandas as pd
import json


task2_employees = pd.read_csv("employees.csv")


print("\nTask 2 - DataFrame loaded from CSV:")
print(task2_employees)


additional_employees = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]


json_filename = "additional_employees.json"
with open(json_filename, "w") as json_file:
    json.dump(additional_employees, json_file, indent=4)

print(f"\nJSON file '{json_filename}' created successfully!")


json_employees = pd.read_json(json_filename)


print("\nTask 2 - DataFrame loaded from JSON:")
print(json_employees)


more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)


print("\nTask 2 - Combined DataFrame:")
print(more_employees)


more_employees.to_csv("updated_employees.csv", index=False)
print("\nCombined DataFrame saved to 'updated_employees.csv'")

# TASK3
# import pandas as pd
# import json


task2_employees = pd.read_csv("employees.csv")


json_filename = "additional_employees.json"
json_employees = pd.read_json(json_filename)


more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)


first_three = more_employees.head(3)
print("\nFirst three rows of more_employees:")
print(first_three)


last_two = more_employees.tail(2)
print("\nLast two rows of more_employees:")
print(last_two)


employee_shape = more_employees.shape
print("\nShape of more_employees DataFrame:")
print(employee_shape)


print("\nSummary of more_employees DataFrame:")
more_employees.info() 

# TASK4
# import pandas as pd
import numpy as np

dirty_data = pd.read_csv("dirty_data.csv")


print("\nOriginal Dirty Data:")
print(dirty_data)


clean_data = dirty_data.copy()


clean_data.drop_duplicates(inplace=True)

print("\nData After Removing Duplicates:")
print(clean_data)


clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")

print("\nData After Converting Age to Numeric:")
print(clean_data)


clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], np.nan)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")

print("\nData After Converting Salary to Numeric:")
print(clean_data)


clean_data["Age"].fillna(clean_data["Age"].mean(), inplace=True)
clean_data["Salary"].fillna(clean_data["Salary"].median(), inplace=True)

print("\nData After Filling Missing Values:")
print(clean_data)


clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")

print("\nData After Converting Hire Date to Datetime:")
print(clean_data)


clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()

print("\nFinal Cleaned Data:")
print(clean_data)