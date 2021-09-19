import unittest
from main import rate_calculator
from input_test import input_set_1,input_set_2,input_set_3,input_set_4

class TestCase(unittest.TestCase):
  # Example test case 1
  def test_case_1(self):
    total_rates = rate_calculator(input_set_1)
    self.assertEqual(
      total_rates, 
      {"value" : 13725}
    )
  

  def test_case_2(self):
    total_rates = rate_calculator(input_set_2)
    
    self.assertEqual(
      total_rates, 
      {"value" : 13725}
    )


  def test_case_3(self):
    total_rates = rate_calculator(input_set_3)
    
    self.assertEqual(
      total_rates, 
      {"value" : 13760}
    )


  def test_case_4(self):
    total_rates = rate_calculator(input_set_4)
    
    self.assertEqual(
      total_rates, 
      {"value" : 19650}
    )

    
if __name__ == "__main__":
  unittest.main()