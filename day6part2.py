with open("inputDay6.txt") as f:
        questions = f.read().split("\n\n")
result = 0
for question in questions:
    answers = question.split()
    common = set.intersection(*map(set, answers))
    result += len(common)
print(result)
