#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Python 获取股票信息

@author zhaoyb
'''
from datetime import datetime
#----------------------------------------------------------------------
def _get_stock_list():
    
    import requests as req
    import re 
    
    """
    获取股票各项信息
    """
    #获取股票代码url
    _stock_list_url = "http://bbs.10jqka.com.cn/codelist.html"
    
    #获取股票详情接口
    _sina_stock_i = "http://hq.sinajs.cn/list="
    
    s = req.Session()
    
    #设置代理
    proxies = {
            #'http': 'http://172.17.18.80:8080',
            #'https': 'http://172.17.18.80:8080'
    }
    
    f = s.get(_stock_list_url, timeout = 3, allow_redirects = True,proxies = proxies)
    
    content = f.content
    
    #ISO-8859-1 乱码...
    if f.encoding.lower() != 'utf-8':
        charset = re.compile(r'content="text/html;.?charset=(.*?)"').findall(content)
        try:
            if len(charset)>0 and charset[0].lower()!=f.encoding.lower():
                content = content.decode('gbk').encode('utf-8')
        except:
            pass
    #获取股票代码 这里指获取沪市的使用sh匹配  sh->[a-zA-Z]{2}可以获取所有的股票代码 
    stock_codes = re.compile(r'sh,[0-9]{3}[0-9a-zA-Z][0-9]{2}').findall(content)

    #存放所有股票信息的列表
    stock_list = list()
    #调用sina股票数据接口
    for stock_code in stock_codes:
        r = s.get(_sina_stock_i + str(stock_code).replace(",",""))
        #获取返回信息文本
        stoct_info_res = r.text
        #解析 - -使用'='分割一次
        (stock_code_res,stock_info) = stoct_info_res.split("=",1)
        stock_info = stock_info.replace('"','')  
        #存放单只股票信息的字典
        stock_dict = {}
        #如果返回信息为空
        stock_dict['stock_code_res'] = stock_code_res
        if len(stock_info) < 50:
            stock_dict['stock_name'],stock_dict['opening_price'],stock_dict['closing_price'],stock_dict['current_price'],stock_dict['higest_price'],stock_dict['lowest_price'] = 'NULL','0',float('0.0'),'0','0','0'
        else:
            #获取股票参数 - 存入字典,只要求获取前六项数据 
            try:
                (stock_dict['stock_name'],stock_dict['opening_price'],closing_price,stock_dict['current_price'],stock_dict['higest_price'],stock_dict['lowest_price'],other_info) \
                    = stock_info.split(',',6)
                #转成float方便排序
                stock_dict['closing_price'] = float(closing_price)
            except:
                print "some error occured when split the stock code ,plz check the input string.<%s>" % stock_info
        stock_list.append(stock_dict)
    return stock_list 

#----------------------------------------------------------------------
def write_to_excel(stock_list):
    
    """写入excel"""
    import os,sys
    import xlwt
    now = datetime.now().strftime('%Y%m%d')
    filename = 'stock' + now + ".xls"
    filepath = sys.path[0] +'\\' + filename
    if os.path.exists(filepath):
        #删除文件
        try:
            os.remove(filepath)
        except:
            print "some error occured when delete the temp file,check if the file is opening in other software."
    else:
        pass
    
    book = xlwt.Workbook()
    font = xlwt.Font()
    font.name = 'Times New Roman'
    font.bold = True
    style = xlwt.XFStyle()
    style.font = font
    #创建沪市股票列表sheet
    stock_list_sheet =  book.add_sheet(now + _toutf8('沪市股票列表'))
    #写表头
    stock_list_sheet.write(0,0,_toutf8('股票名称'),style)
    stock_list_sheet.write(0,1,_toutf8('股票代码'),style)
    stock_list_sheet.write(0,2,_toutf8('开盘价'),style)
    stock_list_sheet.write(0,3,_toutf8('收盘价'),style)
    stock_list_sheet.write(0,4,_toutf8('最高价格'),style)
    stock_list_sheet.write(0,5,_toutf8('最低价格'),style)
    
    #写入数据
    for i in range(len(stock_list)):

        stock_list_sheet.write(i+1,0,stock_list[i].get('stock_name'))
        stock_list_sheet.write(i+1,1,stock_list[i].get('stock_code_res')[-6:])
        stock_list_sheet.write(i+1,2,stock_list[i].get('opening_price'))
        stock_list_sheet.write(i+1,3,stock_list[i].get('closing_price'))
        stock_list_sheet.write(i+1,4,stock_list[i].get('higest_price'))
        stock_list_sheet.write(i+1,5,stock_list[i].get('lowest_price'))       
    
    #创建收盘价sheet
    stock_top10_sheet = book.add_sheet(now + _toutf8('股价最高top10'))
    stock_top10_sheet.write(0,0,_toutf8('股票名称'),style)
    stock_top10_sheet.write(0,1,_toutf8('股票代码'),style)
    stock_top10_sheet.write(0,2,_toutf8('收盘价'),style)    
    
    #排序
    import operator
    sorted_stock_list = sorted(stock_list, key=operator.itemgetter('closing_price'),reverse=True)  
    
    for i in range(10):
        stock_top10_sheet.write(i+1,0,sorted_stock_list[i].get('stock_name'))
        stock_top10_sheet.write(i+1,1,sorted_stock_list[i].get('stock_code_res')[-6:])
        stock_top10_sheet.write(i+1,2,sorted_stock_list[i].get('closing_price'))
	try:
		book.save(filepath)
	except:
		print 'some error occured when save excel,check if the file is opening in other software.'
#----------------------------------------------------------------------
def _toutf8(s):
    """"""
    return str(s).decode('utf-8')

if __name__ == "__main__":
    print '[%s] collecting stock information...' % datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lst = _get_stock_list()
    print '[%s] collect stock information finished...' % datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print _toutf8('[%s] writing stock information to excel...') % datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    write_to_excel(lst);
    print _toutf8('[%s] write stock information to excel finished...') % datetime.now().strftime('%Y-%m-%d %H:%M:%S')