def duplicate_items(list_numbers):
    duplicates = []
    non_duplicates = []
    for i in list_numbers:
        if i in non_duplicates:
            duplicates.append(i)
        else:
            non_duplicates.append(i)
    return sorted(duplicates)
