"""Exercise 1 - Module 5"""


def main(costat_1: float, costat_2: float, costat_3: float):
    """Returns the triangle based on the sides given"""
    if not all([isinstance(costat_1, int), isinstance(costat_2, int), isinstance(costat_3, int)])or all([isinstance(costat_1, float), isinstance(costat_2, float), isinstance(costat_3, float)]):
        raise Exception("Passed non-numerical parameters!")

    grt: float = costat_1
    if costat_2 > grt:
        grt = costat_2

    if costat_3 > grt:
        grt = costat_3

    suma: float = (costat_1 + costat_2 + costat_3) - grt

    if suma > grt:
        if (costat_1 == costat_2) and (costat_2 == costat_3):
            return "Triangle Equilàter"
        if (costat_1 == costat_2) or (costat_1 == costat_3) or (costat_2 == costat_3):
            return "Triangle isósceles"
        return "Triangle Rectangle"
    return "No és un triangle"


if __name__ == "__main__":
    print(main(10, 10, 10))
