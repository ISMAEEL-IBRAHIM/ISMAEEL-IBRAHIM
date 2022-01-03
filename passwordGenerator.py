import random
for i in range(5):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    characters = "!@#$%^&*?.,"
    all = lower + upper + numbers + characters
    length = int(input('enter the lenght of the password:\n'))
    password = "".join(random.sample(all,length))
    print(password)

