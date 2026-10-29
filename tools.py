from datetime import datetime

# Function to get the current time
def get_current_time():
    """
    Returns the current time in a human-readable format.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to get random number of dice rolls
def roll_dice():
    """
    Simulates rolling a six-sided dice and returns the result.
    """
    import random
    return random.randint(1, 6)

# Function to generate secure password.
def generate_secure_password(length=12):
    """
    Generates a secure password of specified length.
    Default length is 12 characters.
    """
    import string
    import secrets
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for i in range(length)) 

