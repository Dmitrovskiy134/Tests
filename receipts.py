def solve(receipts: list):
    result = receipts[2::3]  # получите правильный срез списка receipts
    return result, len(result) # этот код менять не нужно

if __name__ == '__main__':
    # Этот код менять не нужно
    result, count = solve([123, 145, 346, 246, 235, 166, 112, 351, 436])
    assert result == [346, 166, 436], f"Список чеков неверный: {result}"
    assert count == 3, f"Количество чеков неверное: {count}"
    print(result)
    print(count)
    result, count = solve([123, 145])
    assert result == [], f"Список чеков неверный: {result}"
    assert count == 0, f"Количество чеков неверное: {count}"
    print(result)
    print(count)