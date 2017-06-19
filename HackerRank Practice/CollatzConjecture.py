
n = int(input());
counter = 0

while n != 1:
    if n % 2 != 0:
        n = (n * 3) + 1
    elif n % 2 == 0:
        n = n // 2
    counter = counter + 1

print(counter)

'''
9: 28. 14. 7. 22. 11. 34. 17. 52. 26. 13. 40. 20. 10. 5. 16. 8. 4. 2. 1.
'''