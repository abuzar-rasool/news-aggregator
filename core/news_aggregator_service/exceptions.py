from core.custom_base_exception import CustomBaseException

class FailedToRetriveData(CustomBaseException):
    def __init__(self, source):
        super().__init__(f'Failed to retrive data from {str(source)}', 500)
