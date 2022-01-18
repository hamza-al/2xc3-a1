def are_valid_groups(numbers, groups):
    students_in_groups = []
    for group in groups:
        for student in group:
            students_in_groups.append(student)
    for i in numbers:
        if i not in students_in_groups:
            return False
    return True
