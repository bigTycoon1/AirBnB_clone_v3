#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os


class test_Place(test_basemodel):
    """ class test place"""

    def __init__(self, *args, **kwargs):
        """ initialize test class"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ test city_id attr"""
        new = self.value()
        self.assertEqual(type(new.city_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_user_id(self):
        """ test user_id attr"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_name(self):
        """ test name attr"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_description(self):
        """test description attr"""
        new = self.value()
        self.assertEqual(type(new.description), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_number_rooms(self):
        """ test number of rooms attr"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_number_bathrooms(self):
        """ test number of bathrooms attr"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_max_guest(self):
        """ test max_guest attr"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_price_by_night(self):
        """ test price by night attr"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_latitude(self):
        """ test latitude attr"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_longitude(self):
        """ test longitude attr"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_amenity_ids(self):
        """ test_amenity ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
