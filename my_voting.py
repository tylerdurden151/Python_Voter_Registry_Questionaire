"""
Assignment: Lab 1
Name: Timothy Eckart
Date: 11 May 2024"""""

import sys

print("*********************************************************")
print("Welcome to the Python Voter Registration Application.")

def user_wants_to_continue():
    """
    This function is to ask the user if they would like to continue with the voter registry.
    :return: If the user inputs 'NO' the program will end. Otherwise, if they input 'YES' it will
    proceed to the next function.
    """
    while True:
        response = input("Do you want to continue with Voter Registration? ")
        response = response.upper()
        if response in ["YES", "Y", "YES."]:
            print(response)
            return True
        if response in ["NO", "N", "NO."]:
            print(response)
            sys.exit()
        else:
            print("Invalid input. Please enter again")
            continue



def voter_name():
    """"
    This function calls to ask for the user's first name is.
    :return: the user's value
    """
    input_voter_name = input("What is your first name? ")
    return input_voter_name

def voter_last_name():
    """"
     This function calls to ask for the user's last name is.
     :return: the user's value
    """
    input_voter_last_name = input("What is your last name? ")
    return input_voter_last_name

def voter_age():
    """
     This function calls to ask for the user's voter age and returns the user's age.
     The function will end the program if the user's age is under 18, but will ask the
     user to re-enter if their age is over 120.
     """
    while True:
        input_voter_age = input ("What is your age? ")
        try:
            i = int(input_voter_age)
            if i < 18 :
                print("Unfortunately, you are not old enough to vote. Have a nice day.")
                sys.exit()
            elif i > 120 :
                print("Error input try again")
                continue
            else:
                return i
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue


def us_citizen():
    """
    This calls to ask for the user's citizenship
    If the user is not a US citizen, it will end the program. Otherwise, if  'Yes'
    it will proceed to the next function.
    """
    while True:
        citizen_reply = input("Yes Are you a U.S. Citizen? ")
        if citizen_reply.upper() in ["Yes", "Y", "Yes."]:
            return citizen_reply
        if citizen_reply.upper() in ["No", "N", "No."]:
            print(citizen_reply)
            print("Unfortunately, you have to be a US Citizen to vote. Have a nice day.")
            sys.exit()
        else:
            print("Invalid input. Please enter again")
        continue

def state():
    """
    This calls to ask for the user's state address
    :return: the users inputed state address
    """
    while True:
        input_state = input("What state do you live? ")
        if input_state.upper() in ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",\
                             "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",\
                             "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",\
                             "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",\
                             "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]:
            return input_state
        print("Please enter again\n" +"enter state by the following example: 'IL'.")

def zip_code():
    """
    This calls to ask for the user's zip code
    :return: the users inputed zip code
    """

    while True:
        input_zip_code = input("What is your zip code? ")
        if len(input_zip_code) != 5 and len(input_zip_code) != 9:
            print("Error: Input must be five digits or 9 digit zip code.")
        else:
            return input_zip_code
def main_continue_vote():
    """
    This the main function for the program
    :return: will call all the functions declared and then provide a statement at the function
    of the function with all the declared values.
    """
    continue_vote = True
    while continue_vote:
        if not user_wants_to_continue():
            continue_vote = False
            break
        first_name = voter_name()
        print(first_name)
        if not user_wants_to_continue():
            continue_vote = False
            break
        last_name = voter_last_name()
        print(last_name)
        if not user_wants_to_continue():
            continue_vote = False
            break
        age = voter_age()
        print(age)
        if not user_wants_to_continue():
            continue_vote = False
            break
        citizen = us_citizen()
        print(citizen)
        if not user_wants_to_continue():
            continue_vote = False
            break
        user_state = state()
        print(user_state)
        if not user_wants_to_continue():
            continue_vote = False
            break
        user_zip_code = zip_code()
        print(user_zip_code)
        print("Thanks for registering to vote. Here is the information we received: ")
        print(f"Name (first last): {first_name} {last_name}")
        print(f"Age: {age}")
        print(f"U.S. Citizen: {citizen}")
        print(f"State: {user_state}")
        print(f"Zipcode:  {user_zip_code}")
        print("Thanks for trying the Voter Registration Application.")
        print("Your voter registration card should be shipped within 3 weeks.")
        print("*********************************************************")
    return continue_vote

main_continue_vote()
