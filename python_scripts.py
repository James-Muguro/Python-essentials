#!/usr/bin/env python
# coding: utf-8

# ## This program is for event management

# In[2]:


import random

booking_register = [
    "Amani Kamau", "Atieno Mwangi", "Akinyi Maina", "Kamau Njeri",
    "Mwangi Ochieng", "Maina Odhiambo", "Njeri Omondi", "Ochieng Wanjiku",
    "Odhiambo Wambui", "Omondi Wangechi", "Wanjiku Wanyama", "Wambui Wekesa",
    "Wangechi Amani", "Wanyama Atieno", "Wekesa Akinyi"
]

allowed_attendees = []

def check_attendee(booking_register, allowed_attendees):
    first_name = input("Enter your First Name: ").capitalize()
    last_name = input("Enter your Last Name: ").capitalize()
    full_name = f"{first_name} {last_name}"

    if full_name in booking_register:
        if full_name not in allowed_attendees:
            print("Welcome! You are on the booking register.")
            allowed_attendees.append(full_name)
            assign_seats([full_name])
        else:
            print("You have already been allowed in.")
    else:
        print("Sorry, your name is not on the booking register.")
        register_choice = input("Do you want to register? (yes/no): ").lower()
        if register_choice == "yes":
            booking_register.append(full_name)
            print(f"Thank you, {full_name}! You have been registered. Proceed to check in")
        else:
            print("Thank you. Goodbye.")

def assign_seats(attendees):
    if len(attendees) > 20:
        print("Event capacity reached. No more bookings allowed.")
        return

    print("\nAssigning random seating arrangements and chair numbers:")
    seating_arrangements = random.sample(attendees, len(attendees))

    for index, attendee in enumerate(seating_arrangements, start=1):
        chair_number = random.randint(1, 20)  # Assuming there are 20 chairs
        print(f"Seat {index}: {attendee} (Chair {chair_number})")

# Usage
check_attendee(booking_register, allowed_attendees) 



# ## Password Generator

# In[3]:

import string

def generate_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    password_length = int(input("Enter the desired password length: "))

    if password_length < 5:
        print("Invalid password length. Please enter a number higher than 5.")
        return

    password = generate_password(password_length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()


# ## Leap Year Checker

# In[4]:


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        year = int(input("Enter a year to check if it's a leap year: "))
        if year >= 0:
            if is_leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print("Please enter a valid year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    main()


# ## Quiz Simulator

# In[5]:


def run_quiz():
    print("Welcome to the Python Quiz!")

    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "How many continents are there?", "answer": "7"},
        {"question": "What is 5 + 7?", "answer": "12"}
    ]

    score = 0

    for i, question in enumerate(questions, start=1):
        user_answer = input(f"Question {i}: {question['question']}? ").strip()

        if user_answer.lower() == question['answer'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")

    print(f"Quiz complete! You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz()


# In[ ]:




