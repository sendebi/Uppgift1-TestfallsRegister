
from services.test_case_manager import TestCaseManager
from dialogs.console_dialog import (
    display_menu,
    get_menu_choice,
    get_test_case_details,
    display_test_cases,
    get_test_case_number,
    display_message,
    confirm_deletion
)


def main():
    manager = TestCaseManager()

    application_running = True

    while application_running:
        display_menu()
        choice = get_menu_choice()

        # Option 1: Add test case
        if choice == "1":
            title, description, expected_result = get_test_case_details()

            test_case_number = manager.add_test_case(
                title,
                description,
                expected_result
            )

            if test_case_number:
                display_message(
                    f"Test case {test_case_number} added successfully!"
                )
            else:
                display_message(
                    "Invalid input. All fields must contain text."
                )

        # Option 2: Show all test cases
        elif choice == "2":
            test_cases = manager.show_test_cases()
            display_test_cases(test_cases)

        # Option 3: Edit test case
        elif choice == "3":
            test_case_number = get_test_case_number()

            test_case = manager.find_test_case(test_case_number)

            if test_case is None:
                display_message(
                    f"Test case {test_case_number} was not found."
                )

            else:
                title, description, expected_result = get_test_case_details()

                success = manager.edit_test_case(
                    test_case_number,
                    title,
                    description,
                    expected_result
                )

                if success:
                    display_message(
                        f"Test case {test_case_number} updated successfully!"
                    )
                else:
                    display_message(
                        "Could not update the test case. "
                        "Check that all fields contain text."
                    )

        # Option 4: Delete test case
        elif choice == "4":
            test_case_number = get_test_case_number()

            test_case = manager.find_test_case(test_case_number)

            if test_case is None:
                display_message(
                    f"Test case {test_case_number} was not found."
                )

            else:
                confirmed = confirm_deletion()

                if confirmed:
                    success = manager.delete_test_case(test_case_number)

                    if success:
                        display_message(
                            f"Test case {test_case_number} deleted successfully!"
                        )
                    else:
                        display_message(
                            "Could not delete the test case."
                        )

                else:
                    display_message("Deletion cancelled.")

        # Option 5: Exit application
        elif choice == "5":
            application_running = False
            display_message(
                "Thank you for using Test Case Register. Goodbye!"
            )

        # Invalid menu choice
        else:
            display_message(
                "Invalid choice. Please select an option between 1 and 5."
            )


if __name__ == "__main__":
    main()
