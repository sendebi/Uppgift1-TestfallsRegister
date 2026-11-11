from models.test_case import TestCase

class TestCaseRepository:

    def __init__(self):
        self.test_cases = []
        self.next_number = 1

    def generate_test_case_number(self) -> str:
        test_case_number = f"TC_{self.next_number:02d}"
        self.next_number += 1
        return test_case_number
        
    def add(self, test_case:TestCase) -> None: 
        self.test_cases.append(test_case)

    def get_all(self) -> list[TestCase]:
        return self.test_cases

    def find_by_number(self, test_case_number: str) -> TestCase | None:
        for test_case in self.test_cases:
            if test_case.test_case_number == test_case_number:
                return test_case
            
        return None   
            
    def delete(self, test_case_number: str) -> bool:
        for test_case in self.test_cases:
            if test_case.test_case_number == test_case_number:
                self.test_cases.remove(test_case)
                return True

        return False        