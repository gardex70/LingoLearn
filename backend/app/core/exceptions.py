from fastapi import HTTPException

class UserError(HTTPException):
    """Base exception for user-related errors"""
    def __init__(self, status_code: int, detail: str, headers: dict | None = None):
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class UserNotFoundError(UserError):
    def __init__(self, user_id=None):
        message = "User not found" if user_id is None else f"User with id {user_id} not found"
        super().__init__(status_code=404, detail=message)

class UserAlreadyExistsError(UserError):
    def __init__(self, email):
        super().__init__(status_code=400, detail=f'User with email "{email}" already exists')

class PasswordMismatchError(UserError):
    def __init__(self):
        super().__init__(status_code=400, detail="New passwords do not match")

class InvalidPasswordError(UserError):
    def __init__(self):
        super().__init__(status_code=401, detail="Current password is incorrect")

class AuthenticationError(UserError):
    def __init__(self, message: str = "Could not validate user"):
        super().__init__(status_code=401, detail=message)

