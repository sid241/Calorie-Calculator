def main():
    """Main function to execute the calorie calculator."""
    print("\nWelcome to the Calorie Intake Calculator!")
    gender = get_gender()
    weight = get_positive_number("Enter your weight in kg: ")
    height = get_positive_number("Enter your height in cm: ")
    age = get_positive_integer("Enter your age: ")
    bmr = calculate_bmr(gender, weight, height, age)
    activity_level = get_activity_level()
    total_calories = calculate_daily_calories(bmr, activity_level)

    print(f"\nTo maintain your current weight, you need approximately {total_calories:.2f} calories per day.")


def get_gender():
    """Prompt user for gender and validate input."""
    while True:
        gender = input("Do you identify as male or female? ").strip().lower()
        if gender in ["male", "m", "female", "f"]:
            return "male" if gender in ["male", "m"] else "female"
        print("Invalid input. Please enter 'male' or 'female'.")


def get_positive_number(prompt):
    """Prompt user for a positive float value."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Value must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_positive_integer(prompt):
    """Prompt user for a positive integer value."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Value must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def calculate_bmr(gender, weight, height, age):
    """Calculate Basal Metabolic Rate (BMR) based on gender."""
    if gender == "male":
        return (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        return (10 * weight) + (6.25 * height) - (5 * age) - 161


def get_activity_level():
    """Prompt user for activity level and validate input."""
    activity_levels = {
        "sedentary": 1.25,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
    }

    while True:
        activity = input("\nWhat is your activity level?\n"
                         "Sedentary: Little to no exercise\n"
                         "Light: Light exercise 1-3 days/week\n"
                         "Moderate: Moderate exercise 3-5 days/week\n"
                         "Active: Hard exercise daily\n"
                         "Enter: 'sedentary', 'light', 'moderate', or 'active': ").strip().lower()

        if activity in activity_levels:
            return activity_levels[activity]
        print("Invalid input. Please enter one of the listed activity levels.")


def calculate_daily_calories(bmr, activity_multiplier):
    """Calculate total daily calorie requirement."""
    return bmr * activity_multiplier


if __name__ == "__main__":
    main()
