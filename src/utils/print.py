from typing import List, Tuple


def max_row_len(list: List[Tuple]) -> int:
    max_len = 0
    for tuple in list:
        new_tuple = (str(e) for e in tuple)
        local_max_len = len(max(new_tuple, key=len))
        if max_len < local_max_len:
            max_len = local_max_len

    return max_len


def print_rows(list: List[Tuple], label: str = ""):
    print(label)
    row_len = max_row_len(list)
    for tuple in list:
        print("| ", end="")
        for e in tuple:
            print(f"{str(e):^{row_len + 4}} |", end="")
        print()
