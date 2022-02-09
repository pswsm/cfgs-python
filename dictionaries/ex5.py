# @Author: Pau Figueras <pswsm>
# @Date:   2022-02-09T19:50:38+01:00
# @Email:  pau@pswsm.cat
# @Last modified by:   pswsm
# @Last modified time: 2022-02-09T20:33:46+01:00
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", 'city', "salary"]


def mkDictFromDict(ogDict, keysToExtract: list[str]) -> dict:
    result = {}
    for key in keysToExtract:
        result[key] = ogDict[key]
    return result


print(mkDictFromDict(sample_dict, keys))
