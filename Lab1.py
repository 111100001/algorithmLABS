#program to find the greatest common divisors of two positive integers m and n
import time


def standard_algorithm():
    m = 0
    n = 0
    while m < 1 or n < 1:
        m = int(input("Enter a positive integer: "))
        n = int(input("Enter another positive integer: "))
    start_time = time.time()  # Record the start time

    m_array = []  # Array to store the m dvisors
    n_array = []  # Array to store the n dvisors

    # Find the divisors of m
    for i in range(1, m + 1):
        if m % i == 0:
            m_array.append(i)

    # Find the divisors of n
    for i in range(1, n + 1):
        if n % i == 0:
            n_array.append(i)

    # Find the common divisors of m and n
    common_divisors = []
    for i in m_array:
        if i in n_array:
            common_divisors.append(i)

    # Find the greatest common divisor
    gcd = max(common_divisors)
    print("The greatest common divisor of", m, "and", n, "is", gcd)
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
    return gcd


def euclidean_algorithm():

    m = int(input("Enter a positive integer: "))
    n = int(input("Enter another positive integer: "))
    start_time = time.time()  # Record the start time

    mm= m
    nn= n
    r= 0 #remainder of m divided by n
    if n == 0:
        print("The greatest common divisor of", m, "and", n, "in Euclid's algorithm is", m)
        return m
    else:
        while n != 0:
            r = m % n
            m = n
            n = r
        print("The greatest common divisor of", mm, "and", nn, "Euclid's algorithm is", m)
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"Elapsed time: {elapsed_time:.6f} seconds")
        return m



def main():
    #prompt the user if they want to use the euclidean algorithm or the standard algorithm
    print("Would you like to use the Euclidean algorithm or the standard algorithm?")
    print("1. Euclidean algorithm")
    print("2. Standard algorithm")
    choice = int(input("Enter your choice: "))


    if choice == 1:
        euclidean_algorithm()
    elif choice == 2:
        standard_algorithm()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main()





if __name__ == "__main__":
    main()