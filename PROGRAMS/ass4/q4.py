'''
Write a Python program that predicts a person’s Indian Zodiac sign
(Rashi) based on the month of birth (month name) 
Indian Zodiac Order (Simplified Month-Based Model): The Indian
Zodiac cycle starts in March with Mesha
when a person is born in 15th march it should return Mesha
when a person is born in 14th april it should return Vrishabha
when a person is born in 20th may it should return Mithuna
when a person is born in 10th june it should return Karka
when a person is born in 5th july it should return Simha
when a person is born in 25th august it should return Kanya
when a person is born in 30th september it should return Tula
when a person is born in 18th october it should return Vrischika
when a person is born in 22nd november it should return Dhanu
when a person is born in 15th december it should return Makara
when a person is born in 10th january it should return Kumbha
when a person is born in 28th february it should return Meena
'''

def predict_zodiac_sign(day, month):
    """
    This function predicts a person's Indian Zodiac sign (Rashi) based on the day and month of birth.
    
    Parameters:
    day (int): The day of birth.
    month (str): The month of birth.
    
    Returns:
    str: The predicted Indian Zodiac sign.
    """
    month = month.lower()  # Convert month to lowercase for case-insensitive comparison
    
    if (month == 'march' and day >= 15) or (month == 'april' and day <= 14):
        return "Mesha"
    elif (month == 'april' and day >= 15) or (month == 'may' and day <= 19):
        return "Vrishabha"
    elif (month == 'may' and day >= 20) or (month == 'june' and day <= 9):
        return "Mithuna"
    elif (month == 'june' and day >= 10) or (month == 'july' and day <= 4):
        return "Karka"
    elif (month == 'july' and day >= 5) or (month == 'august' and day <= 24):
        return "Simha"
    elif (month == 'august' and day >= 25) or (month == 'september' and day <= 29):
        return "Kanya"
    elif (month == 'september' and day >= 30) or (month == 'october' and day <= 17):
        return "Tula"
    elif (month == 'october' and day >= 18) or (month == 'november' and day <= 21):
        return "Vrischika"
    elif (month == 'november' and day >= 22) or (month == 'december' and day <= 14):
        return "Dhanu"
    elif (month == 'december' and day >= 15) or (month == 'january' and day <= 9):
        return "Makara"
    elif (month == 'january' and day >= 10) or (month == 'february' and day <= 27):
        return "Kumbha"
    elif (month == 'february' and day >= 28) or (month == 'march' and day <= 14):
        return "Meena"
    else:
        return "Invalid date or month. Please enter a valid day and month."
# Example usage
if __name__ == "__main__":
    user_day = input("Enter the day of birth (1-31): ")  # Read day input from the user
    user_month = input("Enter the month of birth (e.g., January): ")  # Read month input from the user
    
    if not user_day.isdigit() or int(user_day) < 1 or int(user_day) > 31:
        print("Invalid input. Please enter a valid day between 1 and 31.")
    else:
        day = int(user_day)  # Convert the input to an integer
        result = predict_zodiac_sign(day, user_month)  # Call the function to predict the zodiac sign
        print(f"The predicted Indian Zodiac sign is: {result}")  # Print the result