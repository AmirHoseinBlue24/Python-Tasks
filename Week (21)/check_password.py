import string
import random
import streamlit as st


def password_genrator(len:int = 8, symbol = False, digit = False):
    if symbol == False and digit == False:
        char = string.ascii_letters
    elif symbol == True and digit == False:
        char = string.ascii_letters + string.punctuation
    elif symbol == True and digit == True:
        char = string.ascii_letters + string.punctuation + string.digits
    else:
        char = string.ascii_letters + string.digits
    
    return ''.join(random.choice(char) for _ in range(len))

def check_password(password:str):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    is_long = len(password) >= 8
   
    if all([has_digit, has_lower, has_symbol, has_upper, is_long]):
        return "You can pass"
    else:
        return f"You can't pass, suggest pass: {password_genrator(8, True, True)} "
        

print(check_password('L!ma67a'))

st.title("Password Generator")
length = st.slider("Length Password:", 8, 20)

symbols = st.checkbox("Has symbols?")
digits = st.checkbox("Has digits?")


st.write(password_genrator(length, symbols, digits))