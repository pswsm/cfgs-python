# @Author: Pau Figueras <pswsm>
# @Date:   2022-02-09T19:05:59+01:00
# @Email:  pau@pswsm.cat
# @Last modified by:   pswsm
# @Last modified time: 2022-02-09T19:37:09+01:00

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


def mkDict(key: list, value: list) -> dict:
    result: dict[str, int] = {k: v for k, v in zip(keys, values)}
    return result


print(mkDict(keys, values))
