import dataDescription as dd
import chiSqure as cs
import corrAndReg as cr
loop = True
while loop == True:
    print("""Please choose an option:
    0. Exit
    1. Measures of Central Tendency
        - Mean
        - Weighted Mean
        - Median
        - Mode
        - Midrange
    2. Measures of Variations
        - Range
        - Sample Variance
        - Population Variance
        - Sample Standard Deviation
        - Population Standard Deviation
    3. Measures of Position
        - Z-Score (Mean and Standard Deviation are already given)
        - Z-Score (Calculate from raw data)
        - Percentile Rank of a Value (Score -> Percentile)
        - Value at a Percentile (Percentile -> Score)
    4. Chi Square
        - Test Value (Testing Variance / Standard Deviation)
        - Critical Value
    5. Correlation and Regression
        - Correlartion Coefficient
        - t Test
        - Regression Line Slope
        - y-intercept Regression Line
    """)
    userChoice = int(input("Enter your choice (0-5): "))

    if userChoice == 0:
        print("Exiting the program.")
        loop = False
    elif userChoice == 1:
        result = dd.central_tendency()
        print(f"Result: {result}")
        print("")
        loop = input("Do you want to continue? (y/n): ").lower() == 'y'
    elif userChoice == 2:
        result = dd.variation()
        print(f"Result: {result}")
        print("")
        loop = input("Do you want to continue? (y/n): ").lower() == 'y'
    elif userChoice == 3:
        result = dd.position()
        print(f"Result: {result}")
        print("")
        loop = input("Do you want to continue? (y/n): ").lower() == 'y'
    elif userChoice == 4:
        result = cs.chi_square()
        print(f"Result: {result}")
        print("")
        loop = input("Do you want to continue? (y/n): ").lower() == 'y'
    elif userChoice == 5:
        result = cr.correlation_and_regression()
        print(f"Result: {result}")
        print("")
        loop = input("Do you want to continue? (y/n): ").lower() == 'y'