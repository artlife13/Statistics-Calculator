import scipy.stats as stats
import statistics

def correlation_and_regression():
    print("Correlation and Regression Options:")
    print("1. Correlation Coefficient")
    print("2. t Test for Correlation Coefficient")
    print("3. Regression Line Slope")
    print("4. y-intercept of Regression Line")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        data1 = [float(x) for x in input("Enter the first set of data separated by spaces: ").split()]
        data2 = [float(x) for x in input("Enter the second set of data separated by spaces: ").split()]
        return statistics.correlation(data1, data2)
    elif choice == 2:
        data1 = [float(x) for x in input("Enter the first set of data separated by spaces: ").split()]
        data2 = [float(x) for x in input("Enter the second set of data separated by spaces: ").split()]
        r = statistics.correlation(data1, data2)
        n = len(data1)
        t_statistic = r * ((n - 2) ** 0.5) / ((1 - r ** 2) ** 0.5)
        return t_statistic
    elif choice == 3:
        data1 = [float(x) for x in input("Enter the independent variable data separated by spaces: ").split()]
        data2 = [float(x) for x in input("Enter the dependent variable data separated by spaces: ").split()]
        slope, intercept, r_value, p_value, std_err = stats.linregress(data1, data2)
        return slope
    elif choice == 4:
        data1 = [float(x) for x in input("Enter the independent variable data separated by spaces: ").split()]
        data2 = [float(x) for x in input("Enter the dependent variable data separated by spaces: ").split()]
        slope, intercept, r_value, p_value, std_err = stats.linregress(data1, data2)
        return intercept
    else:
        print("Invalid choice. Please try again.")
        correlation_and_regression()
    