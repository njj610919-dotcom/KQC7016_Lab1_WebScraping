#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[2]:


get_ipython().system('pip install requests beautifulsoup4')


# In[3]:


import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

print(response.status_code)
print(response.text[:500])


# In[4]:


soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")

for quote in quotes:
    print(quote.text)


# In[5]:


import pandas as pd

data = []

for quote in quotes:
    data.append(quote.text)

df = pd.DataFrame(data, columns=["Quote"])
df.to_csv("quotes.csv", index=False)

print(df)


# In[6]:


authors = soup.find_all("small", class_="author")

data = []

for quote, author in zip(quotes, authors):
    data.append({
        "Quote": quote.text,
        "Author": author.text
    })

df = pd.DataFrame(data)
df.to_csv("quotes_with_authors.csv", index=False)

print(df)


# In[ ]:




