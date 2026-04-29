class DepartmentNotFoundError(Exception):
    """Raised when no students found in the requested department."""
    def __init__(self,message="Department not found or has no students."):
        self.message=message
        super().__init__(self.message)