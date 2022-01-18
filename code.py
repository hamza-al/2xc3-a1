def are_valid_groups(student_id, groups):
    for students in groups:
        for student in students:
            if student_id == groups:
                return True
            else:
                return False
