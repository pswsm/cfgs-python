from pathlib import Path
import q1


# -----------------------------------------------------------------------------
def test_q1():

    # Parameters
    file_contents: str = Path("q1_data.txt").read_text()

    # Get result
    num_lines, num_words, num_letters = q1.get_info(file_contents)

    # Test
    assert num_lines   == 3
    assert num_words   == 6
    assert num_letters == 30

# -----------------------------------------------------------------------------
