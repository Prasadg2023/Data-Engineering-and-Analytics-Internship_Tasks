## Nested Lists
## https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':

    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    students.sort(key=lambda x: (x[1], x[0]))
    second_lowest_score = sorted(set([score for name, score in students]))[1]
    second_lowest_students = [name for name, score in students if score == second_lowest_score]
    second_lowest_students.sort()
    for student in second_lowest_students:
        print(student)