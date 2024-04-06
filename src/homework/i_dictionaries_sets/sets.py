#
# Define the functions as specified

def get_students_who_took_prog1_and_prog2(prog1, prog2):
    return prog1.intersection(prog2)

def get_students_who_took_prog1_or_prog2(prog1, prog2):
    return prog1.union(prog2)

def get_students_who_took_prog1_not_prog2(prog1, prog2):
    return prog1.difference(prog2)

def get_students_who_took_prog2_not_prog1(prog1, prog2):
    return prog2.difference(prog1)
