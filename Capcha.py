                                 # Capctha program without using functions 

import random

captcha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

b = ""

for i in range(5):
    b += random.choice(captcha)
print("generated capcha : " , b)
    