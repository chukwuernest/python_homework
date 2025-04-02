# TASK1
# import traceback

# def write_to_diary():
#     try:
#         with open("diary.txt", "a") as file:
#             prompt = "What happened today? "
#             while True:
#                 entry = input(prompt)
#                 if entry.lower() == "done for now":
#                     file.write(entry + "\n")
#                     break
#                 file.write(entry + "\n")
#                 prompt = "What else? "
#     except Exception as e:
#         trace_back = traceback.extract_tb(e.__traceback__)
#         stack_trace = [
#             f'File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}'
#             for trace in trace_back
#         ]
#         print(f"Exception type: {type(e).__name__}")
#         message = str(e)
#         if message:
#             print(f"Exception message: {message}")
#         print(f"Stack trace: {stack_trace}")

# if __name__ == "__main__":
#     write_to_diary()

# TASK2
# import csv
# import traceback

# def read_employees():
#     employees_dict = {}
#     rows_list = []
#     try:
#         with open("../csv/employees.csv", newline='', encoding='utf-8') as csvfile:
#             reader = csv.reader(csvfile)
#             for index, row in enumerate(reader):
#                 if index == 0:
#                     employees_dict["fields"] = row  # Store headers
#                 else:
#                     rows_list.append(row)  # Store data rows
#         employees_dict["rows"] = rows_list
#         return employees_dict
#     except Exception as e:
#         trace_back = traceback.extract_tb(e.__traceback__)
#         stack_trace = [
#             f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
#             for trace in trace_back
#         ]
#         print(f"Exception type: {type(e).__name__}")
#         message = str(e)
#         if message:
#             print(f"Exception message: {message}")
#         print(f"Stack trace: {stack_trace}")
#         exit(1)

# employees = read_employees()
# print(employees) 
# TASK3
# def column_index(column_name):
#  def employees():
    
#     return employees["fields"].index(column_name)


# employee_id_column = column_index("employee_id")


# print(f"Index of 'employee_id': {employee_id_column}")

# TASK4
# def first_name(row_number):
#     try:
#         index = column_index("first_name")  
#         return employees["rows"][row_number][index] 
#     except IndexError:
#         print(f"Error: Row {row_number} is out of range.")
#         return None
#     except Exception as e:
#         print(f"An exception occurred: {e}")
#         return None

# TASK5
# def employee_find(employee_id):
#     def employee_match(row):
#         return int(row[employee_id_column]) == employee_id  # Check if employee ID matches
    
#     matches = list(filter(employee_match, employees["rows"]))
    
#     employee_id_column = 0  
    
    
    # TASK6
#     def employee_find(employee_id):
#     def employee_match(row):
#         return int(row[employee_id_column]) == employee_id
    
#     matches = list(filter(employee_match, employees["rows"]))
#     return matches

# def employee_find_2(employee_id):
#     matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
#     return matches

# TASK7
# employee_id_column = 0  
# last_name_column = 1  

# def employee_find(employee_id):
#     def employee_match(row):
#         return int(row[employee_id_column]) == employee_id
    
#     matches = list(filter(employee_match, employees["rows"]))
#     return matches

# def employee_find_2(employee_id):
#     matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
#     return matches

# def sort_by_last_name():
#     employees["rows"].sort(key=lambda row: row[last_name_column])
#     return employees["rows"]

# TASK 8

# last_name_column = 1  

# def employee_find(employee_id):
#     def employee_match(row):
#         return int(row[employee_id_column]) == employee_id
    
#     matches = list(filter(employee_match, employees["rows"]))
#     return matches

# def employee_find_2(employee_id):
#     matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
#     return matches

# def sort_by_last_name():
#     employees["rows"].sort(key=lambda row: row[last_name_column])
#     return employees["rows"]

# def employee_dict(row):
#     return {key: value for key, value in zip(employees["fields"], row) if key != employees["fields"][employee_id_column]}


# print(employee_dict(employees["rows"][0]))


# TASK 9
# employee_id_column = 0  
# last_name_column = 1  

# def employee_find(employee_id):
#     def employee_match(row):
#         return int(row[employee_id_column]) == employee_id
    
#     matches = list(filter(employee_match, employees["rows"]))
#     return matches

# def employee_find_2(employee_id):
#     matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
#     return matches

