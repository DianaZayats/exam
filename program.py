import re

def calculate_energy_cost(start_reading, end_reading, rate_per_kwh):
    if not (isinstance(start_reading, int) and isinstance(end_reading, int)):
        raise ValueError("Meter readings must be integers.")
    if start_reading < 0 or end_reading < 0:
        raise ValueError("Meter readings cannot be negative.")
    if end_reading < start_reading:
        raise ValueError("End reading cannot be less than start reading.")

    consumed_kwh = end_reading - start_reading
    return consumed_kwh * rate_per_kwh

def get_user_input():
    try:
        start = int(input("Enter start reading: "))
        end = int(input("Enter end reading: "))
        rate = float(input("Enter rate per kWh: "))
        if start < 0 or end < 0:
            print("Error: Meter readings cannot be negative.")
            return None
        return start, end, rate
    except ValueError as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    user_input = get_user_input()
    if user_input:
        start, end, rate = user_input
        try:
            cost = calculate_energy_cost(start, end, rate)
            print(f"Total cost: ${cost:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
