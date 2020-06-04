for xd in range(3):
    num = xd + 1
    for yd in range(3):
        num = num + yd
        creat_text_x = 100 + 250 * xd + 20
        creat_text_y = 100 + 250 * yd - 20
        print("**************" )
        print(num * 2)
        num = num + 2
        print("--------------")
        print(num)

        print("**************")
        print( num * 2 +1)

list=[]
for i in range(9):
    m = str(i)
    var = 'L' + m + '-' + '1'
    list.append(var)

    print(list)