# def sort_by_last_name():
#     employees["rows"].sort(key=lambda row: row[last_name_column])
#     return employees["rows"]

# def employee_dict(row):
#     return {key: value for key, value in zip(employees["fields"], row) if key != employees["fields"][employee_id_column]}

# def all_employees_dict():
#     return {int(row[employee_id_column]): employee_dict(row) for row in employees["rows"]}

# print(all_employees_dict())

# TASK 10
# import os
# employee_id_column = 0 
# last_name_column = 1  

# def employee_find(employee_id):
#     def employee_match(row):
#         return int(row[employee_id_column]) == employee_id
    
#     matches = list(filter(employee_match, employees["rows"]))
#     return matches

# def employee_find_2(employee_id):
#     matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
#     return matches

# def sort_by_last_name():
#     employees["rows"].sort(key=lambda row: row[last_name_column])
#     return employees["rows"]

# def employee_dict(row):
#     return {key: value for key, value in zip(employees["fields"], row) if key != employees["fields"][employee_id_column]}

# def all_employees_dict():
#     return {int(row[employee_id_column]): employee_dict(row) for row in employees["rows"]}

# def get_this_value():
#     return os.getenv("THISVALUE")


# print(get_this_value())

# TASK11
# import os
# import custom_module

# employee_id_column = 0  
# last_name_column = 1  

# def employee_find(employee_id):
#     def employee_match(row):
#         return int(row[employee_id_column]) == employee_id
    
#     matches = list(filter(employee_match, employees["rows"]))
#     return matches

# def employee_find_2(employee_id):
#     matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
#     return matches

# def sort_by_last_name():
#     employees["rows"].sort(key=lambda row: row[last_name_column])
#     return employees["rows"]

# def employee_dict(row):
#     return {key: value for key, value in zip(employees["fields"], row) if key != employees["fields"][employee_id_column]}

# def all_employees_dict():
#     return {int(row[employee_id_column]): employee_dict(row) for row in employees["rows"]}

# def get_this_value():
#     return os.getenv("THISVALUE")

# def set_that_secret(new_secret):
#     custom_module.set_secret(new_secret)

# set_that_secret("my_new_secret")
# print(custom_module.secret)

# TASK12
# import os
# import custom_module
# import csv

# employee_id_column = 0  
# last_name_column = 1  

# def employee_find(employee_id):
#     def employee_match(row):
#         return int(row[employee_id_column]) == employee_id
    
#     matches = list(filter(employee_match, employees["rows"]))
#     return matches

# def employee_find_2(employee_id):
#     matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
#     return matches

# def sort_by_last_name():
#     employees["rows"].sort(key=lambda row: row[last_name_column])
#     return employees["rows"]

# def employee_dict(row):
#     return {key: value for key, value in zip(employees["fields"], row) if key != employees["fields"][employee_id_column]}

# def all_employees_dict():
#     return {int(row[employee_id_column]): employee_dict(row) for row in employees["rows"]}

# def get_this_value():
#     return os.getenv("THISVALUE")

# def set_that_secret(new_secret):
#     custom_module.set_secret(new_secret)

# def read_csv(file_path):
#     with open(file_path, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         fields = next(reader) 
#         rows = [tuple(row) for row in reader] 
#     return {"fields": fields, "rows": rows}

# def read_minutes():
#     minutes1 = read_csv("../csv/minutes1.csv")
#     minutes2 = read_csv("../csv/minutes2.csv")
#     return minutes1, minutes2


# minutes1, minutes2 = read_minutes()
# print(minutes1)
# print(minutes2)

# TASK13
# import os
# import custom_module
# import csv

# employee_id_column = 0  
# last_name_column = 1  

# def employee_find(employee_id):
#     def employee_match(row):
#         return int(row[employee_id_column]) == employee_id
    
#     matches = list(filter(employee_match, employees["rows"]))
#     return matches

# def employee_find_2(employee_id):
#     matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
#     return matches

# def sort_by_last_name():
#     employees["rows"].sort(key=lambda row: row[last_name_column])
#     return employees["rows"]

# def employee_dict(row):
#     return {key: value for key, value in zip(employees["fields"], row) if key != employees["fields"][employee_id_column]}

# def all_employees_dict():
#     return {int(row[employee_id_column]): employee_dict(row) for row in employees["rows"]}

# def get_this_value():
#     return os.getenv("THISVALUE")

