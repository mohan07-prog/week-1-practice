def calc_average(nums):
    k = sum(nums)
    avg = k / len(nums)
    return avg

def find_missing_skills(student_skills, required_skills):
    missing_skills = []

    for skill in required_skills:
        if skill not in student_skills:
            missing_skills.append(skill)

    return missing_skills


def build_summary(name, marks, skills, required_skills):
    avg = calc_average(marks)
    missing = find_missing_skills(skills, required_skills)
    
    if avg >= 60 and len(missing) == 0:
        status = "ready"
    else:
        status = "need practice"

    return {
        "name": name,
        "avg": avg,
        "status": status,
        "missing": missing
    }


name = input("Enter The Name: ")
n = int(input("enter the number of subjects: "))
marks = list(map(int, input("enter the marks: ")))
s = int(input("enter the number of skills: "))
student_skills = input("enter the skills: ").split()
required_skills = input("enter the required skills: ").split()

result = build_summary(
    name,
    marks,
    student_skills,
    required_skills
)

print("student summary: ")
print("name:", result["name"])
print("avg:", result["avg"])
print("status:", result["status"])

if len(result["missing"]) == 0:
    print("missing skills: none")
else:
    print("missing skills: ", result["missing"])
