# using input function to get user inputs for a username and password and promnpting back the password length to the user
username = input("Enter your username: ")
password = input("Enter your password: ")
password_length = len(password)
password_mask = '*' * password_length
print(
    f"Hello {username}, your password {password_mask} is {password_length} letters long."
)
