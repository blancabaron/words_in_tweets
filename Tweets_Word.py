#!/usr/bin/env python
# coding: utf-8

# import json
# import pandas as pd
# 
# def carga_tweets(filename):
#     
#     try:
#         tweets = []
#         tweets_def = pd.read_json(filename, lines=True)   
#         tweets_def = tweets_def[tweets_def.text.notnull()]['text']
#         tweets = tweets_def.to_list()
#         return tweets
#     except:
#         print("El fichero" + filename + "no existe")

# In[2]:


file_tweet = "tweets2.txt"


# In[3]:


file_sentimientos="sentimientos.txt"


# In[4]:


def carga_sentimientos(filename):
    valores = {}
    for linea in open(filename, 'r'):
         termino, valor = linea.split('\t')
         valores[termino] = int(valor)
    return valores


# In[5]:


lista_tweet = carga_tweets(file_tweet)


# In[6]:


lista_tweet


# In[7]:


sentimiento = carga_sentimientos(file_sentimientos)


# In[8]:


sentimiento


# In[9]:


for tweet in lista_tweet:
    cuenta_tweet = 0
    for palabra in tweet.split(" "):
        cuenta_tweet += sentimiento.get(palabra.lower(),0)
    print("Este tweet: '" + tweet + "' tiene un sentimiento de: " + str(cuenta_tweet))
    print("\n")


# In[ ]:


#Ejercicio 2 # 


# In[15]:


for tweet in lista_tweet:
    cuenta_tweet = 0
    palabras_no = []
    numero_palabras = 0
    for palabra in tweet.split(" "):
        cuenta_tweet += sentimiento.get(palabra.lower(),0)
        numero_palabras += 1
        if sentimiento.get(palabra.lower(),0)==0:
            palabras_no.append(palabra)


# In[16]:


for i in palabras_no:
        print(i + ': ' + str(cuenta_tweet/numero_palabras))
        print("\n")


# In[ ]:




