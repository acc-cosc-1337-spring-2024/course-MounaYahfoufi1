import unittest
from src.homework.i_dictionaries_and_sets import get_students_who_took_prog1_and_prog2,get_students_who_took_prog2_only,get_students_who_took_prog1_not_prog_2,get_students_who_took_prog2_not_prog_1

class Test_Config(unittest.TestCase):

  def test_get_students_who_took_prog1_and_prog2():
    prog1 = {'Student1', 'Student2', 'Student3'}
    prog2 = {'Student3', 'Student4', 'Student5'}
    expected = {'Student3'}
    assert get_students_who_took_prog1_and_prog2(prog1, prog2) == expected, f"Expected {expected}, got {get_students_who_took_prog1_and_prog2(prog1, prog2)}"

def test_get_students_who_took_prog1_or_prog2():
    prog1 = {'Student1', 'Student2', 'Student3'}
    prog2 = {'Student3', 'Student4', 'Student5'}
    expected = {'Student1', 'Student2', 'Student3', 'Student4', 'Student5'}
    assert get_students_who_took_prog1_and_prog2(prog1, prog2) == expected, f"Expected {expected}, got {get_students_who_took_prog1_and_prog2(prog1, prog2)}"

def test_get_students_who_took_prog1_not_prog2():
    prog1 = {'Student1', 'Student2', 'Student3'}
    prog2 = {'Student3', 'Student4', 'Student5'}
    expected = {'Student1', 'Student2'}
    assert get_students_who_took_prog1_not_prog_2(prog1, prog2) == expected, f"Expected {expected}, got {get_students_who_took_prog1_not_prog_2(prog1, prog2)}"

def test_get_students_who_took_prog2_not_prog1():
    prog1 = {'Student1', 'Student2', 'Student3'}
    prog2 = {'Student3', 'Student4', 'Student5'}
    expected = {'Student4', 'Student5'}
    assert get_students_who_took_prog2_not_prog_1(prog1, prog2) == expected, f"Expected {expected}, got {get_students_who_took_prog2_not_prog_1(prog1, prog2)}"

# Run the tests
if __name__ == "__main__":
    test_get_students_who_took_prog1_or_prog2()
    test_get_students_who_took_prog1_or_prog2()
    test_get_students_who_took_prog1_not_prog2()
    test_get_students_who_took_prog2_not_prog1()
    print("All tests passed!")