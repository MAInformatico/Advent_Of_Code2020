#More info: https://adventofcode.com/2020/day/6
print(sum([len(set(question.replace("\n",""))) for question in open("inputDay6.txt").read().split("\n\n")]))
