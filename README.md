# myPython
基于python3的各种爬虫系列（不定时更新）

欢迎访问我的个人网站：https://mealialin.github.io/

## 声明

软件均仅用于学习交流，请勿用于任何商业用途！

## 爬虫实战

* novelDownload文件夹下放的是相关小说网站的小说爬取工具

	第三方依赖库安装(到python安装目录的script文件夹下运行cmd)：

		pip3 install beautifulsoup4
		pip3 install lxml

	使用方法（如biqu.py:《笔趣看》盗版小说网站）：

		python biqu.py

* qichacha.py：简单爬取企查查相关企业信息，并以excel格式存储
    
    环境
    
        * python3.6
        * BeautifulSoup模块
        * lxml模块
        * requests模块
        * xlwt模块
     
    使用方法
    
     1、登录[企查查网站](http://www.qichacha.com)，注册账号（不登录只能查五条信息），然后使用的浏览器需打开cookies功能，关闭浏览器也不能清掉cookies，否则登录信息被删除也只能查到五条信息
     
     2、根据你网页的headers相关信息，修改代码中headers信息，主要是修改一串***区域的信息。不懂可借鉴[在chrome查询http报文的头部信息](https://jingyan.baidu.com/article/27fa73268ff4e146f8271f33.html)
     
     3、修改倒数第二句代码的文本存档位置，根据自己所需要改成自己想要的存放位置
     
     4、运行代码：
     
        python qichacha.py