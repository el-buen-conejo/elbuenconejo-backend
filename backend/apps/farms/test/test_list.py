# Django
from django.test import TestCase
# rest_framework
from rest_framework.test import APIClient
from rest_framework import status
from apps.farms.api.viewsets import FarmViewset
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from rest_framework import viewsets
from rest_framework.response import Response 
from apps.farms.api import viewsets
import unittest
import json


farm = FarmViewset()

"""Validar este tipo de prueba """
# factory = APIRequestFactory()
# rrequest = factory.post('api/farms/', {'name': 'elena',
#                                   'address': 'calle 1',
#                                   'description': 'farm',
#                                   'photo': ''}
#                       )

type_response = Response

class TestListTestCase(TestCase):
    def test_api_farm(self):
        """test verify if api create works"""
        client = APIClient()
        response = client.get('/api/farms/')
        
        self.assertEqual(response.status_code , status.HTTP_200_OK)
        self.assertIs(type(response), type_response, msg='response is not an instance of Response')
         #veriry that the response is a json
        # self.assertIsNone(FarmViewset.create(self, response).__doc__, msg=' function create does not have a docstring')
        

class TestLIstViewsets(unittest.TestCase):
       
    
   def test_list_Viewset(self):

        """test verify that the function create exists"""
        self.assertTrue(hasattr(farm, 'list'),
                        msg='function list does not exist')
   
    # def test_Docstring_Viewset(self):
       
    # self.assertIsNone(FarmViewset.create(self, request).__doc__, msg=' function create does not have a docstring')
    
  
    # def test_response(self):
    #     response = farm.create(self, rrequest)
        
        # verify the response is an response object




if __name__ == '__main__':
    unittest.main()
