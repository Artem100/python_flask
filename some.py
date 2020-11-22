value = "2%3"
listOrigin = list(value)
listMask = []
for i in listOrigin:
    if i == '%':
        listMask.append('\'')
    else:
        listMask.append(i)

print("".join(listMask))