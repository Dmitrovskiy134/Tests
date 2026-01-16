import unittest

def solve(receipts: list):
    result = receipts[2::3]  # получите правильный срез списка receipts
    return result, len(result) # этот код менять не нужно


class TestReceiptsSliceFunction(unittest.TestCase):
    """Тесты для задачи с чеками (каждый третий элемент, начиная с третьего)"""
    
    def test_original_case_1(self):
        """Тестирование оригинального случая из условия"""
        receipts = [123, 145, 346, 246, 235, 166, 112, 351, 436]
        expected_result = [346, 166, 436]
        expected_count = 3
        
        result, count = solve(receipts)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(count, expected_count)
    
    def test_original_case_2(self):
        """Тестирование второго случая из условия (мало элементов)"""
        receipts = [123, 145]
        expected_result = []
        expected_count = 0
        
        result, count = solve(receipts)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(count, expected_count)
    
    def test_exactly_three_elements(self):
        """Ровно 3 элемента - должен вернуть только третий"""
        receipts = [100, 200, 300]
        expected_result = [300]
        expected_count = 1
        
        result, count = solve(receipts)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(count, expected_count)
    
    def test_exactly_four_elements(self):
        """4 элемента - должен вернуть только третий"""
        receipts = [100, 200, 300, 400]
        expected_result = [300]
        expected_count = 1
        
        result, count = solve(receipts)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(count, expected_count)
    
    def test_exactly_five_elements(self):
        """5 элементов - должен вернуть только третий"""
        receipts = [100, 200, 300, 400, 500]
        expected_result = [300]
        expected_count = 1
        
        result, count = solve(receipts)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(count, expected_count)
    
    def test_exactly_six_elements(self):
        """6 элементов - должен вернуть третий и шестой"""
        receipts = [100, 200, 300, 400, 500, 600]
        expected_result = [300, 600]
        expected_count = 2
        
        result, count = solve(receipts)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(count, expected_count)
    
    def test_large_list(self):
        """Большой список из 15 элементов"""
        receipts = list(range(1, 16))  # [1, 2, 3, ..., 15]
        expected_result = [3, 6, 9, 12, 15]
        expected_count = 5
        
        result, count = solve(receipts)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(count, expected_count)
    
    def test_empty_list(self):
        """Пустой список"""
        receipts = []
        expected_result = []
        expected_count = 0
        
        result, count = solve(receipts)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(count, expected_count)
    
    def test_single_element(self):
        """Один элемент"""
        receipts = [999]
        expected_result = []
        expected_count = 0
        
        result, count = solve(receipts)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(count, expected_count)
    
    def test_two_elements(self):
        """Два элемента"""
        receipts = [111, 222]
        expected_result = []
        expected_count = 0
        
        result, count = solve(receipts)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(count, expected_count)
    
    def test_negative_numbers(self):
        """Список с отрицательными числами"""
        receipts = [-100, -200, -300, -400, -500]
        expected_result = [-300]
        expected_count = 1
        
        result, count = solve(receipts)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(count, expected_count)
    
    def test_mixed_numbers(self):
        """Список со смешанными числами (положительные, отрицательные, нули)"""
        receipts = [-10, 0, 10, -20, 0, 20]
        expected_result = [10, 20]
        expected_count = 2
        
        result, count = solve(receipts)
        
        self.assertEqual(result, expected_result)
        self.assertEqual(count, expected_count)
    
    def test_return_type_correct(self):
        """Проверка типа возвращаемого значения"""
        receipts = [1, 2, 3]
        result, count = solve(receipts)
        
        self.assertIsInstance(result, list)
        self.assertIsInstance(count, int)
        self.assertEqual(len(result), count)
    
    def test_original_code_works(self):
        """Проверка, что оригинальный код из условия работает"""
        # Тест из условия 1
        result, count = solve([123, 145, 346, 246, 235, 166, 112, 351, 436])
        self.assertEqual(result, [346, 166, 436])
        self.assertEqual(count, 3)
        
        # Тест из условия 2
        result, count = solve([123, 145])
        self.assertEqual(result, [])
        self.assertEqual(count, 0)


# Параметризация с использованием подхода unittest
def create_receipts_test(receipts, expected_result, expected_count):
    """Фабрика для создания параметризованных тестов"""
    def test(self):
        result, count = solve(receipts)
        self.assertEqual(result, expected_result)
        self.assertEqual(count, expected_count)
    return test


# Динамическое добавление параметризованных тестов
receipts_test_data = [
    # (receipts, expected_result, expected_count)
    ([10, 20, 30, 40, 50, 60, 70, 80, 90], [30, 60, 90], 3),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [3, 6, 9, 12], 4),
    ([1000], [], 0),
    ([], [], 0),
    ([1, 2], [], 0),
    ([1, 2, 3, 4], [3], 1),
    ([1, 2, 3, 4, 5, 6], [3, 6], 2),
    ([0, 0, 0, 0, 0, 0], [0, 0], 2),
    ([-5, -4, -3, -2, -1], [-3], 1),
    ([100, 200, 300, 400, 500, 600, 700], [300, 600], 2),
]

for i, (receipts, expected_result, expected_count) in enumerate(receipts_test_data):
    test_name = f'test_receipts_parametrized_{i+1}'
    test_func = create_receipts_test(receipts, expected_result, expected_count)
    setattr(TestReceiptsSliceFunction, test_name, test_func)


if __name__ == '__main__':
    # Запуск только тестов для этой задачи
    unittest.main(verbosity=2)
    
    # Демонстрация работы
    print("\n" + "="*60)
    print("Демонстрация работы функции solve для задачи с чеками:")
    print("="*60)
    
    test_cases = [
        [123, 145, 346, 246, 235, 166, 112, 351, 436],
        [123, 145],
        [1, 2, 3, 4, 5],
        list(range(1, 10))
    ]
    
    for receipts in test_cases:
        result, count = solve(receipts)
        print(f"receipts = {receipts}")
        print(f"result = {result}, count = {count}")
        print("-" * 40)