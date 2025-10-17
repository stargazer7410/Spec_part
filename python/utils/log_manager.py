import os
def get_logger(job_name):
    cloud = os.getenv('CLOUD_PROVIDER', 'local').lower()
    if cloud == 'azure':
        from python.utils.azure_monitor import AzureMonitorLogger
        return AzureMonitorLogger(job_name)
    elif cloud == 'gcp':
        from python.utils.gcp_monitor import GCPMonitorLogger
        return GCPMonitorLogger(job_name)
    else:
        import logging
        logger = logging.getLogger(job_name)
        logger.setLevel(logging.INFO)
        return logger