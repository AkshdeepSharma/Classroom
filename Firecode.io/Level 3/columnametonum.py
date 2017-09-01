def excel_column_name_to_number(column_title):
    num = 0
    for i in column_title:
        num = num * 26 + (ord(i.upper()) - ord("A")) + 1
    return num
