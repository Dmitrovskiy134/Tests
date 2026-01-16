# test_vote.py - Unit-тесты для задачи "Поиск победителя голосования"
import unittest


def vote(votes):
    """Функция для задачи 3: Поиск победителя голосования"""
    vote_count = {}
    for num in votes:
        if num in vote_count:
            vote_count[num] += 1
        else:
            vote_count[num] = 1
    winner = None
    max_votes = 0
    for num, count in vote_count.items():
        if count > max_votes:
            max_votes = count
            winner = num
    return winner


class TestVoteFunction(unittest.TestCase):
    """Юнит-тесты для функции vote (поиск победителя голосования)"""

    def test_original_case_1(self):
        """Тестирование оригинального случая 1 из условия: [1,1,1,2,3]"""
        votes = [1, 1, 1, 2, 3]
        expected_winner = 1

        result = vote(votes)

        self.assertEqual(result, expected_winner,
                         f"Для списка {votes} ожидался победитель {expected_winner}, получен {result}")

    def test_original_case_2(self):
        """Тестирование оригинального случая 2 из условия: [1,2,3,2,2]"""
        votes = [1, 2, 3, 2, 2]
        expected_winner = 2

        result = vote(votes)

        self.assertEqual(result, expected_winner,
                         f"Для списка {votes} ожидался победитель {expected_winner}, получен {result}")

    def test_single_vote(self):
        """Тест с одним голосом"""
        votes = [5]
        expected_winner = 5

        result = vote(votes)

        self.assertEqual(result, expected_winner)

    def test_all_votes_equal(self):
        """Тест: все кандидаты получили одинаковое количество голосов (ничья)"""
        votes = [1, 2, 3]
        # В случае ничьей возвращается первый кандидат с максимальным количеством голосов
        expected_winner = 1

        result = vote(votes)

        self.assertEqual(result, expected_winner)

    def test_tie_with_multiple_max(self):
        """Тест: несколько кандидатов имеют одинаковое максимальное количество голосов"""
        votes = [2, 2, 1, 1]
        # Оба имеют по 2 голоса, но 2 встречается первым
        expected_winner = 2

        result = vote(votes)

        self.assertEqual(result, expected_winner)

    def test_negative_numbers(self):
        """Тест с отрицательными числами в голосах"""
        votes = [-1, -1, -2, -2, -2, -3]
        expected_winner = -2

        result = vote(votes)

        self.assertEqual(result, expected_winner)

    def test_zero_votes(self):
        """Тест с нулями в голосах"""
        votes = [0, 0, 0, 1, 1]
        expected_winner = 0

        result = vote(votes)

        self.assertEqual(result, expected_winner)

    def test_large_numbers(self):
        """Тест с большими числами"""
        votes = [1000, 1000, 2000, 2000, 2000, 3000]
        expected_winner = 2000

        result = vote(votes)

        self.assertEqual(result, expected_winner)

    def test_string_votes(self):
        """Тест: голоса в виде строк (функция должна работать с любыми хешируемыми типами)"""
        votes = ['A', 'A', 'B', 'C', 'C', 'C']
        expected_winner = 'C'

        result = vote(votes)

        self.assertEqual(result, expected_winner)

    def test_empty_list(self):
        """Тест: пустой список голосов"""
        votes = []
        # Для пустого списка должен возвращаться None
        result = vote(votes)

        self.assertIsNone(result, "Для пустого списка должен возвращаться None")

    def test_floats(self):
        """Тест с числами с плавающей точкой"""
        votes = [1.5, 1.5, 2.0, 2.0, 2.0]
        expected_winner = 2.0

        result = vote(votes)

        self.assertEqual(result, expected_winner)

    def test_boolean_values(self):
        """Тест с булевыми значениями"""
        votes = [True, True, False, False, False]
        expected_winner = False

        result = vote(votes)

        self.assertEqual(result, expected_winner)

    def test_mixed_types_not_recommended(self):
        """Тест со смешанными типами (не рекомендуется, но функция может обработать)"""
        votes = [1, '1', 1]  # 1 (число) и '1' (строка) - разные значения
        expected_winner = 1  # Число 1 встречается 2 раза, строка '1' - 1 раз

        result = vote(votes)

        self.assertEqual(result, expected_winner)

    def test_long_list(self):
        """Тест с длинным списком голосов"""
        votes = [1] * 10 + [2] * 5 + [3] * 8  # 1:10 голосов, 2:5 голосов, 3:8 голосов
        expected_winner = 1

        result = vote(votes)

        self.assertEqual(result, expected_winner)

    def test_return_type(self):
        """Проверка типа возвращаемого значения"""
        votes = [1, 2, 2]
        result = vote(votes)

        # Проверяем, что результат соответствует типу элементов списка
        self.assertIsInstance(result, int)

    def test_identical_elements(self):
        """Тест: все элементы одинаковые"""
        votes = [7, 7, 7, 7, 7]
        expected_winner = 7

        result = vote(votes)

        self.assertEqual(result, expected_winner)


