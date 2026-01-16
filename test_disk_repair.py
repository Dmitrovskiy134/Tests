import unittest


def solve(models: list, available: list, manufacturers: list):
    repair_count = 0
    ssds = []
    for model, is_available in zip(models, available):
        if is_available == 1 and any(manufacturer in model for manufacturer in manufacturers):
            ssds.append(model)
            repair_count += 1
    return ssds, repair_count


class TestDiskRepairFunction(unittest.TestCase):
    """Юнит-тесты для функции solve"""

    def test_original_case(self):
        """Тестирование оригинального случая из условия задачи"""
        models = [
            '480 ГБ 2.5" SATA накопитель Kingston A400',
            '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
            '480 ГБ 2.5" SATA накопитель ADATA SU650',
            '240 ГБ 2.5" SATA накопитель ADATA SU650',
            '250 ГБ 2.5" SATA накопитель Samsung 870 EVO',
            '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER',
            '480 ГБ 2.5" SATA накопитель WD Green',
            '500 ГБ 2.5" SATA накопитель WD Red SA500'
        ]
        available = [1, 1, 1, 1, 0, 1, 1, 0]
        manufacturers = ['Intel', 'Samsung', 'WD']

        expected_ssds = ['500 ГБ 2.5" SATA накопитель Samsung 870 EVO', '480 ГБ 2.5" SATA накопитель WD Green']
        expected_count = 2

        result_ssds, result_count = solve(models, available, manufacturers)

        self.assertEqual(result_count, expected_count)
        self.assertEqual(result_ssds, expected_ssds)

    def test_all_disks_available_and_suitable(self):
        """Все диски доступны и подходят по производителям"""
        models = [
            '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
            '480 ГБ 2.5" SATA накопитель WD Green'
        ]
        available = [1, 1]
        manufacturers = ['Samsung', 'WD']

        expected_ssds = ['500 ГБ 2.5" SATA накопитель Samsung 870 EVO', '480 ГБ 2.5" SATA накопитель WD Green']
        expected_count = 2

        result_ssds, result_count = solve(models, available, manufacturers)

        self.assertEqual(result_count, expected_count)
        self.assertEqual(result_ssds, expected_ssds)

    def test_no_disks_available(self):
        """Ни один диск не доступен"""
        models = [
            '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
            '480 ГБ 2.5" SATA накопитель WD Green'
        ]
        available = [0, 0]
        manufacturers = ['Samsung', 'WD']

        expected_ssds = []
        expected_count = 0

        result_ssds, result_count = solve(models, available, manufacturers)

        self.assertEqual(result_count, expected_count)
        self.assertEqual(result_ssds, expected_ssds)

    def test_available_but_wrong_manufacturers(self):
        """Диски доступны, но производители не подходят"""
        models = [
            '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
            '480 ГБ 2.5" SATA накопитель Kingston A400'
        ]
        available = [1, 1]
        manufacturers = ['Intel', 'Kingston']

        expected_ssds = ['480 ГБ 2.5" SATA накопитель Kingston A400']
        expected_count = 1

        result_ssds, result_count = solve(models, available, manufacturers)

        self.assertEqual(result_count, expected_count)
        self.assertEqual(result_ssds, expected_ssds)

    def test_manufacturer_in_middle_of_string(self):
        """Производитель в середине строки модели"""
        models = [
            'Накопитель Samsung 500 ГБ',
            'WD Disk 480 ГБ'
        ]
        available = [1, 1]
        manufacturers = ['Samsung', 'WD']

        expected_ssds = ['Накопитель Samsung 500 ГБ', 'WD Disk 480 ГБ']
        expected_count = 2

        result_ssds, result_count = solve(models, available, manufacturers)

        self.assertEqual(result_count, expected_count)
        self.assertEqual(result_ssds, expected_ssds)

    def test_lowercase_manufacturer_in_model(self):
        """Производитель с маленькой буквы в модели (не должен находиться)"""
        models = [
            '500 ГБ samsung evo',
            '480 ГБ wd green'
        ]
        available = [1, 1]
        manufacturers = ['Samsung', 'WD']

        expected_ssds = []
        expected_count = 0

        result_ssds, result_count = solve(models, available, manufacturers)

        self.assertEqual(result_count, expected_count)
        self.assertEqual(result_ssds, expected_ssds)

    def test_empty_lists(self):
        """Пустые списки входных данных"""
        models = []
        available = []
        manufacturers = ['Samsung', 'WD']

        expected_ssds = []
        expected_count = 0

        result_ssds, result_count = solve(models, available, manufacturers)

        self.assertEqual(result_count, expected_count)
        self.assertEqual(result_ssds, expected_ssds)

    def test_different_availability_for_same_manufacturer(self):
        """Разная доступность для одного производителя"""
        models = [
            'Samsung SSD 500GB',
            'Samsung SSD 250GB',
            'Samsung SSD 1TB'
        ]
        available = [1, 0, 1]
        manufacturers = ['Samsung']

        expected_ssds = ['Samsung SSD 500GB', 'Samsung SSD 1TB']
        expected_count = 2

        result_ssds, result_count = solve(models, available, manufacturers)

        self.assertEqual(result_count, expected_count)
        self.assertEqual(result_ssds, expected_ssds)

    def test_intel_manufacturer_present(self):
        """Производитель Intel в списке (но нет в моделях в оригинальном случае)"""
        models = [
            'Intel SSD 500GB',
            'Kingston SSD 480GB'
        ]
        available = [1, 1]
        manufacturers = ['Intel', 'Kingston']

        expected_ssds = ['Intel SSD 500GB', 'Kingston SSD 480GB']
        expected_count = 2

        result_ssds, result_count = solve(models, available, manufacturers)

        self.assertEqual(result_count, expected_count)
        self.assertEqual(result_ssds, expected_ssds)

    def test_partial_manufacturer_match(self):
        """Частичное совпадение названия производителя"""
        models = [
            'SSD Samsung Pro',
            'SSD Samsungung Basic'  # Содержит "Samsung" как часть строки
        ]
        available = [1, 1]
        manufacturers = ['Samsung']

        expected_ssds = ['SSD Samsung Pro', 'SSD Samsungung Basic']
        expected_count = 2

        result_ssds, result_count = solve(models, available, manufacturers)

        self.assertEqual(result_count, expected_count)
        self.assertEqual(result_ssds, expected_ssds)

    def test_return_type_correct(self):
        """Проверка типа возвращаемого значения"""
        models = ['Samsung SSD']
        available = [1]
        manufacturers = ['Samsung']

        result = solve(models, available, manufacturers)

        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[1], int)

    def test_mismatched_lengths(self):
        """Разная длина списков models и available"""
        models = ['Samsung SSD', 'WD SSD']
        available = [1]  # Только одно значение доступности
        manufacturers = ['Samsung', 'WD']

        # Ожидаем, что функция обработает только первые min(len(models), len(available)) элементов
        result_ssds, result_count = solve(models, available, manufacturers)

        # Проверяем, что обработан только первый диск
        self.assertEqual(result_count, 1)
        self.assertEqual(result_ssds, ['Samsung SSD'])

    def test_zero_availability_not_one(self):
        """Проверка, что функция работает только с available == 1"""
        models = ['Samsung SSD', 'WD SSD']
        available = [2, -1]  # Не 1, но и не 0
        manufacturers = ['Samsung', 'WD']

        result_ssds, result_count = solve(models, available, manufacturers)

        self.assertEqual(result_count, 0)
        self.assertEqual(result_ssds, [])


