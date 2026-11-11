from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class TestCase:
    title:str
    description:str
    expected_result:str
    id: UUID = field(default_factory=uuid4)  # Automatically generates a unique ID when a new test case is created
    test_case_number: str = ""              # Testcase number is assigned later by the repository 
