from pathlib import Path

# -----------------------------------------------------------------------------
# Student name: Pau Figueras Pavón
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Q1: get_info()
# - Input: Receives the contents of a text file as a string.
# - Output: Returns three integers
#   - num_lines:   Number of lines in the file
#   - num_words:   Number of words in the file
#   - num_letters: Number of letters in the file, excluding spaces and newlines
#
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------


# - Write your solution here.
# - This function must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def get_info(file_contents: str) -> tuple[int, int, int]:
    
    lines: list[str] = file_contents.split("\n")
    words: list[str] = file_contents.replace("\n", " ").split(" ")
    letters: str = file_contents.replace("\n", " ").replace(" ", "")

    num_lines:   int = len(lines)
    num_words:   int = len(words)
    num_letters: int = len(letters)

    return num_lines, num_words, num_letters


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Write your solution inside the function.
    # Code here is not evaluated.
    # This is just for your convenience.
    file_contents: str = Path("q1_data.txt").read_text()
    print(get_info(file_contents))

# -----------------------------------------------------------------------------

