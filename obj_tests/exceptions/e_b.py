def check_seq(a) -> None:
    if not len(a) % 3 == 0:
        raise Exception

if __name__ == "__main__":
    seq: str = input(f"Input a sequence:\n")
    try:
        check_seq(seq)
    except:
        print(f"Not triplets")
