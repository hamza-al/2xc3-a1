from typing import List


def are_valid_groups(numbers: List[str], groups: List[List[str]]):
    for group in groups:
        if len(group) > 3 or len(group) < 2:
            return False
    students_in_groups = []
    for group in groups:
        for student in group:
            students_in_groups.append(student)
    for i in numbers:
        if i not in students_in_groups:
            return False
    return True
