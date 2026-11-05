import statistics

def weighted_mean():
    data = [float(x) for x in input("Enter the data separated by spaces: ").split()]
    weights = [float(x) for x in input("Enter the weights separated by spaces: ").split()]

    if len(data) != len(weights):
        print("Data and weights must have the same length.")
        weighted_mean()

    weighted_sum = sum(d * w for d, w in zip(data, weights))
    total_weight = sum(weights)

    return weighted_sum / total_weight
def central_tendency():
    print("Central Tendency Options:")
    print("1. Mean")
    print("2. Weighted Mean")
    print("3. Median")
    print("4. Mode")
    print("5. Midrange")
    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        data = [float(x) for x in input("Enter the data separated by spaces: ").split()]
        return statistics.mean(data)
    elif choice == 2:
        return weighted_mean()
    elif choice == 3:
        data = [float(x) for x in input("Enter the data separated by spaces: ").split()]
        return statistics.median(data)
    elif choice == 4:
        data = [float(x) for x in input("Enter the data separated by spaces: ").split()]
        return statistics.multimode(data)
    elif choice == 5:
        data = [float(x) for x in input("Enter the data separated by spaces: ").split()]
        return (max(data) + min(data)) / 2
    else:
        print("Invalid choice. Please try again.")
        central_tendency()

def variation():
    print("Variation Options:")
    print("1. Range")
    print("2. Sample Variance")
    print("3. Population Variance")
    print("4. Sample Standard Deviation")
    print("5. Population Standard Deviation")
    choice = int(input("Enter your choice (1-5): "))

    data = [float(x) for x in input("Enter the data separated by spaces: ").split()]

    if choice == 1:
        return max(data) - min(data)
    elif choice == 2:
        return statistics.variance(data)
    elif choice == 3:
        return statistics.pvariance(data)
    elif choice == 4:
        return statistics.stdev(data)
    elif choice == 5:
        return statistics.pstdev(data)
    else:
        print("Invalid choice. Please try again.")
        variation()

def position():
    print("Position Options:")
    print("1. Z-Score (Mean and Std Dev given)")
    print("2. Z-Score (From raw data)")
    print("3. Percentile Rank of a Value (Score -> Percentile)")
    print("4. Value at a Percentile (Percentile -> Score)")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        x = float(input("Enter the value (X): "))
        mean = float(input("Enter the mean: "))
        stdev = float(input("Enter the standard deviation: "))
        return (x - mean) / stdev

    elif choice == 2:
        data_type = input("Is this a Sample or Population? (s/p): ").strip().lower()
        data = [float(x) for x in input("Enter the data separated by spaces: ").replace(",", " ").split()]
        value = float(input("Enter the value to calculate Z-Score for: "))
        mean = statistics.mean(data)
        stdev = statistics.stdev(data) if data_type == 's' else statistics.pstdev(data)
        return (value - mean) / stdev

    elif choice == 3:
        data = [float(x) for x in input("Enter the data separated by spaces: ").replace(",", " ").split()]
        value = float(input("Enter the score/value to find the percentile rank for: "))
        
        count_below = sum(1 for x in data if x < value)
        n = len(data)
        percentile_rank = ((count_below + 0.5) / n) * 100
        return f"{percentile_rank:.1f}th percentile"

    elif choice == 4:
        data = [float(x) for x in input("Enter the data separated by spaces: ").replace(",", " ").split()]
        percentile = float(input("Enter the percentile (0-100): "))
        return statistics.quantiles(data, n=100)[int(percentile) - 1]

    else:
        print("Invalid choice. Please try again.")
        return position()