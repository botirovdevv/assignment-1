def classify(value):
    if value < 208:
        return "Below range"
    elif 208 <= value <= 212:
        return "In range"
    else:
        return "Above range"

def calculate_average(total, count):
    return total / count

paper_sheets = int(input("Enter the number of paper sheets: "))
total_width = 0
below_range = 0
in_range = 0
above_range = 0

for i in range(paper_sheets):
    width_input = int(input("Enter the paper sheet width: "))
    total_width = total_width + width_input

    category = classify(width_input)
    print(category)

    if category == "Below range":
        below_range += 1
    elif category == "In range":
        in_range += 1
    else:
        above_range += 1

average_width = calculate_average(total_width, paper_sheets)

print(f"Total width: {total_width} mm")
print(f"Average width: {average_width} mm")
print(f"Below range: {below_range}")
print(f"In range: {in_range}")
print(f"Above range: {above_range}")