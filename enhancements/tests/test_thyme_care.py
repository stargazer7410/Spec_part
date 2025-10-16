import unittest
from unittest.mock import MagicMock, patch
from python.jobs import thyme_care

class TestThymeCareJob(unittest.TestCase):
    @patch("python.utils.sql_runner.run_sql_for_job")
    @patch("python.utils.error_handler.log_job_observation")
    def test_run(self, mock_log, mock_sql):
        mock_spark = MagicMock()
        mock_df = MagicMock()
        mock_df.count.return_value = 1000
        mock_sql.return_value = mock_df
        params = {"job_name": "thyme-care"}
        thyme_care.run(mock_spark, params)
        mock_log.assert_called()

if __name__ == "__main__":
    unittest.main()
