from pathlib import Path
import q3


# -----------------------------------------------------------------------------
def test_q3():

    # Parameters
    coronavirus_fasta: str = Path("q3_coronavirus.fasta").read_text()

    # Get result
    indexes: list[int] = q3.get_indexes("AAA", coronavirus_fasta)

    # Test
    assert indexes == [3, 28, 67, 78, 79]


# -----------------------------------------------------------------------------
