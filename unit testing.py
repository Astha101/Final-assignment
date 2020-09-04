import unittest

from epm import Product


class MyTest(unittest.TestCase):

    def test_add_product(self):
        a = Product()
        # actual_result = b.add_product('id', 'type', 'name', 'price', 'qty', 'payment method', 'delivery to')
        actual_result = a.add_product('11', 'Essential', 'Towel', '700', '2', 'cash on delivery', 'Kapan')
        self.assertTrue(actual_result)


    def test_fetch_data(self):
        c = Product()
        actual_result = c.fetch_data()
        self.assertTrue(actual_result)

    def test_login_function(self):
        d = Product()
        actual_result = d.login_function('q', 'q')
        self.assertTrue(len(actual_result), 1)

    def test_register_data(self):
        e = Product()
        actual_result = e.register_data('a', 'b', '980256709', 'melol@gmail.com', 'shopping')
        self.assertTrue(actual_result)

    def test_delete_data(self):
        e = Product()
        actual_result = e.delete_data('1')
        self.assertTrue(actual_result)


