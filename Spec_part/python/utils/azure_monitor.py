class AzureMonitorLogger:
    def __init__(self, job_name):
        import logging
        self.logger = logging.getLogger(job_name)
        self.logger.setLevel(logging.INFO)
    def info(self, msg):
        self.logger.info(f'[Azure] {msg}')
    def error(self, msg):
        self.logger.error(f'[Azure] {msg}')