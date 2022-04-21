'''Tables as an object'''
from pathlib import Path

class Table:

    # Constructor
    def __init__(self, data: list[list[str]]):
        self.data: list[list[str]] = data

    def __str__(self) -> str:
        result: str = ''
        for row in self.data:
            row_str: str = ''.join(row)
            result += f'{row_str}\n'
        return result

    def read_csv(self, csv_file_path: str) -> str:
        '''Input:  The path to a .csv file.
          Output: The contents of the .csv file as a single string.'''

        raw_text:      str = Path(csv_file_path).read_text()
        stripped_text: str = raw_text.strip()

        return stripped_text


    def separate_by_rows(self, contents: str) -> list[str]:
        '''Input:  The file contents as a single string.
            Output: A list of strings where each string is a row of the csv file.'''
        
        rows: list[str] = contents.split("\n")

        return rows


    def separate_by_columns(self, rows: list[str]) -> list[list[str]]:
        '''Input:  A list of strings. Each string is a row of a csv file. Row fields are separated by ";".
            Output: A table where each row has been splitted into a list of fields.'''

        table: list[list[str]] = [row.split(";") for row in rows]

        return table

    
    def read_table(self, csv_file_path: str) -> list[list[str]]:
        '''Input:  Path of a .csv file.
           Output: Table as a list of lists of strings with the csv contents.'''

        csv_str: str             = self.read_csv(csv_file_path)
        rows:    list[str]       = self.separate_by_rows(csv_str)
        table:   list[list[str]] = self.separate_by_columns(rows)

        return table


    def filter_rows(self, table: list[list[str]], column_name: str, search_str: str) -> list[list[str]]:
        '''Input:  Table, columne and search string to filter by. 
           Output: Returns table with rows whose column_name includes search_str. Includes the header.'''

        # Precondition: There is at least a header in the table
        assert len(table) >= 1

        # Get the header and data body
        header: list[str]       = table[0]
        data:   list[list[str]] = table[1:]

        # Precondition: column_name is in the header
        assert column_name in header

        # Find the column index
        column_index: int = header.index(column_name)

        # Filter rows
        filtered_data: list[list[str]] = [row for row in data if (search_str in row[column_index]) ]

        # Add header to result
        result: list[list[str]] = [header] + filtered_data

        return result


    def get_column(self, table: list[list[str]], column_name: str) -> list[str]:
        '''Input:  Column name as a string and Table as a list of lists of strings.
           Output: The column whose name is column_name WITHOUT the header.'''

        # Precondition: There is at least a header in the table
        assert len(table) >= 1

        # Get the header and data body
        header: list[str]       = table[0]
        data:   list[list[str]] = table[1:]

        # Precondition: column_name is in the header
        assert column_name in header

        # Find the column index
        column_index: int = header.index(column_name)

        # Return column
        result: list[str] = [row[column_index] for row in data]

        return result


    def convert_type_to_int(self, input_list: list) -> list[int]:
        '''Input:  A list of a certain type.
           Output: The list with all elements converted to new_type.'''

        result: list[int] = [int(elem) for elem in input_list]

        return result


if __name__ == "__main__":

    list1: list[list[str]] = [[str(y) for y in range(6)] for x in range(21)]
    table: Table = Table(list1)
    print(table)
    table_from_list: Table = Table.from_csv("/home/pswsm/github/cfgs-python/dades_covid/2022-01-20-covid-dades-aga/2022-01-20-covid-dades-simple.csv")
    print(table_from_list)


