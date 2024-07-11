from django.test import TestCase
from .utils.ReadCSV import readCSV
from .utils.DTO import DTO

class TestReadCSV(TestCase):
    """
    A test case for the readCSV function.
    """

    def setUp(self):
        self.fileName = "D:/Git/PythonLearning/PythonLearning/trafficdata/traffic_data_app/data/Traffic_Volumes_-_Provincial_Highway_System.csv"

    def test_readCSV(self):
        dtos = readCSV(self.fileName)
        self.assertIsInstance(dtos, list)
        self.assertTrue(all(isinstance(dto, DTO) for dto in dtos))
