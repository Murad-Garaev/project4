def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    return f"{card_number[0: 4]} {card_number[4: 6]}** **** {card_number[-4:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция маскировки номера счета"""
    return f"**{mask_account[-4:]}"


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
