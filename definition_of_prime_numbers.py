# find all prime using only a limited number of numbers
# research paper: The Definition of Prime Numbers Contradicts Its Very Own Existence
# created by Glenn Patrick King Ang 10/20/2021
# email: glenn.patrick.king.ang@outlook.com (preferred)
# email: glenn.p.ang@alumni.uts.edu.au (not affiliated, only an alumni)
# https://github.com/07231985


all_known_numbers = [1, 2, 3, ]
original_set_known_numbers = all_known_numbers.copy()
prime_numbers = []
find_number_until = 100
previous_count_known_numbers = 0
loop = 0

while loop < 5:
    for num_one in all_known_numbers:
        for num_two in all_known_numbers:

            product = num_one * num_two

            if product not in all_known_numbers and product < find_number_until:
                all_known_numbers.append(product)
                loop = 0
    loop += 1

    if previous_count_known_numbers == len(all_known_numbers) and loop > 3:
        break

    previous_count_known_numbers = len(all_known_numbers)

all_known_numbers.sort()
print(f"all_known_numbers = {original_set_known_numbers}")
print(f"find numbers until = {find_number_until}")
print(f"\nStarting the program:")
print(f"all known numbers: {all_known_numbers}")
print(f"total count of all known numbers: {len(all_known_numbers)}")

for prime_candidate in all_known_numbers:
    is_prime = True

    if len(all_known_numbers) > 1:
        if prime_candidate % 2 == 0:
            pass
        else:
            for all_smaller_nums in all_known_numbers[1:all_known_numbers.index(prime_candidate)]:
                if prime_candidate % all_smaller_nums == 0:
                    is_prime = False

            if is_prime:
                if prime_candidate != 1:
                    prime_numbers.append(prime_candidate)
        if prime_candidate == 2:
            prime_numbers.append(2)

print(f"Prime numbers are: {prime_numbers}")
