class LoadEnvException(BaseException):
    def __str__(self):
        return 'Create .env file with fields from example.env'
