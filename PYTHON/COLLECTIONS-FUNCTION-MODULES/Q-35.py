# Write a Python program to check multiple keys exists in a dictionary

# we can check existense of multiple key using [in] and [all] function



# Sample dictionary
Dictionary = {'jay': 'Full Stack Developer', 'tirth': 'C_D_P', 'devanshu': 'Full Stack Developer'}

# Keys to check for existence
checking = {'niyati': 'Backend Developer', 'Umesh': 'IT Career Path'}

# Check if all keys exist using a loop
existence = all(key in Dictionary for key in checking)

if existence:
    print(f"All Keys {checking} Exist In the Dictionary.")
else:
    missing = [key for key in checking if key not in Dictionary]
    print(f"The Following Keys Are Missing In The Dictionary: {missing}")
