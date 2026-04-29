class DepartmentNotFoundError(Exception):
    
    def __init__(self,message="Department not found or has no students."):
        self.message=message
        super().__init__(self.message)