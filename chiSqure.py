import scipy.stats as stats

def chi_square():
    print("Chi Square Options:")
    print("1. Test Value")
    print("2. Critical Value")
    choice = int(input("Enter your choice (1-2): "))

    if choice == 1:
        N = float(input("Enter the real variance: "))
        E = float(input("Enter the claimed variance: "))
        df = (int(input("Enter the numbers of categories: ")) - 1)
        alpha = float(input("Enter the significance level (e.g., 0.05): "))
        chi_square_statistic = df * (N / E)
        return chi_square_statistic
    elif choice == 2:
        tail = input("Enter the tail type (left/right/two-tailed): ").lower()
        df = (int(input("Enter the numbers of categories: ")) - 1)
        alpha = float(input("Enter the significance level (e.g., 0.05): "))
        if tail == "left":
            critical_value = stats.chi2.ppf(alpha, df)
        elif tail == "right":
            critical_value = stats.chi2.ppf(1 - alpha, df)
        elif tail == "two-tailed":
            critical_value = stats.chi2.ppf([alpha/2, 1-alpha/2], df)
        return critical_value
    else:
        print("Invalid choice. Please try again.")
        chi_square()