# def set_that_secret(new_secret):
#     custom_module.set_secret(new_secret)

# def read_csv(file_path):
#     with open(file_path, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         fields = next(reader)  
#         rows = [tuple(row) for row in reader]  
#     return {"fields": fields, "rows": rows}

# def read_minutes():
#     minutes1 = read_csv("../csv/minutes1.csv")
#     minutes2 = read_csv("../csv/minutes2.csv")
#     return minutes1, minutes2

# def create_minutes_set():
#     set1 = set(minutes1["rows"])
#     set2 = set(minutes2["rows"])
#     return set1.union(set2)


# minutes1, minutes2 = read_minutes()
# minutes_set = create_minutes_set()
# print(minutes_set)

# TASK14
# import os
# import custom_module
# import csv
# from datetime import datetime

# employee_id_column = 0 
# last_name_column = 1  

# def employee_find(employee_id):
#     def employee_match(row):
#         return int(row[employee_id_column]) == employee_id
    
#     matches = list(filter(employee_match, employees["rows"]))
#     return matches

# def employee_find_2(employee_id):
#     matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
#     return matches

# def sort_by_last_name():
#     employees["rows"].sort(key=lambda row: row[last_name_column])
#     return employees["rows"]

# def employee_dict(row):
#     return {key: value for key, value in zip(employees["fields"], row) if key != employees["fields"][employee_id_column]}

# def all_employees_dict():
#     return {int(row[employee_id_column]): employee_dict(row) for row in employees["rows"]}

# def get_this_value():
#     return os.getenv("THISVALUE")

# def set_that_secret(new_secret):
#     custom_module.set_secret(new_secret)

# def read_csv(file_path):
#     with open(file_path, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         fields = next(reader)  
#         rows = [tuple(row) for row in reader]  
#     return {"fields": fields, "rows": rows}

# def read_minutes():
#     minutes1 = read_csv("../csv/minutes1.csv")
#     minutes2 = read_csv("../csv/minutes2.csv")
#     return minutes1, minutes2

# def create_minutes_set():
#     set1 = set(minutes1["rows"])
#     set2 = set(minutes2["rows"])
#     return set1.union(set2)

# def create_minutes_list():
#     return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), list(minutes_set)))


# minutes1, minutes2 = read_minutes()
# minutes_set = create_minutes_set()
# minutes_list = create_minutes_list()
# print(minutes_list)

# TASK15


# import os
# import custom_module
# import csv
# from datetime import datetime

# employee_id_column = 0 
# last_name_column = 1 

# def employee_find(employee_id):
#     def employee_match(row):
#         return int(row[employee_id_column]) == employee_id
    
#     matches = list(filter(employee_match, employees["rows"]))
#     return matches

# def employee_find_2(employee_id):
#     matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
#     return matches

# def sort_by_last_name():
#     employees["rows"].sort(key=lambda row: row[last_name_column])
#     return employees["rows"]

# def employee_dict(row):
#     return {key: value for key, value in zip(employees["fields"], row) if key != employees["fields"][employee_id_column]}

# def all_employees_dict():
#     return {int(row[employee_id_column]): employee_dict(row) for row in employees["rows"]}

# def get_this_value():
#     return os.getenv("THISVALUE")

# def set_that_secret(new_secret):
#     custom_module.set_secret(new_secret)

# def read_csv(file_path):
#     with open(file_path, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         fields = next(reader)  
#         rows = [tuple(row) for row in reader] 
#     return {"fields": fields, "rows": rows}

# def read_minutes():
#     minutes1 = read_csv("../csv/minutes1.csv")
#     minutes2 = read_csv("../csv/minutes2.csv")
#     return minutes1, minutes2

# def create_minutes_set():
#     set1 = set(minutes1["rows"])
#     set2 = set(minutes2["rows"])
#     return set1.union(set2)

# def create_minutes_list():
#     return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), list(minutes_set)))

# def write_sorted_list():
#     sorted_minutes_list = sorted(minutes_list, key=lambda x: x[1])
#     formatted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_minutes_list))
#     with open("./minutes.csv", mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(minutes1["fields"])
#         writer.writerows(formatted_list)
#     return formatted_list


# minutes1, minutes2 = read_minutes()
# minutes_set = create_minutes_set()
# minutes_list = create_minutes_list()
# write_sorted_list()
