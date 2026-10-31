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
        weighted_mean()
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
    print("1. Sample Z-Score")
    print("2. Population Z-Score")
    print("3. Percentile")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        data = [float(x) for x in input("Enter the data separated by spaces: ").split()]
        value = float(input("Enter the value to calculate Z-Score for: "))
        mean = statistics.mean(data)
        stdev = statistics.stdev(data)
        return (value - mean) / stdev
    elif choice == 2:
        data = [float(x) for x in input("Enter the data separated by spaces: ").split()]
        value = float(input("Enter the value to calculate Z-Score for: "))
        mean = statistics.mean(data)
        stdev = statistics.pstdev(data)
        return (value - mean) / stdev
    elif choice == 3:
        data = [float(x) for x in input("Enter the data separated by spaces: ").split()]
        percentile = float(input("Enter the percentile (0-100): "))
        return statistics.quantiles(data, n=100)[int(percentile)-1]
    else:
        print("Invalid choice. Please try again.")
        position()