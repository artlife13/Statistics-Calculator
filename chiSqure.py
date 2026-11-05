import scipy.stats as stats

import scipy.stats as stats
import statistics

def chi_square():
    print("Chi Square Options:")
    print("1. Test Value (Testing Variance / Standard Deviation)")
    print("2. Critical Value")
    choice = int(input("Enter your choice (1-2): "))

    if choice == 1:
        data_input_type = input("Do you have raw data? (y/n): ").strip().lower()

        if data_input_type == 'y':
            raw_data = [float(x) for x in input("Enter the data separated by spaces: ").replace(",", " ").split()]
            s2 = statistics.variance(raw_data)
            df = len(raw_data) - 1
        else:
            is_stdev = input("Is your sample value a Standard Deviation (s) or Variance (s^2)? (s/v): ").strip().lower()
            val = float(input("Enter the sample value: "))
            s2 = val**2 if is_stdev == 's' else val
            n = int(input("Enter sample size (n): "))
            df = n - 1


        is_pop_stdev = input("Is the claimed value a Standard Deviation (sigma) or Variance (sigma^2)? (s/v): ").strip().lower()
        claimed_val = float(input("Enter the claimed value: "))
        sigma2 = claimed_val**2 if is_pop_stdev == 's' else claimed_val


        test_value = df * (s2 / sigma2)
        return round(test_value, 2)

    elif choice == 2:
        tail = input("Enter the tail type (left/right/two-tailed): ").lower()
        n = int(input("Enter the sample size (n): "))
        df = n - 1                                      
        alpha = float(input("Enter the significance level (e.g., 0.05): "))
        if tail == "left":
            return stats.chi2.ppf(alpha, df)
        elif tail == "right":
            return stats.chi2.ppf(1 - alpha, df)
        elif tail == "two-tailed":
            return [x for x in stats.chi2.ppf([alpha/2, 1-alpha/2], df)]