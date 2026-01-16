def solve(models: list, available: list, manufacturers: list):
    repair_count = 0 # количество дисков, которые купит сисадмин
    ssds = [] # модели дисков из списка models, которые купит сисадмин
    # код вашего решения ниже:
    for model, is_available in zip(models, available):
        if is_available == 1 and any(manufacturer in model for manufacturer in manufacturers):
            ssds.append(model)
            repair_count += 1
    
    return ssds, repair_count # Этот код менять не нужно

if __name__ == '__main__':
    # Этот код менять не нужно
    models = ['480 ГБ 2.5" SATA накопитель Kingston A400', '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
              '480 ГБ 2.5" SATA накопитель ADATA SU650', '240 ГБ 2.5" SATA накопитель ADATA SU650',
              '250 ГБ 2.5" SATA накопитель Samsung 870 EVO', '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER',
              '480 ГБ 2.5" SATA накопитель WD Green', '500 ГБ 2.5" SATA накопитель WD Red SA500']
    available = [1, 1, 1, 1, 0, 1, 1, 0]
    manufacturers = ['Intel', 'Samsung', 'WD']

    result = solve(models, available, manufacturers)
    assert result == (['500 ГБ 2.5" SATA накопитель Samsung 870 EVO', '480 ГБ 2.5" SATA накопитель WD Green'], 2), \
        f"Неверный результат: {result}"
    print(f"Сисадмин Василий сможет купить диски: {result[0]} и починить {result[1]} компьютера")
