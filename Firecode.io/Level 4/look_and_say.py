def look_and_say(sequence_number):
    if sequence_number <= 0:
        return None

    output = '1'
    i = 1
    while i < sequence_number:
        temp = ""
        count = 1
        for j in range(1, len(output)):
            if output[j] == output[j - 1]:
                count += 1
            else:
                temp += str(str(count) + output[j - 1])
                count = 1

        temp += str(str(count) + output[len(output) - 1])
        output = temp
        i += 1
    return output


print(look_and_say(7))
