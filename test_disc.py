""" module which test line module """
from unittest import TestCase
from unittest import main as unittest_run
import math
from disc import Disc, Center


class TestCenter(TestCase):
    def setUp(self):
        self.center = Center(1, 4)

    def test_all(self):
        self.asserEqual(str(self.center), "Center is x=1, y=4")
        self.asserEqual(self.center.x_coord, 1)
        self.asserEqual(self.center.x_coord, 4)


class TestDisc(TestCase):
    def setUp(self) -> None:
        """ create values for testing """
        self.PRECISION = 2
        self.disc1 = Disc(Center(1, 1), 3)
        self.disc2 = Disc(Center(-1, -1), 3)
        self.disc3 = Disc(Center(0, 0), 3)
        self.disc4 = Disc(Center(0, 1), 1)
        self.disc5 = Disc(Center(0, 0), 2)
        self.disc6 = None


    def tast_init(self):
        self.assertEqual(self.disk1, '(x-1.00)**2 + (y-1.00)**2 = 9.00')
        self.assertEqual(self.disk2, '(x+1.00)**2 + (y+1.00)**2 = 9.00')
        self.assertEqual(self.disk2, '(x)**2 + (y)**2 = 9.00')
        self.assertEqual(self.disk1.radius, 3)
        self.assertEqual(self.disk1.center, (1, 1))

    def test_all(self):
        self.assertTrue(self.disc4.is_touching(self.disc5,
                                               precision=self.PRECISION))
        self.assertFalse(self.disc1.is_touching(self.disc2,
                                                precision=self.PRECISION))

        disc2 = Disc(Center(-1, -1), 3)
        (disc5, disc6) = disc2.inscribe_discs()
        self.assertEqual(str(disc5), "(x-3.00)**2 + (y-5.00)**2 = 4.00")
        self.assertEqual(str(disc6), "(x-7.00)**2 + (y-5.00)**2 = 4.00")

        self.assertEqual(str(disc2), "(x-5.00)**2 + (y-5.00)**2 = 36.00")
        disc2.transform_disc(-2)
        self.assertEqual(str(disc2), "(x-5.00)**2 + (y-5.00)**2 = 16.00")
        # Transformed disc is a new object
        disc = disc2.transformed_disc(2)
        self.assertIsinstance(disc, Disc)
        self.assertEqual(str(disc2), "(x-5.00)**2 + (y-5.00)**2 = 16.00")
        self.assertEqual(str(disc), "(x-5.00)**2 + (y-5.00)**2 = 36.00")


if __name__ == '__main__':
    unittest_run()
