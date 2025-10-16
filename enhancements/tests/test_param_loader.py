import unittest
from unittest.mock import mock_open, patch
import json
from python.utils import param_loader

class TestParamLoader(unittest.TestCase):
    def test_load_params_success(self):
        mock_data = json.dumps({
            "job_name": "thyme-care",
            "folder_name": "inbound/thyme-care/filename.csv",
            "job_registry": ["thyme-care", "sales_reporting", "inventory_management"]
        })
        with patch("builtins.open", mock_open(read_data=mock_data)):
            params = param_loader.load_params("config/job_params.json")
            self.assertEqual(params["job_name"], "thyme-care")
            self.assertIn("thyme-care", params["job_registry"])

    def test_load_params_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                param_loader.load_params("config/job_params.json")

if __name__ == "__main__":
    unittest.main()
