
# 🧠 Specialty_Partners Project Summary

## 🔧 Purpose
Automate and orchestrate data processing using **Azure Data Factory (ADF)** and **Databricks**, enabling dynamic job execution, structured logging, and centralized monitoring.

## 🚀 Workflow Overview
1. **ADF** monitors a folder in **Azure Data Lake Storage (ADLS)**.
2. On file drop, ADF triggers a **Databricks job**, passing a `job_name`.
3. **Databricks** executes `main.py`, which:
   - Loads job parameters from config files.
   - Dynamically imports and runs the corresponding job module.
   - Executes an associated SQL script if available.
   - Logs events locally and to **Azure Monitor**.

## 📁 Folder Structure
```
Specialty_Partners
│
├── main.py
│
├── config
│   ├── config.json
│   └── job_params.json
│
├── python
│   ├── jobs
│   │   └── thyme-care.py
│   │
│   └── utils
│       ├── logger_setup.py
│       ├── param_loader.py
│       ├── error_handler.py
│       ├── sql_runner.py
│       ├── constants.py
│       ├── log_manager.py
│       └── azure_monitor.py
│
├── sql
│   └── thyme-care.sql
```

## ✅ Key Features
- **Config-driven architecture**: Externalized paths and job mappings.
- **Dynamic job execution**: Uses `importlib` for modular job loading.
- **Structured logging**: Dual logging to local files and Azure Monitor.
- **Centralized error handling**: Managed via `ErrorHandler` class.
- **Reusable utilities**: Modular components for logging, SQL, and parameter handling.
- **Scalable design**: Easily extendable with new jobs and configurations.

## 🧪 Testing & Validation
- Verified integration of all modules and functions.
- Simulated end-to-end job execution:
  - Job name validation
  - Parameter loading
  - Job module execution
  - SQL script detection and execution
  - Logging and Azure Monitor event tracking

## 📦 Download
Full project available: `📁 Specialty_Partners.zip`
