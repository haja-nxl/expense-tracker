def get_user_info():
    """Collect user's name, age, and favorite color."""
    print("🌟 Welcome to the Personal Greeting Generator! 🌟")
    name = input("What's your name? ").strip().title()
    age = input("How old are you? ").strip()
    color = input("What's your favorite color? ").strip().lower()
    return name, age, color

def generate_greeting(name, age, color):
    """Generate a personalized greeting."""
    return f"\n✨ Hello {name}! You're {age} years young, and {color} is an awesome color! ✨"

def main():
    """Run the greeting generator."""
    name, age, color = get_user_info()
    greeting = generate_greeting(name, age, color)
    print(greeting)

if __name__ == "__main__":
    main()