import unittest
from unittest.mock import patch, MagicMock
from python.utils import sql_runner

class TestSQLRunner(unittest.TestCase):
    @patch("builtins.open", new_callable=unittest.mock.mock_open, read_data="SELECT * FROM test_table;")
    def test_run_sql_for_job(self, mock_open):
        mock_spark = MagicMock()
        mock_spark.sql.return_value = "mocked dataframe"
        params = {"job_name": "test-job"}
        result = sql_runner.run_sql_for_job(mock_spark, params)
        self.assertEqual(result, "mocked dataframe")

if __name__ == "__main__":
    unittest.main()
