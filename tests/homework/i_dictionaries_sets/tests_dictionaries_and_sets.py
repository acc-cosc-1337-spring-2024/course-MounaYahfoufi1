import unittest
from src.homework.i_dictionaries_sets import get_p_distance
from src.homework.i_dictionaries_sets import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        # Test case to assert that adding Widget1 with quantity of 10 inserts the correct value
        inventory_dictionary = {}
        add_inventory(inventory_dictionary, "Widget1", 10)
        self.assertEqual(inventory_dictionary["Widget1"], 10)

        # Test case to assert that adding Widget1 with quantity of 25 updates the existing quantity correctly
        add_inventory(inventory_dictionary, "Widget1", 25)
        self.assertEqual(inventory_dictionary["Widget1"], 35)

        # Test case to assert that adding Widget1 with quantity of -10 updates the existing quantity correctly
        add_inventory(inventory_dictionary, "Widget1", -10)
        self.assertEqual(inventory_dictionary["Widget1"], 25)

    def test_remove_inventory_widget(self):
        # Test case to add two widgets with quantities of your choice
        inventory_dictionary = {"widget1": 5, "widget2": 10}

        # Remove widget1
        remove_inventory_widget(inventory_dictionary, "widget1", 5)

        # Test that the length of dictionary is 1 after removal
        self.assertEqual(len(inventory_dictionary), 1)

        # Test that widget2 still exists after removal of widget1
        self.assertTrue("widget2" in inventory_dictionary)

if __name__ == '__main__':
    unittest.main()

