from models.test_case import TestCase

def display_menu():
    print("\n===== TEST CASE REGISTER =====")
    print("1. Add test case")
    print("2. Show all test cases")
    print("3. Edit test case")
    print("4. Delete test case")
    print("5. Exit")

def get_menu_choice() -> str:
    return input("Choose an option (1-5): ").strip()


def get_test_case_details() -> tuple[str, str, str]:
    title = input("Enter test case title: ").strip()
    description = input("Enter test case description: ").strip()
    expected_result = input("Enter expected result: ").strip()

    return title, description, expected_result


def display_test_cases(test_cases: list[TestCase]) -> None:
    if not test_cases:
        print("\nNo test cases have been registered yet.")
        return

    print("\n===== REGISTERED TEST CASES =====")

    for test_case in test_cases:
        print(f"\nTest case number: {test_case.test_case_number}")
        print(f"Title: {test_case.title}")
        print(f"Description: {test_case.description}")
        print(f"Expected result: {test_case.expected_result}")
        print(f"UUID: {test_case.id}")


def get_test_case_number() -> str:
    return input("Enter test case number (e.g. TC_01): ").strip().upper()


def display_message(message: str) -> None:
    print(f"\n{message}")
    

def confirm_deletion() -> bool:
    answer = input("Are you sure you want to delete this test case? (y/n): ").strip().lower()
    return answer == "y"    