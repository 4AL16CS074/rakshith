for i  in range(7):
    for j in range(5):
        if j==0 or ((j==4) and (i!=0 and i!=3 and i!=6))  or ((i==0 or i==3 or i==6) and (0<j<4)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()
                              
