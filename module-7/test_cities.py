import unittest
import city_functions

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do cities and countries like 'Santiago, Chile' work?"""
        formatted_string = city_functions.city_country("Santiago", "Chile")
        self.assertEqual(formatted_string, "Santiago, Chile")

if __name__ == '__main__':
    unittest.main()
    