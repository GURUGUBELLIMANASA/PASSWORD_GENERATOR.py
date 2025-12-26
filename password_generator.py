import random
import string

def generate_password(length):
    if length < 4:
        print(" Password length should be at least 4")
        return ""

    letters = string.ascii_letters      
    digits = string.digits             
    symbols = string.punctuation      

    all_chars = letters + digits + symbols

   
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_chars, k=length - 3)
    random.shuffle(password)

    return "".join(password)

def main():
    print("====== PASSWORD GENERATOR ======")
    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        if password:
            print(f" Generated Password: {password}")
    except ValueError:
        print(" Please enter a valid number.")

main()
