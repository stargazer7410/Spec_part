class LogManager:
    def __init__(self, logger):
        self.logger = logger

    def log_job_start(self, job_name):
        self.logger.info(f"Job {job_name} started.")

    def log_job_success(self, job_name):
        self.logger.info(f"Job {job_name} completed successfully.")

    def log_job_failure(self, job_name, error):
        self.logger.error(f"Job {job_name} failed with error: {error}")
