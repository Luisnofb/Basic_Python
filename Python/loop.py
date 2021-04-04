"""
loops in python
"""


#for i, v in enumerate(nome):
    #print(nome[i])
#origin U+1F60D -> U0001F60D
for i in range(1,11):
    for n in range(11,i,-1):
        print(' ', end ='')
    print('\U0001F60D' * i)

for i in range(10,1 ,-1):
    for n in range(i,10,):
        print(' ', end ='')
    print('\U0001F60D' * i)
a=0
while a<3:
    print('amor')
    a+=1



