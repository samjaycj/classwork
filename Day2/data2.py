# Dictionary data type
score_dic = {
    "Allice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88,
    "Frank": 70
}

print("......... Initial Student scores ..........")

for name, score in score_dic.items():
    print(f"{name}: {score}")
print("\n")

# Add new student to the dictionary
new_name = 'Grace'
new_score = 90
score_dic[new_name]=new_score
print(f"......... Student scores with added new student: {new_name} and score: {new_score} ..........")
for name, score in score_dic.items():
    print(f"{name}: {score}")
print("\n")

if score_dic:
    highest = 0
    highest_name = ''
    score_list = []
    for name, score in score_dic.items():
        score_list.append(score)
        if score>highest:
            highest = score
            highest_name = name
    print(f"Highest scorer name is {highest_name} with a score of {highest}")
    high_score=max(score_list)
    print(f"High score is {high_score}")
else:
    print("Cannot find the highest score!")
    