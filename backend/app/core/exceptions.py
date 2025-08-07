class AppError(Exception):
    def __init__(self, status_code=500, message="Ocorreu um erro inesperado", headers: dict | None = None ):
        self.status_code = status_code
        self.message = message
        self.headers = headers


class UserNotFoundError(AppError):
    def __init__(self, user_id=None):
        message = "User not found" if user_id is None else f"User with id {user_id} not found"
        super().__init__(status_code=404, message=message)


class UserAlreadyExistsError(AppError):
    def __init__(self, email):
        message = f'User with email "{email}" already exists'
        super().__init__(status_code=400, message=message)


class InvalidPasswordError(AppError):
    def __init__(self):
        message="Current password is incorrect"
        super().__init__(status_code=401, message=message)


class AuthenticationError(AppError):
    def __init__(self, email):
        message = f'Could not authenticate user with email "{email}"'
        headers = {"WWW-Authenticate": "Bearer"}
        super().__init__(status_code=401, message=message, headers=headers)
