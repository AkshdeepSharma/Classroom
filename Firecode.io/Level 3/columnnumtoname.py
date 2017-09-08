def excel_column_number_to_name(column_number):
    column_name = ''
    while column_number > 0:
        module = (column_number - 1) % 26
        column_name += chr(module + 65)
        column_number = (column_number - module) // 26
    return column_name[::-1]


print(excel_column_number_to_name(81))