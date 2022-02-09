# @Author: Pau Figueras <pswsm>
# @Date:   2022-02-09T19:33:13+01:00
# @Email:  pau@pswsm.cat
# @Last modified by:   pswsm
# @Last modified time: 2022-02-09T19:47:56+01:00
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}


def mkDictDefault(keys, defaults) -> dict:
    return dict.fromkeys(employees, defaults)


print(mkDictDefault(employees, defaults))
