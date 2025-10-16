import logging
from datetime import datetime

logging.basicConfig(filename='error_log.log', level=logging.ERROR)

def log_exception(e, context=""):
    logging.error(f"Exception in {context}: {str(e)}", exc_info=True)

def log_job_observation(job_name, job_run_time, source_record_count, success_count, failure_count):
    with open("job_observations.log", "a") as log_file:
        log_file.write(f"{datetime.now()} - Job Name: {job_name} | Run Time: {job_run_time} | Source Records: {source_record_count} | Processed Successfully: {success_count} | Failed Records: {failure_count}\n")
