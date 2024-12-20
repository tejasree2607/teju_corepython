def check_password(password):
    
    if(len(password)<10 or len(password)>=15):
        return("The password should contain min 10 characters and max 15")
    elif not any(char.islower() for char in password):
        return " Moderate: atleast one lower case letter"
    elif not any(char.isupper() for char in password):
        return " Moderate: atleast one upper case letter"
    elif not any(char.isdigit() for char in password):
        return " Moderate: atleast one digit"
    elif not any(char in "!@#$%^&*()" for char in password):
        return " Moderate: atleast any one special character is needed"
    elif(password[-1]== '.' or password[-1]== '@'):
        return "Should not end with . or @"
    elif " " in password:
        return "Should not contain spaces"
    else:
        return "Strong: good password"
password=input("Enter password:")
print(check_password(password))