'''testing module'''
import unittest
from check_json import check_location

class Testing(unittest.TestCase):
    '''test for lat longs for:
    Bangalore
    New Delhi
    Pune
    Hyderabad
    '''
    def test_1_inbangalore(self):
        '''Test case'''
        check1 = check_location("Bangalore", 12.9129197, 77.6303869)
        self.assertEqual(check1, 1)

    def test_2_outbangalore(self):
        '''Test case'''
        check2 = check_location("Bangalore", -8.4553718, 114.7913839)
        self.assertEqual(check2, 0)

    def test_3_innewdelhi(self):
        '''Test case'''
        check3 = check_location("New Delhi", 28.620954, 77.215752)
        self.assertEqual(check3, 1)

    def test_4_outnewdelhi(self):
        '''Test case'''
        check4 = check_location("New Delhi", 28.7753992, 76.8130804)
        self.assertEqual(check4, 0)

    def test_5_indiawest(self):
        '''Test case'''
        check5 = check_location("India", 24.9857629, 80.0751535)
        self.assertEqual(check5, 1)

    def test_6_indianorth(self):
        '''Test case'''
        check6 = check_location("India", 33.192038, 76.248406)
        self.assertEqual(check6, 1)

    def test_7_indiaeast(self):
        '''Test case'''
        check7 = check_location("India", 27.722709, 96.735429)
        self.assertEqual(check7, 1)

    def test_8_indiasouth(self):
        '''Test case'''
        check8 = check_location("India", 8.230485, 77.521544)
        self.assertEqual(check8, 1)

    def test_9_indiawest(self):
        '''Test case'''
        check9 = check_location("India", 23.583946, 58.2835811)
        self.assertEqual(check9, 0)

    def test_10_indianorth(self):
        '''Test case'''
        check10 = check_location("India", 57.489161, 86.098448)
        self.assertEqual(check10, 0)

    def test_11_indiaeast(self):
        '''Test case'''
        check11 = check_location("India", 37.440254, 88.655882)
        self.assertEqual(check11, 0)

    def test_12_indiasouth(self):
        '''Test case'''
        check12 = check_location("India", 1.076794, 100.687324)
        self.assertEqual(check12, 0)

    def test_13_inpune(self):
        '''Test case'''
        check13 = check_location("Pune", 18.5918652, 73.9084917)
        self.assertEqual(check13, 1)

    def test_14_outpune(self):
        '''Test case'''
        check14 = check_location("Pune", 17.9677184, 74.1024077)
        self.assertEqual(check14, 0)

    def test_15_inhyderabad(self):
        '''Test case'''
        check15 = check_location("Hyderabad", 17.4122998, 78.26796)
        self.assertEqual(check15, 1)

    def test_16_outhyderabad(self):
        '''Test case'''
        check16 = check_location("Hyderabad", 17.9581458, 79.5691675)
        self.assertEqual(check16, 0)


if __name__ == '__main__':
    unittest.main()
