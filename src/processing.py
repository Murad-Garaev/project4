from typing import Any


def filter_by_state(dictionary_inform: list[dict[str, Any]], state_id: str = 'EXECUTED') -> list[dict[str, Any]]:
    '''Функция фильтрующая данные по указанному параметру'''

    list_state = []
    for key in dictionary_inform:
        if key.get('state') == state_id:
            list_state.append(key)
    return list_state


def sort_by_date(dictionary_inform: list[dict[str, Any]], revers: bool = True) -> list[dict[str, Any]]:
    '''Функция сортировки словарей по дате'''
    sorted_inform_state = sorted(dictionary_inform, key=lambda x: ['date'], reverse=revers)

    return sorted_inform_state
