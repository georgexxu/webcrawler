
# coding: utf-8

# In[44]:

import urllib.request
import urllib.error
import json
import pprint
import csv


# In[34]:

class search:
    # 初始化方法，定义一些变量
    def __init__(self):      
        
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
        
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
        # 存放程序是否继续运行的变量
        self.enable = False
        


    # 传入某一页的索引获得页面代码
    def getpage(self,pagenum):
        
        url = 'https://www.openrice.com/api/pois?uiLang=zh&uiCity=hongkong&page={}&&sortBy=Default&categoryGroupId=20002'.format(pagenum)
            # 构建请求的request
        request = urllib.request.Request(url, headers=self.headers)
            # 利用urlopen获取页面代码
        response = urllib.request.urlopen(request)
            # 将页面转化为UTF-8编码
        pageCode = response.read().decode('utf-8')
        
        return pageCode
    def getListOfRest(self,pagenum):
        contents=json.loads(self.getpage(pagenum))
        ListOfRest=contents['searchResult']['paginationResult']['results']
        ListOfRest_=[]
        for key in ListOfRest:
            ListOfRest_.append({k: key.get(k, None) for k in ('name','priceUI','reviewCount','shortenUrl',)})

        return ListOfRest_
    
    def longList(self):
        longList_=[]
        i=1;
        while(1):
            if (i>17):
                return longList_
                
            try:
                longList_+=(self.getListOfRest(i))
                print(i)
                i+=1
            except Exception as e:
                print('gggg')
                return longList_
#        return longList_
    
    
pages= search() 

ChineseRestaurant=pages.longList()


# In[9]:

pp=pprint.PrettyPrinter()
ListOfRest_=[]
for key in ListOfRest:
    ListOfRest_.append({k: key.get(k, None) for k in ('name','priceUI','reviewCount','shortenUrl',)})


# In[46]:

ChineseRestaurant=a
ChineseRestaurant


# In[58]:

len(ChineseRestaurant)


# In[38]:

with open("ChineseRestaurant.csv",'w',encoding='utf8') as file:
    file.write(a)


# In[61]:

with open('ChineseRestaurant.csv', 'w',encoding="utf-8-sig") as csv_file:
    keys=ChineseRestaurant[0].keys()
    writer = csv.DictWriter(csv_file,keys)
    writer.writeheader()
    for rows in ChineseRestaurant:
        writer.writerow(rows)


# In[ ]:




# In[ ]:



