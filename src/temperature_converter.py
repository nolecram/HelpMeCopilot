#!/usr/bin/env python3
"""
Temperature Converter Application
Convert between Celsius and Fahrenheit temperatures
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius"""
    return (fahrenheit - 32) * 5/9

def main():
    """Main function to run the temperature converter application"""
    print("Temperature Converter")
    print("====================")
    
    # Initialize counter for conversion requests
    request_count = 0
    
    while True:
        print("\nSelect an option:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. View Request Count")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
                request_count += 1
            
            elif choice == 2:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")
                request_count += 1
            
            elif choice == 3:
                print(f"Number of temperature conversions performed: {request_count}")
            
            elif choice == 4:
                print(f"Total conversions performed: {request_count}")
                print("Thank you for using the Temperature Converter!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
