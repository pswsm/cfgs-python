from pathlib import Path
from datetime import date

# -----------------------------------------------------------------------------
# Student name: Pau Figueras Pavón
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Q2: get_class_days()
# - Input:
#   - Start date:  int
#   - End date:    int (INCLUDED!)
#   - Holiday_txt: str. The holidays of December 2021.
# - Output:
#   - class_days: list[int] with all class days in December 2021 between
#                 start and end (included), excluding weekends and holidays.
# 
# - Hint:
#   - You can use the provided function get_weekday().
# 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
#   - You can write additional functions to simplify your algorithm.
# -----------------------------------------------------------------------------


# - Returns the weekday, assuming it is a day of December 2021.
# - 1 = Monday, 2 = Tuesday, ... 7 = Sunday
# - Usage example: get_weekday(1) -> 3  # Wednesday
# -----------------------------------------------------------------------------
def get_weekday(day: int) -> int:

    return date.fromisoformat(f"2021-12-{day:02}").isoweekday()


# - Write your solution here.
# - This function must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def get_class_days(start: int, end: int, holiday_txt: str) -> list[int]:

    class_days: list[int] = []
    holidays: list[str] = holiday_txt.replace("\n", " ").split(" ")

    holidays = list(map(int, holidays))

    for day in range(start, end+1):
        if day not in holidays and (get_weekday(day) == 1 or get_weekday(day) <= 5):
            class_days.append(day)


    return class_days


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Write your solution inside the function.
    # Code here is not evaluated.
    # This is just for your convenience.
    holiday_txt: str = Path("q2_holiday.txt").read_text()
    print(get_class_days(1, 15, holiday_txt))

# -----------------------------------------------------------------------------
