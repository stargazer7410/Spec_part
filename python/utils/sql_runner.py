import os

def run_sql_for_job(spark, params):
    job_name = params.get("job_name")
    sql_file_path = os.path.join("sql", f"{job_name}.sql")
    with open(sql_file_path, "r") as file:
        query = file.read()
    print(f"Executing SQL for job: {job_name}")
    return spark.sql(query)
