import unittest
from booklover import BookLover
import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal


class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        instance = BookLover('Neil', 'nantra', 'fiction')
        instance.add_book('harry potter', 5)
        test_book_dict = instance.book_list.to_dict()
        make_dict = {'book_name': {0: 'harry potter'}, 'book_rating': {0:5}}
        message = "assert made list equals method list"
        # assertEqual() to check equality of first & second value
        self.assertEqual(test_book_dict, make_dict)


    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        instance = BookLover('Neil', 'nantra', 'fiction')
        instance.add_book('harry potter', 5)
        instance.add_book('harry potter', 5)
        test_dict = instance.book_list.to_dict()
        make_dict = {'book_name': {0: 'harry potter'}, 'book_rating': {0:5}}
        message = "assert made list equals method list"
        # assertEqual() to check equality of first & second value
        self.assertEqual(test_dict, make_dict, message)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        instance = BookLover('Neil', 'nantra', 'fiction')
        instance.add_book('harry potter', 5)
        testValue = instance.has_read('harry_potter')
        message = "assert method equals True"
        self.assertTrue(testValue, message)
        
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        instance = BookLover('Neil', 'nantra', 'fiction')
        instance.add_book('harry potter', 5)
        testValue = instance.has_read('Lord of The Rings')
        message = "assert method equals False"
        self.assertFalse(testValue, message)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        instance = BookLover('Neil', 'nantra', 'fiction')
        instance.add_book('harry potter', 5)
        instance.add_book('Lord of The Rings', 4)
        test_num_books = instance.num_books_read()
        real_len = 2
        message = "assert len = 2"
        # assertEqual() to check equality of first & second value
        self.assertEqual(test_num_books, real_len, message)
        

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        instance = BookLover('Neil', 'nantra', 'fiction')
        instance.add_book('harry potter', 5)
        instance.add_book('Lord of The Rings', 4)
        instance.add_book('Twilight', 2)
        test_book_list = instance.fav_books().to_dict()
        message = "assert fav books are HP and LOTR"
        real_list = {'book_name': {0: 'harry potter', 1: 'Lord of The Rings'}, 'book_rating': {0: 5.0, 1: 4.0}}
        # assertEqual() to check equality of first & second value
        self.assertEqual(test_book_list, real_list, message)
        
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)