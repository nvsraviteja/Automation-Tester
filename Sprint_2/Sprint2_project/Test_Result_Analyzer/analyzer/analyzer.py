from models.test_case import TestCase
from models.test_case import test_cases

class TestResultAnalyzer():

    def __init__(self, test_cases):
        self.test_cases = test_cases
        self.total = len(test_cases)
        

    def count_pass(self):
        pass_count = 0
        for test_case in self.test_cases:
            if test_case.status == "Pass":
                pass_count += 1
        return pass_count

    def count_fail(self):
        fail_count = 0
        for test_case in self.test_cases:
            if test_case.status == "Fail":
                fail_count += 1
        return fail_count
    
    def count_blocked(self):
        block_count = 0
        for test_case in self.test_cases:
            if test_case.status == "Blocked":
                block_count += 1
        return block_count

    def get_failed_ids(self):
        fail_id = []
        for test_case in self.test_cases:
            if "Fail" in test_case.status:
                fail_id.append(test_case.id)
        return fail_id

    def generate_summary(self):
        summary = {
            "Total": self.total,
            "Pass": self.count_pass(),
            "Fail": self.count_fail(),
            "Blocked": self.count_blocked(),
            "Failed IDs": self.get_failed_ids()
        }
        return summary

c = TestResultAnalyzer(test_cases)

