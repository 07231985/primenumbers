# The link between prime and even numbers
# research paper: Existence of Prime Numbers
# created by Glenn Patrick King Ang 10/21/2021
# email: glenn.patrick.king.ang@outlook.com (preferred)
# email: glenn.p.ang@alumni.uts.edu.au (not affiliated, only an alumni)
# https://github.com/07231985


all_even_numbers = []
found_even_numbers = []
find_numbers_until = 2000
starting_prime_numbers = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                          59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, ]

find_odd_composite_nums = []
found_numbers = starting_prime_numbers.copy()
missing_even_numbers = []
loop = 0

# designed for 2 as a prime number
for even_nums in range(6, find_numbers_until, 2):
    all_even_numbers.append(even_nums)

while loop < 3:
    for current_num in starting_prime_numbers:
        if current_num % 2 == 1:
            for next_num in starting_prime_numbers:
                if next_num % 2 == 1:
                    sum_of_odd_nums = current_num + next_num
                    if sum_of_odd_nums not in found_numbers and sum_of_odd_nums < find_numbers_until:
                        loop = 0
                        found_numbers.append(sum_of_odd_nums)

    loop += 1
    if loop > 3:
        break

# identify all the even integers and put it inside found_even_integer

for all_even in all_even_numbers:
    if all_even in found_numbers:
        found_even_numbers.append(all_even)

# find the missing even integers if any

for all_even in all_even_numbers:
    if all_even not in found_numbers:
        last_even_found = found_even_numbers[-1]
        index_last_even_found = all_even_numbers.index(last_even_found)

        if all_even < all_even_numbers[index_last_even_found]:
            missing_even_numbers.append(all_even)

# Multiply all prime numbers by itself and  with each other:
# ignore product if it is greater than the last even number + 1
for prime_num in starting_prime_numbers:
    for prime_num_two in starting_prime_numbers:
        product_itself = prime_num * prime_num_two
        if len(found_even_numbers) > 1:
            if product_itself < found_even_numbers[-1]:
                if product_itself not in find_odd_composite_nums:
                    find_odd_composite_nums.append(product_itself)

# Multiply all odd numbers by itself and  with each other:
# ignore product if it is greater than the last even number + 1
all_odd_nums = starting_prime_numbers.copy()

for odd_composite in find_odd_composite_nums:
    if odd_composite not in all_odd_nums:
        all_odd_nums.append(odd_composite)
for odd_nums in all_odd_nums:
    for odd_nums_two in all_odd_nums:
        product_all_odds = odd_nums * odd_nums_two
        if len(found_even_numbers) > 1:
            if product_all_odds < found_even_numbers[-1]:
                if product_all_odds not in find_odd_composite_nums:
                    find_odd_composite_nums.append(product_all_odds)

found_numbers.sort()
find_odd_composite_nums.sort()
found_even_numbers.sort()

print(f"Starting number is: {starting_prime_numbers}")
print(f"Find numbers until: {find_numbers_until}")
print(f"Found numbers are: {found_numbers}")
print(f"\nFound even numbers: {found_even_numbers}")
print(f"\nMissing even numbers: {missing_even_numbers}")
print(f"Found odd composite numbers: {find_odd_composite_nums}")