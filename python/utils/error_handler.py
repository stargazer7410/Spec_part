class ErrorHandler:
    def __init__(self, logger):
        self.logger = logger
    def capture(self, error, context):
        self.logger.error(f'Error: {error}, Context: {context}')