from pathlib import Path
import q2


# -----------------------------------------------------------------------------
def test_q2():

    # Parameters
    holiday_txt: str = Path("q2_holiday.txt").read_text()

    # Get result
    class_days: list[int] = q2.get_class_days(1, 15, holiday_txt)

    # Test
    assert class_days == [1, 2, 3, 9, 10, 13, 14, 15]

# -----------------------------------------------------------------------------
