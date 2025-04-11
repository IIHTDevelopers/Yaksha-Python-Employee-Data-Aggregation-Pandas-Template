import unittest
import pandas as pd
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import os


class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeDataAnalysis("employee_data.csv")
        cls.test_obj = TestUtils()

    def test_csv_loading(self):
        """Test if the CSV file is loaded correctly."""
        try:
            if not self.analysis:
                self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
                print("TestCSVLoading = Failed")
                return
            obj = not self.analysis.df.empty
            self.test_obj.yakshaAssert("TestCSVLoading", obj, "functional")
            print("TestCSVLoading = Passed" if obj else "TestCSVLoading = Failed")
        except:
            self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
            print("TestCSVLoading = Failed")
                
    def test_display_head(self):
        """Test if the first 5 rows are returned correctly."""
        try:
            head = self.analysis.display_head()
            if head is None:
                head = []
            obj = len(head) == 5
            self.test_obj.yakshaAssert("TestDisplayHead", obj, "functional")
            print("TestDisplayHead = Passed" if obj else "TestDisplayHead = Failed")
        except Exception as e:
            print("TestDisplayHead = Failed")

    def test_group_by_department(self):
        """Test if the employee data can be grouped by department and aggregate statistics can be computed."""
        try:
            # Get aggregated data
            aggregated_data = self.analysis.group_by_department()

            # Check that the index is correctly set to Department (Department is the index now)
            obj_index = isinstance(aggregated_data.index, pd.Index) and 'Department' == aggregated_data.index.name
            
            # Check if the aggregated data has expected columns (i.e., aggregated statistics)
            obj_columns = all(col in aggregated_data.columns for col in ['Age_Mean', 'Salary_Mean', 'Age_Median', 'Salary_Median', 'Employee_Count'])

            # Combine both checks
            obj = obj_index and obj_columns
            self.test_obj.yakshaAssert("TestGroupByDepartment", obj, "functional")
            
            print("TestGroupByDepartment = Passed" if obj else "TestGroupByDepartment = Failed")
        except Exception as e:
            print("TestGroupByDepartment = Failed")


    def test_export_aggregated_data(self):
        """Test if the aggregated statistics are saved to a new CSV file."""
        self.analysis.export_aggregated_data()
        try:
            pd.read_csv("department_statistics.csv")
            obj = True
        except FileNotFoundError:
            obj = False
        self.test_obj.yakshaAssert("TestExportAggregatedData", obj, "functional")
        print("TestExportAggregatedData = Passed" if obj else "TestExportAggregatedData = Failed")
