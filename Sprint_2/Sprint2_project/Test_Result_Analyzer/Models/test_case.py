
test_results = [
    {"id": "TC101", "status": "Pass"},
    {"id": "TC102", "status": "Fail"},
    {"id": "TC103", "status": "Blocked"}
]

class TestCase():
    def __init__(self, id, status):
        self.id = id
        self.status = status

    def validate_status(self):
        allowed = ["Pass", "Fail", "Blocked"]
        if self.status in allowed:
            return True
        else:
            raise ValueError(f"Invalid status: {self.status}")
        
    def is_failed(self):
        if self.status == "Fail":
            return True
        else:
            return False
    
    def __str__(self):
        return f"ID:{self.id} | Status:{self.status}"


test_cases = []
for i in test_results:
    result = i
    call = TestCase(result["id"], result["status"])
    test_cases.append(call)
    print(str(call))