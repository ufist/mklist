import string
import itertools
import subprocess
import os

subprocess.run(["clear"])

if not os.path.exists("wordlists"):
    os.mkdir("wordlists")

subprocess.run(["printf", "\e[33m"])

subprocess.run(["figlet", "-w", "200", "-f", "standard", "UBIQUITY"])

subprocess.run(["printf", "\e[31m"])

subprocess.run(["figlet", "-w", "200", "-f", "small", "Mklist"])

subprocess.run(["printf", "\e[0m"])

print(" [] made by Ubiquity - Wordlist Generator")
print("")

try:
    from tqdm import tqdm
except ImportError:
    print("\033[91mtqdm is not installed. Installing...\033[0m")
    subprocess.run(["pip", "install", "tqdm"])
    from tqdm import tqdm

word = input("\033[94mEnter a word: \033[0m")
output_file_name = os.path.join("wordlists", input("\033[94mEnter the name of the wordlist: \033[0m"))

add_numbers = input("\033[94mDo you want to add numbers to the combinations? (Y/n): \033[0m").lower() == "y"

if add_numbers:
    while True:
        try:
            min_numbers = int(input("\033[94mEnter the minimum number of digits: \033[0m"))
            if min_numbers < 0:
                print("\033[91mPlease enter a non-negative number\033[0m")
            else:
                break
        except ValueError:
            print("\033[91mPlease enter a valid number for the minimum digits\033[0m")

    while True:
        try:
            max_numbers = int(input("\033[94mEnter the maximum number of digits: \033[0m"))
            if max_numbers < min_numbers:
                print("\033[91mMaximum digits should be greater than or equal to minimum digits\033[0m")
            else:
                break
        except ValueError:
            print("\033[91mPlease enter a valid number for the maximum digits\033[0m")

with open(output_file_name, "w") as file_with_numbers, open(output_file_name + "_no_num.txt", "w") as file_without_numbers:
    file_with_numbers.write(word + "\n")
    file_without_numbers.write(word + "\n")

    combinations = itertools.product(*[c.upper() + c.lower() for c in word])
    total_combinations = sum(1 for _ in combinations)

    with tqdm(total=total_combinations, desc="\033[93mGenerating\033[0m") as pbar:
        combinations = itertools.product(*[c.upper() + c.lower() for c in word])
        for combo in combinations:
            word_combination = ''.join(combo)
            file_with_numbers.write(word_combination + "\n")
            file_without_numbers.write(word_combination + "\n")
            pbar.update(1)

            if add_numbers:
                for num_digits in range(min_numbers, max_numbers + 1):
                    for num_combination in itertools.product(string.digits, repeat=num_digits):
                        number_part = ''.join(num_combination)
                        file_with_numbers.write(word_combination + number_part + "\n")
                        pbar.update(1)

print(f"\033[92mWordlist with combinations and numbers has been saved to {output_file_name}\033[0m")
print(f"\033[92mWordlist without numbers has been saved to {output_file_name}_no_num.txt\033[0m")
