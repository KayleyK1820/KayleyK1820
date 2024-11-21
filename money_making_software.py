import random
import time

def generate_income():
    return random.randint(5, 100)  # Generate a random income between $5 and $100

def main_simulation():
    total_income = 0
    duration = 10  # Run the simulation for 10 seconds

    print("Starting the income simulation...")
    start_time = time.time()

    while time.time() - start_time < duration:
        income = generate_income()
        total_income += income
        print(f"Generated Income: ${income}")
        time.sleep(1)  # Wait for 1 second before generating the next income

    print(f"\nTotal Income Generated in {duration} seconds: ${total_income}")

if __name__ == "__main__":
    main_simulation()
