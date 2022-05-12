# @Author: Pau Figueras <pswsm>
# @Date:   2022-02-09T19:24:01+01:00
# @Email:  pau@pswsm.cat
# @Last modified by:   pswsm
# @Last modified time: 2022-02-09T19:29:14+01:00
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}


def getValue(key: str, dictionary: dict):
    result = dictionary.get(key, 'not found')
    return result


print(getValue('history', sampleDict))
