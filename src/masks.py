def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты.
    Принимает строку с номером карты (16 цифр, могут быть пробелы)
    и возвращает маскированный номер в формате XXXX XX** **** XXXX.
    """
    # Удаляем все пробелы на случай, если они переданы в номере
    clean_number = card_number.replace(" ", "")
    if len(clean_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Маскируем цифры с 7 по 12 включительно (индексы с 6 по 11)
    masked_part = clean_number[:6] + "** ****" + clean_number[12:]

    # Форматируем строку группами по 4 символа для красивого отображения
    formatted_number = f"{masked_part[:4]} {masked_part[4:8]} {masked_part[8:12]} {masked_part[12:]}"
    return formatted_number


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета.
    Принимает строку с номером счета и возвращает маскированный номер
    в формате **XXXX (видны только последние 4 цифры).
    """
    clean_number = account_number.replace(" ", "")
    if len(clean_number) <= 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    # Берем последние 4 цифры и добавляем звездочки в начале
    masked_account = f"**{clean_number[-4:]}"
    return masked_account
