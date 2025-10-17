# Entry point for job execution
import os
import sys
import importlib
from python.utils.param_loader import load_params
from python.utils.error_handler import ErrorHandler
from python.utils.log_manager import get_logger

def run_job(file_directory, filename, cloud_provider):
    os.environ["CLOUD_PROVIDER"] = cloud_provider
    job_name = filename.split(".")[0]
    logger = get_logger(job_name)
    try:
        logger.info(f"Starting job: {job_name}")
        params = load_params(file_directory, filename)
        job_module = importlib.import_module(f"python.jobs.{job_name.replace('-', '_')}")
        job_module.run(params, logger)
        logger.info(f"Job {job_name} completed successfully.")
    except Exception as e:
        error_handler = ErrorHandler(logger)
        error_handler.capture(e, context={"job_name": job_name})
        logger.error(f"Job {job_name} failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <file_directory> <filename> <cloud_provider>")
        sys.exit(1)
    run_job(sys.argv[1], sys.argv[2], sys.argv[3])
