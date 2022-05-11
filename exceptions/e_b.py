def check_seq(a) -> None:
    if not len(a) % 3 == 0:
        print("Not triplets")


if __name__ == "__main__":
    seq: str = input(f"Input a sequence:\n")
    check_seq(seq)
