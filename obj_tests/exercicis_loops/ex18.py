#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

pattern_len: int = 5
pattern_cur_len: int = 1
pattern_char: str = '*'
is_done: bool = False

while pattern_cur_len > -1:
    while pattern_cur_len < pattern_len and is_done == False:
        print(f'{pattern_char} ' * pattern_cur_len)
        pattern_cur_len += 1

    is_done = True
    print(f'{pattern_char} ' * pattern_cur_len)
    pattern_cur_len -= 1
