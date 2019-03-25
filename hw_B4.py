#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
a = int(random.uniform(0, 100))
def nomber():
    nomber_input = input('Введите число ')
    while nomber_input.isdigit() is not True:
        nomber_input = input('Введите корректное число ')
    else:
        b = int(nomber_input)
    return(b)
c = nomber()    
while a != c:
    while a > c:
        print('Загаданное число больше')
        c = nomber()
        
    else:
        print('Загаданное число меньше')
        c = nomber()
else:
    print('Вы угадали!')


# In[2]:





# In[ ]:




