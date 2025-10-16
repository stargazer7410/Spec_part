# Job Registry Automation

## Description
Automatically discover available jobs instead of manually listing them in job_params.json.

## Implementation Strategy
- Scan the python/jobs directory.
- Populate job_registry dynamically.
- Validate job_name against discovered jobs.
