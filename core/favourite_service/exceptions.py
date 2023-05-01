from core.custom_base_exception import CustomBaseException

class UserRequiredException(CustomBaseException):
    def __init__(self):
        super().__init__('User name is required', 400)

class NewsItemRequiredException(CustomBaseException):
    def __init__(self):
        super().__init__('News id is required', 400)

class NewsItemNotFoundException(CustomBaseException):
    def __init__(self):
        super().__init__('News item not found', 400)

class UserNotFoundException(CustomBaseException):
    def __init__(self):
        super().__init__('User not found', 400)
