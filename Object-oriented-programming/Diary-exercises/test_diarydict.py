import unittest
from diarydict import DiaryDict
from datetime import date

class TestDiaryDict(unittest.TestCase):
    ''' 
    tests DiaryDicts property observations, add, modify, and remove methods
    '''
    
    def test_observations(self):
        '''checks the length of observations after setting the property '''
        diary = DiaryDict()        
        diary.observations = {0:['hawk',  date(2000, 12, 10)], 1:['hawk'],  2:['hawk',  date(2000, 1, 1), 'might have been the same specimen saw earlier'] }
        self.assertTrue(len(diary.observations) == 3)
       
    def test_add(self):
        '''checks the length of observations after adding new observation '''
        diary = DiaryDict()
        diary.observations = {0:['hawk',  date(2000, 12, 10)], 1:['hawk'],  2:['hawk',  date(2000, 1, 1), 'might have been the same specimen saw earlier'] }
        old = len(diary.observations)
        diary.add(len(diary.observations), 'eagle',  date(1980, 1, 4), 'very far but cound not be anything else')
        self.assertEqual(len(diary.observations), old + 1)

    def test_modify_exist(self):
        '''checks the length of modified observation after adding modifying observation and length of observations (unchanged)'''
        diary = DiaryDict()
        diary.observations = {0:['hawk',  date(2000, 12, 10)], 1:['hawk'],  2:['hawk',  date(2000, 1, 1), 'might have been the same specimen saw earlier'] }
        old_1 = len(diary.observations)
        old_2 = len(diary.observations[1])
        new = ['hawk',  date(1990, 1, 4), 'not actually sure I saw it']
        diary.modify(1, new[0], new[1], new[2])
        self.assertFalse(old_1 == len(diary.observations) and old_2 == len(new))
        
    def test_modify_not_exist(self):
        '''checks the length of modified observation after adding modifying observation and length of observations (changed)'''
        diary = DiaryDict()
        diary.observations = {0:['hawk',  date(2000, 12, 10)], 1:['hawk'],  2:['hawk',  date(2000, 1, 1), 'might have been the same specimen saw earlier'] }
        old = len(diary.observations)
        diary.modify(5, 'hawk',  date(1995, 11, 14), 'really beautiful')
        self.assertEqual(len(diary.observations), old + 1)  
        
    def test_remove(self):
        '''checks the length of observations after adding new observation and that the removed item is a list'''
        diary = DiaryDict()
        diary.observations = {0:['hawk',  date(2000, 12, 10)], 1:['hawk'],  2:['hawk',  date(2000, 1, 1), 'might have been the same specimen saw earlier'] }
        old = len(diary.observations)
        removed = diary.remove(1)
        self.assertTrue(isinstance(removed, list) and len(diary.observations) == old - 1 )        
        
if __name__ == '__main__':
    unittest.main()        