
from models.test_case import TestCase
from repositories.test_case_repository import TestCaseRepository


class TestCaseManager:

    def __init__(self):
        self.repository = TestCaseRepository()

    def validate_input(
        self,
        title: str,
        description: str,
        expected_result: str
    ) -> bool:
        return bool(
            title.strip()
            and description.strip()
            and expected_result.strip()
        )

    def add_test_case(
        self,
        title: str,
        description: str,
        expected_result: str
    ) -> str:

        if not self.validate_input(title, description, expected_result):
            return ""

        title = title.strip()
        description = description.strip()
        expected_result = expected_result.strip()

        test_case = TestCase(
            title=title,
            description=description,
            expected_result=expected_result
        )

        test_case.test_case_number = self.repository.generate_test_case_number()

        self.repository.add(test_case)

        return test_case.test_case_number

    def show_test_cases(self) -> list[TestCase]:
        return self.repository.get_all()

    def find_test_case(self, test_case_number: str) -> TestCase | None:
        return self.repository.find_by_number(
            test_case_number.strip().upper()
        )

    def edit_test_case(
        self,
        test_case_number: str,
        title: str,
        description: str,
        expected_result: str
    ) -> bool:

        if not self.validate_input(title, description, expected_result):
            return False

        test_case = self.repository.find_by_number(
            test_case_number.strip().upper()
        )

        if test_case is None:
            return False

        test_case.title = title.strip()
        test_case.description = description.strip()
        test_case.expected_result = expected_result.strip()

        return True

    def delete_test_case(self, test_case_number: str) -> bool:
        return self.repository.delete(
            test_case_number.strip().upper()
        )
