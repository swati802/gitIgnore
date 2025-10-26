def print_primes_in_range(lower, upper):
    """
    Prints all prime numbers within a given range (inclusive).

    Args:
        lower (int): The lower bound of the range.
        upper (int): The upper bound of the range.
    """
    print(f"Prime numbers between {lower} and {upper} are:")
    for num in range(lower, upper + 1):
        if num > 1:  # Prime numbers are greater than 1
            is_prime = True
            # Check for divisibility from 2 up to the square root of num
            # We only need to check up to the square root for efficiency
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    is_prime = False
                    break  # Not a prime, no need to check further
            if is_prime:
                print(num)

# Example usage:
start_range = 1
end_range = 100
print_primes_in_range(start_range, end_range)