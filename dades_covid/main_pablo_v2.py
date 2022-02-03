from pathlib import Path

# 1. Read csv file
# -----------------------------------------------------------------------------
def read_csv(csv_file_path: str) -> str:
   '''Input:  The path to a .csv file.
      Output: The contents of the .csv file as a single string.'''

   raw_text:      str = Path(csv_file_path).read_text()
   stripped_text: str = raw_text.strip()

   return stripped_text


# 2. Separate by rows
# -----------------------------------------------------------------------------
def separate_by_rows(contents: str) -> list[str]:
   '''Input:  The file contents as a single string.
      Output: A list of strings where each string is a row of the csv file.'''
   
   rows: list[str] = contents.split("\n")

   return rows


# 3. Separate by columns
# -----------------------------------------------------------------------------
def separate_by_columns(rows: list[str]) -> list[list[str]]:
   '''Input:  A list of strings. Each string is a row of a csv file. Row fields are separated by ";".
      Output: A table where each row has been splitted into a list of fields.'''
   
   table: list[list[str]] = []
   row:   str

   for row in rows:
      splitted_row: list[str] = row.split(";")
      table.append(splitted_row)

   return table


# 4. Get Covid Shots
# -----------------------------------------------------------------------------
def get_covid_shots(table: list[list[str]]) -> tuple[list[int], list[int]]:
   '''Input:  A table with Covid Data. Each datum is a string.
      Output: The data of two columns as ints: "dosi_1" and "dosi_2"'''
   
   header:     list[str]       = table[0]
   covid_data: list[list[str]] = table[1:]
   row:        list[str]
   row_bcn:    list[str]

   comarca_field_index: int = header.index("NOM")
   dosi1_field_index:   int = header.index("VACUNATS_DOSI_1")
   dosi2_field_index:   int = header.index("VACUNATS_DOSI_2")

   dosi1_list: list[int] = []
   dosi2_list: list[int] = []
   bcn_list:   list[str] = []


   for row_bcn in covid_data:
       bcn_cmc: str = row_bcn[comarca_field_index]
       if "BARCELONA" in bcn_cmc:
           bcn_list.append(row_bcn)

   for row in bcn_list:
      dosi1_str: str = row[dosi1_field_index]
      dosi1_int: int = int(dosi1_str)
      dosi1_list.append(dosi1_int)

      dosi2_str: str = row[dosi2_field_index]
      dosi2_int: int = int(dosi2_str)
      dosi2_list.append(dosi2_int)

   return dosi1_list, dosi2_list


# 5. Sum Shots
# -----------------------------------------------------------------------------
def sum_shots(dosi1_list: list[int], dosi2_list: list[int]) -> tuple[int, int, int]:
   '''Input: A list of two columns: dosi_1 and dosi_2.
      Output: The sum of dosi_1, the sum of dosi_2 and the sum of both.'''

   dosi1_sum: int = sum(dosi1_list)
   dosi2_sum: int = sum(dosi2_list)
   total_sum: int = dosi1_sum + dosi2_sum

   return dosi1_sum, dosi2_sum, total_sum

def pct_shots(dosi1: int, dosi2: int, total: int) -> tuple[float, float]:
    '''Input: Total shots given, total 1st and 2nd shots given
       Output: Percentage of people who have gotten the 2nd shot, and dif'''

    only1_shot: int = dosi2 - dosi1
    only1_shot_pct: float = only1_shot * 100 / total
    only2_shot_pct: float = 100 - only1_shot_pct

    return only1_shot_pct, only2_shot_pct


# Main
# -----------------------------------------------------------------------------
contents: str                   = read_csv("/home/pswsm/github/cfgs-python/dades_covid/2022-01-20-covid-dades-aga/2022-01-20-covid-dades-aga.csv")
rows:     list[str]             = separate_by_rows(contents)
table:    list[list[str]]       = separate_by_columns(rows)
dosi1_list, dosi2_list          = get_covid_shots(table)
dosi1_sum, dosi2_sum, total_sum = sum_shots(dosi1_list, dosi2_list)
percent1_shot, percent2_shot    = pct_shots(dosi1_sum, dosi2_sum, total_sum)

print(f"Total de dosi 1: {dosi1_sum}")
print(f"Total de dosi 2: {dosi2_sum}")
print(f"Total de dosis:  {total_sum}")
print(f'Percentatge de vacunats 1a dosi: {percent1_shot}%')
print(f'Percentatge de vacunats 2na dosi: {percent2_shot}%')

# -----------------------------------------------------------------------------
