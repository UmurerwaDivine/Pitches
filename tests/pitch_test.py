import unittest

from app.models import Pitch,User
from app import db
class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(1234,'Python Must Be Crazy',1,'/khsjha27hbs')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

if __name__ == '__main__':
    unittest.main()