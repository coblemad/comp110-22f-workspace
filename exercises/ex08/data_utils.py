"""Dictionary related utility functions."""

__author__ = "730544275"


from csv import DictReader


def read_csv_rows(csv_path: str) -> list[dict[str, str]]:
    """Read the CSV into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        rows.append(row)
    file_handle.close()
    return rows


def column_values(table_rows: list[dict[str, str]], key: str) -> list[str]:
    """Produce a list of all values in a single column whose name is in the second parameter."""
    values: list[str] = []
    for row in table_rows:
        values.append(row[key])
    return values


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Trasform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column."""
    new_table: dict[str, list[str]] = {}
    for key in table:
        new_table[key] = table[key][0:n]
    return new_table


def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    new_table: dict[str, list[str]] = {}
    for column in column_names:
        new_table[column] = table[column]
    return new_table


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    new_table: dict[str, list[str]] = {}
    for column in table_1:
        new_table[column] = table_1[column]
    for column in table_2:
        if column in new_table:
            new_table[column] += table_2[column]
        else:
            new_table[column] = table_2[column]
    return new_table