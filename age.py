from datetime import datetime

def calculate_age(birth_date):
    """
    Calculate age based on the given birth_date and the current date.

    :param birth_date: A string in the format 'YYYY-MM-DD'
    :return: Age in years as an integer
    """
    try:
        birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'."

birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")
age = calculate_age(birth_date_input)
print(f"Your age is: {age}")