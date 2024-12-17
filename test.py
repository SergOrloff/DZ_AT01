import unittest
import logging
from main import add, subtract, multiply, divide, check, modulo

# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("test.log"),
                        logging.StreamHandler()
                    ]
                    )
logger = logging.getLogger(__name__)
logger.info("Testing started...")


# Базовый класс для тестов с логированием
class BaseTest(unittest.TestCase):
    def setUp(self):
        logging.info('Starting test: %s', self._testMethodName)

    def tearDown(self):
        logging.info('Finished test: %s', self._testMethodName)


class TestMath(BaseTest):
    def test_add(self):
        """Тест функции add: проверка сложения"""
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)
        self.assertEqual(add(-3, 7), 4)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, -5), -10)

    def test_subtract(self):
        """Тест функции subtract: проверка вычитания"""
        self.assertEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)
        self.assertEqual(subtract(-3, -7), 4)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(5, 0), 5)

    def test_multiply(self):
        """Тест функции multiply: проверка умножения"""
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)
        self.assertEqual(multiply(-3, 6), -18)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-4, -5), 20)

    def test_divide(self):
        """Тест функции divide: проверка деления"""
        self.assertNotEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)
        self.assertEqual(divide(-15, 3), -5)
        self.assertEqual(divide(5, -1), -5)
        self.assertEqual(divide(0, 5), 0)

    def test_divide_success(self):
        """Тест функции divide: успешное деление"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)
        self.assertEqual(divide(7.5, 2.5), 3.0)

    def test_divide_by_zero(self):
        """Тест функции divide: деление на ноль"""
        with self.assertRaises(ValueError):
            divide(6, 0)

    def test_modulo(self):
        """Тест функции modulo: проверка остатка от деления"""
        self.assertEqual(modulo(10, 3), 2)
        self.assertEqual(modulo(20, 5), 0)
        self.assertEqual(modulo(7, 4), 3)
        self.assertEqual(modulo(-10, 3), 2)
        self.assertEqual(modulo(10, -3), -2)

    def test_modulo_by_zero(self):
        """Тест функции modulo: деление на ноль"""
        with self.assertRaises(ValueError):
            modulo(10, 0)


class TestCheck(BaseTest):
    def test_check_true(self):
        """Тест функции check: проверка на чётность (должно быть True)"""
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertTrue(check(220))
        self.assertTrue(check(0))
        self.assertTrue(check(-4))

    def test_check_false(self):
        """Тест функции check: проверка на чётность (должно быть False)"""
        self.assertFalse(check(1))
        self.assertFalse(check(3))
        self.assertFalse(check(57))
        self.assertFalse(check(-5))


def run_tests():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMath))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCheck))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    unittest.main()
