import re

with open("1/input.txt", "r") as f:
    global data 
    data = f.readlines()

total = 0
numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

for line in data:
    nums = re.findall(r'\d', line)
    total += int(nums[0] + nums[-1])

print("Q1 answer", total)

total = 0

for line in data:
    nums = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    if not nums[0].isnumeric():
        nums[0] = numbers[nums[0]]
    if not nums[-1].isnumeric():
        nums[-1] = numbers[nums[-1]]
    total += int(nums[0] + nums[-1])

print("Q2 answer", total)