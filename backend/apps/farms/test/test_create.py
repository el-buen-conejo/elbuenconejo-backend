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


farm = FarmViewset()

"""Validar este tipo de prueba """
# factory = APIRequestFactory()
# rrequest = factory.post('api/farms/', {'name': 'elena',
#                                   'address': 'calle 1',
#                                   'description': 'farm',
#                                   'photo': ''}
#                       )

type_response = Response

class TestCreateTestCase(TestCase):
    def test_api_farm(self):
        """test verify if api create works"""
        client = APIClient()
        response = client.post('/api/farms/',
                               {'name': 'elena',
                                'address': 'calle 1',
                                'description': 'farm',
                                "is_active" : 'True',
                                'photo': "prueba"},
                               format='json')
        
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)
        self.assertIs(type(response), type_response, msg='response is not an instance of Response')
         #veriry that the response is a json
        # self.assertIsNone(FarmViewset.create(self, response).__doc__, msg=' function create does not have a docstring')
        

class TestFarmViewsets(unittest.TestCase):

    def test_class_exists(self):
        """test verify if class exist and if has a docstring"""        
        self.assertTrue(hasattr(viewsets, 'FarmViewset'),
                        msg='Class  farmViewset does not exist')
        self.assertIsNone(FarmViewset.__doc__,
                          msg=' class FarmViewset does not have a docstring')
        self.assertTrue(issubclass(FarmViewset, viewsets.GenericViewSet),
                        msg='Class FarmViewset does not inherit from GenericsViewSet')
       
    
    def test_farm_get_atrributes(self):
        """test verify class has atributes"""
        self.assertTrue(hasattr(farm, "name"))
        self.assertTrue(hasattr(farm, "description"))
        self.assertTrue(hasattr(farm, 'serializer_class'),
                        msg='serializer_class does not exist')
        self.assertTrue(hasattr(farm, 'permission_classes'),
                        msg='permission_classes does not exist')
    
    def test_Create_Viewset(self):

        """test verify that the function create exists"""
        self.assertTrue(hasattr(farm, 'create'),
                        msg='function create does not exist')
   
    # def test_Docstring_Viewset(self):
       
    # self.assertIsNone(FarmViewset.create(self, request).__doc__, msg=' function create does not have a docstring')
    
  
    # def test_response(self):
    #     response = farm.create(self, rrequest)
        
        # verify the response is an response object




if __name__ == '__main__':
    unittest.main()
