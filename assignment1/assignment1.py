# Write your code here.
# TASK1
def hello():
    return "Hello!"
print(hello())  
   # TASK2 
def name():
    return "micheal"
print(hello() + ", " + name())  
# TASK3
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
print(calc(10, 20, "add"))        
print(calc(10, 15, "subtract"))   
print(calc(10, 50))               
print(calc(10, 0, "divide"))     
print(calc('hello', 1, "multiply")) 

# TASK4
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return f"Invalid data type: {data_type}"
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
print(data_type_conversion("123", "int"))  
print(data_type_conversion("3.14", "float")) 
print(data_type_conversion(100, "str"))     
print(data_type_conversion("nonsense", "float"))  

print(data_type_conversion(42, "boolean"))  

# TASK5
def grade(*args):
    try:
        if not args:
            return "Invalid data was provided."
        
        avg = sum(args) / len(args)
        
        match avg:
            case _ if avg >= 90:
                return "A"
            case _ if avg >= 80:
                return "B"
            case _ if avg >= 70:
                return "C"
            case _ if avg >= 60:
                return "D"
            case _:
                return "F"
    except (TypeError, ValueError):
        return "Invalid data was provided."

print(grade(85, 90, 78))  
print(grade(100, 95, 92)) 
print(grade(50, 55, 60))  
print(grade("hello", 90))
print(grade())            

# TASK6
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

print(repeat("hello", 3))  
print(repeat("abc", 2))   
print(repeat("!", 5))    
print(repeat("xyz", 0))    

# TASK7
def student_scores(mode, **kwargs):
    if not kwargs:
        return "No student scores provided."
    
    if mode == "best":
        return max(kwargs, key=kwargs.get)
    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        return "Invalid mode."

print(student_scores("best", Alice=85, Bob=92, Charlie=78))  
print(student_scores("mean", Alice=85, Bob=92, Charlie=78))  
print(student_scores("best"))  
print(student_scores("average", Alice=85, Bob=92))  

# TASK8
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()

    if not words:
        return ""

    titleized_words = [
        word.capitalize() if i == 0 or i == len(words) - 1 or word.lower() not in little_words else word.lower()
        for i, word in enumerate(words)
    ]

    return " ".join(titleized_words)

print(titleize("the lord of the rings"))  
print(titleize("a tale of two cities"))  
print(titleize("in the middle of nowhere"))  
print(titleize("on an island"))  
print(titleize(""))  

# TASK9
def hangman(secret, guess):
    return "".join(letter if letter in guess else "_" for letter in secret)


print(hangman("alphabet", "ab"))  
print(hangman("mississippi", "sip"))  
print(hangman("python", "xyz"))  

# TASK10
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    pig_latin_words = []

    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(word + "ay")
        elif word.startswith("qu"):
            pig_latin_words.append(word[2:] + "quay")
        else:
            consonant_cluster = ""
            for i, letter in enumerate(word):
                if letter in vowels or (letter == "u" and i > 0 and word[i - 1] == "q"):
                    break
                consonant_cluster += letter
            pig_latin_words.append(word[len(consonant_cluster):] + consonant_cluster + "ay")

    return " ".join(pig_latin_words)


print(pig_latin("hello world"))  
print(pig_latin("apple banana orange"))  
print(pig_latin("quiet question"))  
print(pig_latin("string translation example")) 