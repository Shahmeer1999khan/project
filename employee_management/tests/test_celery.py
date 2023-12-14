from django.test import TestCase
from unittest import mock
from employee_management.tasks import test_func


class CeleryTasksTestCase(TestCase):
    @mock.patch('employee_management.tasks.test_func.apply_async')
    def test_test_func_task(self, mock_apply_async):
        mock_result = mock.Mock()

        mock_result.successful.return_value = True
        mock_result.get.return_value = "DONE"

        mock_apply_async.return_value = mock_result

        result = test_func.apply_async()

        self.assertTrue(result.successful())
        result_value = result.get()
        self.assertEqual(result_value, "DONE")

if __name__ == '__main__':
    import unittest
    unittest.main()
