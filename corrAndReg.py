import scipy.stats as stats
import statistics

def correlation_and_regression():
    print("Correlation and Regression Options:")
    print("1. Correlartion Coefficient")
    print("2. Correlation Coefficient(corr determination given)")
    print("3. Correlation Determination")
    print("4. t Test")
    print("5. Equation of Regression Line")
    print("6. Regression Line Slope")
    print("7. y-intercept Regression Line")
    print("8. Prediction Value")
    choice = int(input("Enter your choice (1-8): "))

    if choice == 1:
        data1 = [float(x) for x in input("Enter the x values separated by spaces: ").split()]
        data2 = [float(x) for x in input("Enter the y values separated by spaces: ").split()]
        return statistics.correlation(data1, data2)
    elif choice == 2:
        r_squared = float(input("Enter the correlation determination (R^2) value: "))
        r = r_squared ** 0.5
        return r
    elif choice == 3:
        data1 = [float(x) for x in input("Enter the x values separated by spaces: ").split()]
        data2 = [float(x) for x in input("Enter the y values separated by spaces: ").split()]
        r = statistics.correlation(data1, data2)
        r_squared = r ** 2
        return r_squared
    elif choice == 4:
        data1 = [float(x) for x in input("Enter the x values separated by spaces: ").split()]
        data2 = [float(x) for x in input("Enter the y values separated by spaces: ").split()]
        r = statistics.correlation(data1, data2)
        n = len(data1)
        t_statistic = r * ((n - 2) ** 0.5) / ((1 - r ** 2) ** 0.5)
        return t_statistic
    elif choice == 5:
        data1 = [float(x) for x in input("Enter the x values separated by spaces: ").split()]
        data2 = [float(x) for x in input("Enter the y values separated by spaces: ").split()]
        slope, intercept, r_value, p_value, std_err = stats.linregress(data1, data2)
        return f"y = {slope:.2f}x + {intercept:.2f}"
    elif choice == 6:
        data1 = [float(x) for x in input("Enter the x values separated by spaces: ").split()]
        data2 = [float(x) for x in input("Enter the y values separated by spaces: ").split()]
        slope, intercept, r_value, p_value, std_err = stats.linregress(data1, data2)
        return slope
    elif choice == 7:
        data1 = [float(x) for x in input("Enter the x values separated by spaces: ").split()]
        data2 = [float(x) for x in input("Enter the y values separated by spaces: ").split()]
        slope, intercept, r_value, p_value, std_err = stats.linregress(data1, data2)
        return intercept
    elif choice == 8:
        data1 = [float(x) for x in input("Enter the x values separated by spaces: ").split()]
        data2 = [float(x) for x in input("Enter the y values separated by spaces: ").split()]
        slope, intercept, r_value, p_value, std_err = stats.linregress(data1, data2)
        x_value = float(input("Enter the value of x to predict y: "))
        predicted_y = slope * x_value + intercept
        return predicted_y
    else:
        print("Invalid choice. Please try again.")
        correlation_and_regression()
    