# Параметризация с использованием подхода unittest
def create_vote_test(votes, expected_winner, description=""):
    """Фабрика для создания параметризованных тестов"""

    def test(self):
        result = vote(votes)
        self.assertEqual(result, expected_winner,
                         f"{description}: для {votes} ожидался {expected_winner}, получен {result}")

    return test


# Динамическое добавление параметризованных тестов
vote_test_data = [
    # (votes, expected_winner, description)
    ([5, 5, 5, 3, 3], 5, "Очевидный победитель"),
    ([10, 20, 10, 20, 10], 10, "Два кандидата, победитель 10"),
    ([7, 8, 9], 7, "Три кандидата с ничьей (возвращается первый)"),
    ([42], 42, "Один голос"),
    ([6, 6, 6, 6], 6, "Все голоса одинаковые"),
    ([1, 2, 1, 2, 3, 3, 3], 3, "Три кандидата, победитель 3"),
    ([-5, -5, -10], -5, "Отрицательные числа"),
    ([0, 1, 0, 1, 0], 0, "С нулями"),
    ([1.5, 1.5, 2.0], 1.5, "Числа с плавающей точкой"),
    (['x', 'y', 'x', 'x', 'y'], 'x', "Строки"),
    ([True, False, True], True, "Булевы значения"),
    ([], None, "Пустой список"),
    ([100, 200, 100, 300, 300, 300], 300, "Большие числа"),
    ([1, 1, 2, 2, 3, 3, 4, 4, 4], 4, "Несколько кандидатов"),
    ([7, 7, 8, 8, 9, 9, 9], 9, "Победитель с перевесом в 1 голос"),
]

# Добавляем параметризованные тесты в класс
for i, (votes, expected_winner, description) in enumerate(vote_test_data):
    test_name = f'test_vote_parametrized_{i + 1}_{description.replace(" ", "_")}'
    test_func = create_vote_test(votes, expected_winner, description)
    setattr(TestVoteFunction, test_name, test_func)


# Функция для запуска тестов с красивым выводом
def run_vote_tests():
    """Запуск тестов для функции vote с кастомным отчетом"""
    print("=" * 70)
    print("UNIT-ТЕСТЫ ДЛЯ ЗАДАЧИ 'ПОИСК ПОБЕДИТЕЛЯ ГОЛОСОВАНИЯ'")
    print("=" * 70)
    print("\nОписание задачи:")
    print("Функция vote(votes) принимает список голосов и возвращает")
    print("значение, которое встречается наибольшее количество раз.")
    print("В случае ничьей возвращается первый такой элемент.")
    print("\n" + "=" * 70)

    # Создаем тестовый набор
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestVoteFunction)

    # Считаем тесты
    test_count = suite.countTestCases()

    print(f"Всего тестов: {test_count}")
    print(
        f"- Явные тесты: {len([m for m in dir(TestVoteFunction) if m.startswith('test_') and not m.startswith('test_vote_parametrized')])}")
    print(
        f"- Параметризованные тесты: {len([m for m in dir(TestVoteFunction) if m.startswith('test_vote_parametrized')])}")
    print("\n" + "=" * 70)
    print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ:")
    print("=" * 70)

    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Статистика
    print("\n" + "=" * 70)
    print("СТАТИСТИКА:")
    print("=" * 70)
    print(f"Всего тестов: {result.testsRun}")
    print(f"Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Провалено: {len(result.failures)}")
    print(f"Ошибок: {len(result.errors)}")

    # Демонстрационные примеры
    if result.wasSuccessful():
        print("\n" + "=" * 70)
        print("ДЕМОНСТРАЦИЯ РАБОТЫ ФУНКЦИИ:")
        print("=" * 70)

        demo_cases = [
            ([1, 1, 1, 2, 3], "Оригинальный случай 1"),
            ([1, 2, 3, 2, 2], "Оригинальный случай 2"),
            ([5, 5, 3, 3, 3, 5, 5], "Несколько кандидатов"),
            ([], "Пустой список"),
            (['apple', 'banana', 'apple', 'orange'], "Строковые значения"),
        ]

        for votes, description in demo_cases:
            result = vote(votes)
            print(f"\n{description}:")
            print(f"  Входные данные: {votes}")
            print(f"  Победитель: {result}")
            if votes:
                # Показываем подсчет голосов для наглядности
                from collections import Counter
                counts = Counter(votes)
                print(f"  Распределение голосов: {dict(counts)}")

    return result


if __name__ == '__main__':
    # Можно запускать двумя способами:

    # Способ 1: С кастомным отчетом
    run_vote_tests()

    # Способ 2: Стандартный запуск unittest
    # unittest.main(verbosity=2)