# Параметризация с использованием подхода unittest
def create_test_case(models, available, manufacturers, expected_ssds, expected_count):
    """Фабрика для создания тестовых случаев"""

    def test(self):
        result_ssds, result_count = solve(models, available, manufacturers)
        self.assertEqual(result_count, expected_count)
        self.assertEqual(result_ssds, expected_ssds)

    return test


# Динамическое добавление параметризованных тестов
test_data = [
    (
        ["Kingston SSD", "Samsung SSD", "WD SSD"],
        [1, 1, 0],
        ["Samsung"],
        ["Samsung SSD"],
        1
    ),
    (
        ["Intel SSD", "AMD SSD"],
        [1, 1],
        ["Intel"],
        ["Intel SSD"],
        1
    ),
    (
        ["SSD 1", "SSD 2"],
        [0, 0],
        ["Manufacturer"],
        [],
        0
    ),
]

for i, (models, available, manufacturers, expected_ssds, expected_count) in enumerate(test_data):
    test_name = f'test_parametrized_case_{i + 1}'
    test_func = create_test_case(models, available, manufacturers, expected_ssds, expected_count)
    setattr(TestDiskRepairFunction, test_name, test_func)

if __name__ == '__main__':
    # Запуск юнит-тестов
    unittest.main(verbosity=2)

    # Демонстрация работы оригинального случая
    print("\n" + "=" * 60)
    print("Демонстрация оригинального случая:")
    print("=" * 60)
    models = [
        '480 ГБ 2.5" SATA накопитель Kingston A400',
        '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
        '480 ГБ 2.5" SATA накопитель ADATA SU650',
        '240 ГБ 2.5" SATA накопитель ADATA SU650',
        '250 ГБ 2.5" SATA накопитель Samsung 870 EVO',
        '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER',
        '480 ГБ 2.5" SATA накопитель WD Green',
        '500 ГБ 2.5" SATA накопитель WD Red SA500'
    ]
    available = [1, 1, 1, 1, 0, 1, 1, 0]
    manufacturers = ['Intel', 'Samsung', 'WD']

    result = solve(models, available, manufacturers)
    print(f"Сисадмин Василий сможет купить диски: {result[0]} и починить {result[1]} компьютера")