# -*- coding-8 -*-
import requests
import lxml
from bs4 import BeautifulSoup
import xlwt


def craw(url):
    headers = {
        'Host': 'www.qichacha.com',
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.qichacha.com/',
        'Cookie': r'UM_distinctid=*************************',
        'Connection': 'keep-alive',
        'If-Modified-Since': 'Wed, 10 May ***************',
        'Cache-Control': 'max-age=0',
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        response.encoding = 'utf-8'
        print(response.status_code)
        print('ERROR')
    # ---获取网页信息赋值给soup---
    soup = BeautifulSoup(response.text, 'lxml')
    # ---通过相应位置的class获取相应的信息---
    com_names = soup.find_all(class_='ma_h1')
    peo_names = soup.find_all(class_='text-primary')
    peo_phones = soup.find_all(class_='m-t-xs')

    # ---使用global声明变量，使在局部内改变全局变量的值---
    global com_name_list
    global peo_name_list
    global peo_phone_list
    global com_place_list
    global zhuceziben_list
    global chenglishijian_list
    print('开始爬取数据，请勿打开excel')

    for i in range(0, len(com_names)):
        n = 1 + 3 * i
        m = i + 2 * (i + 1)
        peo_phone = peo_phones[n].find(text=True).strip()
        peo_phone = peo_phone[3:len(peo_phone)]
        # print(peo_phone)
        com_place = peo_phones[m].find(text=True).strip()
        com_place = com_place[3:len(com_place)]
        # print(com_place)
        zhuceziben = peo_phones[3 * i].find(class_='m-l').get_text()
        zhuceziben = zhuceziben[5:len(zhuceziben)]
        # print(zhuceziben)
        chenglishijian = peo_phones[3 * i].contents[5].get_text()
        chenglishijian = chenglishijian[5:len(chenglishijian)]
        # print(chenglishijian)
        com_name = com_names[i].get_text()
        peo_name = peo_names[i].get_text()

        # 将上面处理的字段赋值给相应的list
        peo_phone_list.append(peo_phone)
        com_place_list.append(com_place)
        zhuceziben_list.append(zhuceziben)
        chenglishijian_list.append(chenglishijian)
        com_name_list.append(com_name)
        peo_name_list.append(peo_name)



if __name__ == '__main__':
    com_name_list = []
    peo_name_list = []
    peo_phone_list = []
    com_place_list = []
    zhuceziben_list = []
    chenglishijian_list = []
    key_word = input('请输入您想搜索的关键词：')
    print('正在搜索，请稍后')
    url = r'http://www.qichacha.com/search?key={}'.format(key_word)
    craw(url)
    workbook = xlwt.Workbook()
    # 创建sheet对象，新建sheet
    sheet1 = workbook.add_sheet('xlwt', cell_overwrite_ok=True)

    # ---设置excel样式---
    # 初始化样式
    style = xlwt.XFStyle()
    # 创建字体样式
    font = xlwt.Font()
    font.name = 'Times New Roman'
    font.bold = True  # 加粗
    # 设置字体
    style.font = font
    print('正在存储数据，请勿打开excel')

    # ---向sheet中写入数据---
    name_list = ['公司名字', '法定代表人', '联系方式', '注册人资本', '成立时间', '公司地址']
    for cc in range(0, len(name_list)):
        sheet1.write(0, cc, name_list[cc], style)
    for i in range(0, len(com_name_list)):
        x = i + 1
        sheet1.write(x, 0, com_name_list[i], style)  # 公司名字
        sheet1.write(x, 1, peo_name_list[i], style)  # 法定代表人
        sheet1.write(x, 2, peo_phone_list[i], style)  # 联系方式
        sheet1.write(x, 3, zhuceziben_list[i], style)  # 注册人资本
        sheet1.write(x, 4, chenglishijian_list[i], style)  # 成立时间
        sheet1.write(x, 5, com_place_list[i], style)  # 公司地址

    # ---保存excel文件到指定，有同名的直接覆盖---
    workbook.save(r'D:\work\xlwt.xls')
    print('the excel save success')