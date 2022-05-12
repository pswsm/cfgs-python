# @Author: pswsm
# @Date:   2022-02-09T19:13:09+01:00
# @Last modified by:   pswsm
# @Last modified time: 2022-02-09T19:39:44+01:00

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


def mergeDict(*argv) -> dict:
    merged: dict = {}
    for dictionary in argv:
        merged |= dictionary
    return merged


print(mergeDict(dict1, dict2))
