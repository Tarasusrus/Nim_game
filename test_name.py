# подключаем модуль для автотестов
import unittest

from hello_function import hello


# импортируем функцию из другого файла


# объявляем класс с тестом
class HelloTestCase(unittest.TestCase):
    # функция, которая проверит, как формируется приветствие
    def test_hello(self):
        # отправляем тестовую строку в функцию
        result = hello('тарас')
        # задаем ожидаемый результат
        self.assertEqual(result, 'Привет, Тарас.')


# запускаем тестирование
if __name__ == '__main__':
    unittest.main()
