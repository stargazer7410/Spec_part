import json
import importlib
from python.utils.param_loader import load_params

def main():
    params = load_params('config/job_params.json')
    job_name = params.get('job_name')
    job_module = importlib.import_module(f'python.jobs.{job_name}')
    from python.utils.spark_session import get_spark_session
    spark = get_spark_session()
    job_module.run(spark, params)

if __name__ == '__main__':
    main()
