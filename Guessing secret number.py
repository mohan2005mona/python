from random import randint
secret_num=randint(1,100)
user_num=-1
try_count=1
while secret_num != user_num:
    print('%d try :'% try_count , end='')
    number=int(input())
    if number < secret_num:
        print('its less')
    elif number > secret_num:
        print('its greater')
    else :
        print('the secret number is :',secret_num)
        break
    try_count+=1
print('the random number is :',secret_num)

