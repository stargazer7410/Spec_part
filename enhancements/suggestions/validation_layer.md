# Validation Layer

## Description
Ensure that the job_name provided in job_params.json is valid and exists in the job_registry.

## Implementation Strategy
- Add a check in main.py to verify job_name against job_registry.
- Raise a descriptive error or log a warning if the job_name is not registered.
- Optionally, validate the existence of corresponding job and SQL files.
