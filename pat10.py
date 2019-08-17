for i in range(6):
    for j in range(5):
        if j==0 or ((j==4) and (i!=0 and i!=5)) or ((i==0 or i==5) and (0<j<4)): 
            print('*',end=' ')
        else:
            print(end='  ')
    print()
