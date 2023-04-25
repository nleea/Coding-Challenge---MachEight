def pairs_function(list_numbers, target):
    complements = set()
    return [(target - number, number) for number in set(list_numbers) if (target - number) in complements or complements.add(number)]

with open("numbers.txt", "r") as numberText:
    content = numberText.read()

numbers = content.split()
list_numbers = numbers[0].split(",")
results_numbers = list(map(int, map(str.strip, list_numbers)))
print(pairs_function(results_numbers,int(numbers[-1])))