from pprint import pprint

with open("./day_11.in") as fin:
    raw_data = fin.read().strip()
    monkey_parts = raw_data.split("\n\n")

monkeys = []


def expr(operation, x):
    left, op, right = operation

    assert left == "old"  # Assumption

    if op == "+":
        return x + int(right)
    else:
        if right == "old":
            return x * x
        else:
            return x * int(right)


class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0

    def __str__(self):
        return f"{self.items}, {self.operation}, {self.test}"


for i, monkey_part in enumerate(monkey_parts):
    lines = monkey_part.split("\n")
    items = list(map(int, lines[1][2:].split(" ", 2)[2].split(", ")))
    operation = lines[2][2:].split(" ", 3)[3].split(" ")

    # Parse the test
    mod = int(lines[3][2:].split(" ")[-1])
    if_true = int(lines[4][4:].split(" ")[-1])
    if_false = int(lines[5][4:].split(" ")[-1])

    # Package it together
    monkeys.append(Monkey(
        items,
        operation,
        [mod, if_true, if_false]
    ))


# Do the rounds
N = len(monkeys)

for round in range(20):
    for i in range(N):
        monkey = monkeys[i]
        for item in monkey.items:
            # item is an int, representing worry level
            item = expr(monkey.operation, item)
            item //= 3

            mod, if_true, if_false = monkey.test
            if item % mod == 0:
                monkeys[if_true].items.append(item)
            else:
                monkeys[if_false].items.append(item)

            monkey.inspections += 1

        # Empty the list of items
        monkey.items = []


# Are we done
amounts = [m.inspections for m in monkeys]
sorted_amts = sorted(amounts)
print(sorted_amts[-1] * sorted_amts[-2])
