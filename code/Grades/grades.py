
class Grade():
    def __init__(self, string, value=0):
        self.string = string
        self.value = value
        for i in string:
            if i == "A":
                self.value = 140
            elif i == "B":
                self.value = 120
            elif i == "C":
                self.value = 100
            elif i == "D":
                self.value = 80
            elif i == "E":
                self.value = 60
            elif i == "X":
                self.value = 40
            elif i == "F":
                self.value = 20
            elif i == "+":
                self.value += 1
            elif i == "-":
                self.value -= 1
            
    def value(self):
        return self.value

def main():
    input_size = int(input())
    iterator = 0
    global grade_dict
    grade_dict = {}
    while iterator < input_size:
        name, grade = input().split()
        grade_value = Grade(grade)
        if len(grade_dict) == 0:
            grade_dict.setdefault(grade_value.value, [name])
        else:
            create_list(name, grade_value.value, grade_dict)
        iterator += 1
    sorted_grades = {}
    for i in sorted(grade_dict, reverse = True):
        sorted_grades[i] = grade_dict[i]
    print(sorted_grades)
    for i in sorted_grades.values():
        for j in i:
            print(j)
    return

def create_list(name, grade, grade_dict):
    if grade in grade_dict:
        grade_dict[grade].append(name)
        grade_dict[grade] = sorted(grade_dict[grade])
        return
    else:
        grade_dict.update({grade: [name]})

if __name__ == "__main__":
    main()