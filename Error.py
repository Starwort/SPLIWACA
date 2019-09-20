import typing as ty

#ERROR CLASS
class Error:
    def __init__(self, error_name: str, details: str):
        self.error_name = error_name
        self.details = details
        
    def as_string(self):
        return f"{self.error_name}: {self.details}"
        
#SUBCLASSES
#ILLEGAL CHARACTER
class IllegalCharError(Error):
    def __init__(self, details: str):
        super().__init__("IllegalCharError",details)