def flexible_counter(lowNum, highNum, mult):
    for x in range(lowNum, highNum+1):
        if x % mult == 0:
            print(x)

flexible_counter(2,9,3)