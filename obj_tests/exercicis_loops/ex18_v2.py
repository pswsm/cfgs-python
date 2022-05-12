#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

def mk_pattern(char: str = "*", length: int = 5) -> str:
    pattern_cur_len: int = 1
    is_done: bool = False
    to_print: str = ""

    while pattern_cur_len > -1:
        while pattern_cur_len < length and is_done == False:
            to_print += (f'{char} ' * pattern_cur_len)
            pattern_cur_len += 1

        is_done = True
    to_print += (f'{char} ' * pattern_cur_len)
    pattern_cur_len -= 1

    return to_print

print(mk_pattern)
