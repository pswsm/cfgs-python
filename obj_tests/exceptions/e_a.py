def main(a) -> None:
    try:
        int(a)
    except:
        print(f"{a} is not an integer.\n")

    print(f"{a} is an integer")

if __name__ == "__main__":
    an_int: str = input(f"Write an integer:\t")
    main(an_int)
