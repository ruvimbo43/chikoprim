# primrose mugombi
#R257042H
#Assignment 3
def classify_number(num):
    """Classify the given number as Positive, Negative, or Zero."""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


# Keep asking until the user enters a valid integer
while True:
    user_input = input("Enter an integer: ")
    try:
        number = int(user_input)
        result = classify_number(number)
        print(f"The number is {result}.")
        break  # exit loop after valid input
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


#Question 2
def calculate_average(*args):
    """
    Return the arithmetic mean of a variable number of numeric arguments.

    Args:
        *args (int | float): One or more numbers.

    Returns:
        float: The average of the provided numbers.

    Raises:
        ValueError: If no numbers are provided.
        TypeError: If any argument is not numeric.

    Examples:
        >>> calculate_average(2, 4, 6)
        4.0
        >>> calculate_average(5)
        5.0
    """
    if not args:
        raise ValueError("Provide at least one number.")
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError("All arguments must be int or float.")
    return sum(args) / len(args)

#Question3

while True:
    raw = input("Enter a number: ")
    try:
        num = float(raw)            # use int(raw) if you want integers only
        print(f"Thanks! You entered: {num}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number (e.g., 42 or 3.14).")

#Questin 4

names = ["Collins", "Ephias", "Walter", "Junior", "Mike"]

with open("names.txt", "w", encoding="utf-8") as f:
    for name in names:
        f.write(name + "\n")

# Read back and print each name
with open("names.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
        
        
#Question 5
        

celsius = [0, 15, 20, 25.5, 78.6, 100]

fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))

print("Celsius   :", celsius)
print("Fahrenheit:", fahrenheit)

  
  
#Question 6
def divide_numbers(numerator, denominator):
    """
    Divide numerator by denominator and return the result.

    Handles:
      - ZeroDivisionError: denominator is 0
      - TypeError: inputs are not numeric
    Returns the quotient on success, otherwise None.
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
        return None
    except TypeError:
        print("Error: both numerator and denominator must be numbers (int or float).")
        return None

#Question 7
    # Define custom exception
class NegativeNumberError(Exception):
    """Custom exception raised when a negative number is encountered."""
    pass


# Function that raises the exception if number is negative
def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    else:
        print(f"{num} is positive.")


# Demonstration using a try block
try:
    number = int(input("Enter a number: "))
    check_positive(number)
except NegativeNumberError as e:
    print("Error:", e)
except ValueError:
    print("Invalid input. Please enter an integer.")

#Question 8
    import random

def random_ints(n=10, low=1, high=100):
    """Return a list of n random integers in [low, high]."""
    return [random.randint(low, high) for _ in range(n)]

def average(numbers):
    """Return the arithmetic mean of a non-empty list of numbers."""
    return sum(numbers) / len(numbers)


nums = random_ints(10, 1, 100)
avg = average(nums)

print("Generated numbers:", nums)
print(f"Average: {avg:.2f}")

#Question 9
import re

def extract_emails(text: str) -> list[str]:
    # Simple, practical email pattern
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(pattern, text)


# II) Validate a date in the format YYYY-MM-DD (with calendar-aware ranges incl. leap years)
def is_valid_yyyy_mm_dd(date_str: str) -> bool:
    # Valid years 1900–2099; adjust if you need a wider range.
    pattern = re.compile(
        r'^(?:'
        r'(?:19|20)\d{2}-(?:'                              # YYYY-
        r'(?:0[13578]|1[02])-(?:0[1-9]|[12]\d|3[01])|'     # 31-day months
        r'(?:0[469]|11)-(?:0[1-9]|[12]\d|30)|'             # 30-day months
        r'02-(?:0[1-9]|1\d|2[0-8])'                        # Feb 1–28
        r')|'
        r'(?:(?:19|20)(?:[02468][048]|[13579][26]))-02-29' # Leap-day
        r')$'
    )
    return bool(pattern.match(date_str))


# III) Replace all occurrences of a word with another word in a string (whole word only)
def replace_word(text: str, old: str, new: str) -> str:
    
    return re.sub(rf'\b{re.escape(old)}\b', new, text)


# IV) Split a string by all non-alphanumeric characters
def split_non_alnum(text: str) -> list[str]:
    parts = re.split(r'[^0-9A-Za-z]+', text)
    return [p for p in parts if p]  # drop empty pieces

#Queastion 10
import socket

HOST = "127.0.0.1"   # localhost
PORT = 65432
MSG  = b"Hello from server!"

def main():
    # TCP/IPv4 socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind((HOST, PORT))
            s.listen(1)
            print(f"Server listening on {HOST}:{PORT} ...")
            conn, addr = s.accept()         # wait for a client
            with conn:
                print("Connected by", addr)
                conn.sendall(MSG)           # send greeting
                print("Message sent, closing.")
        except Exception as e:
            print("Server error:", e)

if __name__ == "__main__":
    main()

    
    
import socket

HOST = "127.0.0.1"
PORT = 65432

def main():
    try:
        
        with socket.create_connection((HOST, PORT), timeout=5) as sock:
            data = sock.recv(1024)
            print("Received:", data.decode(errors="replace"))
    except ConnectionRefusedError:
        print("Client error: connection refused (is the server running?).")
    except socket.timeout:
        print("Client error: connection attempt timed out.")
    except Exception as e:
        print("Client error:", e)

if __name__ == "__main__":
    main()

        
        
#Question 11
    
#API and GET request with requests
#API (Application Programming Interface)
#A set of rules and protocols that allow one software to communicate with another.
#APIs let programs request and exchange data or services.

#Making a GET request with
    
    
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    print("Response JSON:", response.json())
else:
    print("Failed to fetch data.")
    
#Connect to SQLite database in Python

#Steps
#Import sqlite3 - Provides SQLite support
#Connect to DB - sqlite3.connect("mydb.db")
#Create cursor - Used to execute SQL queries
#Execute queries - Create tables, insert, select
#Commit changes - Save changes to the DB
#Close connection - Free resources
        
   
import sqlite3

#connecting to database (creates file thats if it not exists)
conn = sqlite3.connect("chiko .db")
cursor = conn.cursor()

#creating a table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

#inserting data
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
conn.commit()

# reading the data 
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

#closing the connection
conn.close()
     











