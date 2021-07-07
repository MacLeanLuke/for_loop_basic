for x in range(0,101):
    gibberish = ''
    if x % 5 == 0:
        gibberish += 'Coding'
        if x % 10 == 0:
            gibberish += 'Dojo'
    else:
        gibberish = x
    print(gibberish)