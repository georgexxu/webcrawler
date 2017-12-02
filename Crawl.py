
# coding: utf-8

# In[34]:

import urllib.request
import urllib.error
import json
import pprint


# In[35]:

class search:
    # 初始化方法，定义一些变量
    def __init__(self):      
        
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
        
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
        # 存放程序是否继续运行的变量
        self.enable = False
        


    # 传入某一页的索引获得页面代码
    def getpage(self):
        url = 'https://www.openrice.com/api/pois?uiLang=zh&uiCity=hongkong&page=1&&sortBy=Default&cuisineId=1008&districtId=2999'
            # 构建请求的request
        request = urllib.request.Request(url, headers=self.headers)
            # 利用urlopen获取页面代码
        response = urllib.request.urlopen(request)
            # 将页面转化为UTF-8编码
        pageCode = response.read().decode('utf-8')
        
        return pageCode
    def getListOfRest(self):
        contents=json.loads(self.getpage())
        return contents['searchResult']['paginationResult']['results']

pages= search() 

ListOfRest=pages.getListOfRest()


# In[38]:

pp=pprint.PrettyPrinter()
pp.pprint(ListOfRest)


# In[ ]:




# In[ ]:



