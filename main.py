#coding=utf-8
import time
import re
import requests
import datetime
import smtplib
from multiprocessing import Process

def qingqiu(web_url,uni_name='none'):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}     #设置headers信息，模拟成浏览器取访问网站
    req = requests.get(web_url, headers=headers)   #向网站发起请求，并获取响应对象
    req.encoding = 'utf-8'
    content = req.text   #获取网站源
    pattern = re.findall('.*调剂.*|.*硕士.*',content)  #正则化匹配字符，根据网站源码设置
    print(uni_name,':',pattern)
    return pattern  #运行qingqiu()函数，会返回pattern的值
    # return content
def send_email(uni_name,web_url):
    HOST = 'smtp.qq.com'   # 邮箱smtp
    PORT = '465'
    fajianren = '18392096749@qq.com'   #发送人邮箱
    shoujianren = '1454416200@qq.com'   #收件人邮箱
    title = uni_name + '更新信息通知'     # 邮件标题
    new_pattern = qingqiu(web_url)  #提取网页内容列表
    context = uni_name+'通知网站更新:'+web_url  # 邮件内容
    smtp = smtplib.SMTP_SSL(HOST, 465)  # 启用SSL发信, 端口一般是465
    res = smtp.login(user=fajianren, password='rkznwqgckknfbadg') # 登录验证，password是邮箱授权码而非密码，需要去网易邮箱手动开启
    print('发送结果：', res)
    msg = '\n'.join(
        ['From: {}'.format(fajianren), 'To: {}'.format(shoujianren), 'Subject: {}'.format(title), '', context])
    smtp.sendmail(from_addr=fajianren, to_addrs=shoujianren, msg=msg.encode('utf-8')) # 发送邮件
    print(context)

def update(uni_name,web_url):
    print('通知系统启动中')
    old_pattern = qingqiu(web_url,uni_name)  #记录原始内容列表
    while True:
        new_pattern = qingqiu(web_url,uni_name)  #记录新内容列表
        if (new_pattern!= old_pattern):  #判断内容列表是否更新
            old_pattern=new_pattern    #原始内容列表改变
            send_email(uni_name,web_url)   #发送邮件
        else:
            now=datetime.datetime.now()
            print(now,uni_name,"尚无更新")
        time.sleep(20)




if __name__ == '__main__':
    fun = update


    p1 = Process(target = fun,args=('大连大学', 'https://yjs.dlu.edu.cn/'))
    p1.start()
    p2 = Process(target = fun,args=('云南民族大学','http://202.203.158.67/web/469079/moreDongtai?categoryId=01d7abe2-c0d2-4bd3-b891-d3ae541f84c0'))
    p2.start()
    p3 = Process(target=fun, args=('北方民族大学', 'https://yjsc.nmu.edu.cn/index.htm'))
    p3.start()
    p4 = Process(target=fun, args=('大连理工大学', 'http://gs.dlut.edu.cn/yjszs/gzdt/gzdt.htm'))
    p4.start()
    p5 = Process(target=fun, args=('青岛大学', 'https://grad.qdu.edu.cn/infoArticleList.do?columnId=11363'))
    p5.start()
    p6 = Process(target=fun, args=('哈尔滨师范大学', 'http://yjsxy.hrbnu.edu.cn/list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1045'))
    p6.start()
    p7 = Process(target=fun, args=('安庆师范大学', 'http://grad.aqnu.edu.cn/zsjy.htm'))
    p7.start()
    p8 = Process(target=fun, args=('辽宁师范大学', 'https://master.lnnu.edu.cn/webroot/master/qrzxs/'))
    p8.start()
    p9 = Process(target=fun, args=('东北师范大学', 'https://yjsy.nenu.edu.cn/z_s1/s_s/f_s.htm'))
    p9.start()
    p10 = Process(target=fun, args=('西南大学', 'http://yz.swu.edu.cn/s/yanzhao/news1/'))
    p10.start()
    p11 = Process(target=fun, args=('辽宁大学', 'http://grs.lnu.edu.cn/zsgz.htm'))
    p11.start()
    p12 = Process(target=fun, args=('首都师范大学', 'https://grad.cnu.edu.cn/index/tzgg.htm'))
    p12.start()
    p13 = Process(target=fun, args=('江西师范大学', 'https://yz.jxnu.edu.cn/6249/list.htm'))
    p13.start()
    p14 = Process(target=fun, args=('福建师范大学', 'https://yjsy.fjnu.edu.cn/4227/list.htm'))
    p14.start()
    p15 = Process(target=fun, args=('西北师范大学', 'https://yjsy.nwnu.edu.cn/2701/list.htm'))
    p15.start()
    p16 = Process(target=fun, args=('山东师范大学', 'http://www.yjszs.sdnu.edu.cn/'))
    p16.start()
    p17 = Process(target=fun, args=('云南大学', 'http://www.grs.ynu.edu.cn/zytz.htm'))
    p17.start()
    p18 = Process(target=fun, args=('湖南师范大学', 'https://yjsy.hunnu.edu.cn/index.htm'))
    p18.start()
    p19 = Process(target=fun, args=('延边大学', 'https://grad.ybu.edu.cn/tzgg/zs.htm'))
    p19.start()
    p20 = Process(target=fun, args=('宁波大学', 'http://graduate.nbu.edu.cn/zsgz/ssszs.htm'))
    p20.start()
    p21 = Process(target=fun, args=('四川农业大学', 'https://yan.sicau.edu.cn/index/zs.htm'))
    p21.start()
    p22 = Process(target=fun, args=('曲阜师范大学', 'https://yjs.qfnu.edu.cn/zsgz.htm'))
    p22.start()
    p23 = Process(target=fun, args=('兰州大学文学院', 'http://chinese.lzu.edu.cn/'))
    p23.start()
    p24 = Process(target=fun, args=('广西大学文学院', 'https://wxy.gxu.edu.cn/index/tzgg.htm'))
    p24.start()
    p25 = Process(target=fun, args=('西北农林科技大学', 'https://yz.nwsuaf.edu.cn/tzgg/index.htm'))
    p25.start()
    p26 = Process(target=fun, args=('广西大学', 'https://yjsc.gxu.edu.cn/zsgz1/sszs.htm'))
    p26.start()
    p27 = Process(target=fun, args=('渤海大学', 'https://yjszsxxw.bhu.edu.cn/engine2/general/more?appId=506189&pageId=85721&wfwfid=138779&websiteId=63018&rootAppId='))
    p27.star()
    p28 = Process(target=fun, args=('重庆师范大学文学院', 'https://wxy.cqnu.edu.cn/xb2021/xbsy/tzgg.htm'))
    p28.start()
    p29 = Process(target=fun, args=('重庆师范大学', 'https://graduate.cqnu.edu.cn/zsgz1/sszs.htm'))
    p29.start()
    p30 = Process(target=fun, args=('山西大学', 'http://yjszsw.sxu.edu.cn'))
    p30.start()
    p31 = Process(target=fun, args=('闽南师范大学研究生', 'https://yjsc.mnnu.edu.cn/zsgz/ssyjszs.htm'))
    p31.start()
    p32 = Process(target=fun, args=('河北大学', 'http://yjsy.hbu.edu.cn/index.php?m=content&c=index&a=lists&catid=51'))
    p32.start()
    p33 = Process(target=fun, args=('西北师范大学文学院', 'https://wxy.nwnu.edu.cn/753/list.htm'))
    p33.start()
    p34 = Process(target=fun, args=('福建师范大学文学院', 'http://wxy.fjnu.edu.cn/_t1886/7401/list.psp'))
    p34.start()
    p35 = Process(target=fun, args=('河北大学文学院', 'https://wxy.nwnu.edu.cn/753/list.htm'))
    p35.start()
    p36 = Process(target=fun, args=('渤海大学文学院', 'https://www3.bhu.edu.cn/page/depart/wxy/index.asp'))
    p36.start()
    p37 = Process(target=fun, args=('燕山大学', 'http://zsjyc.ysu.edu.cn/yjsxwz/sszs/szdong.htm'))
    p37.start()
    p38 = Process(target=fun, args=('西华大学', 'http://rwxy.xhu.edu.cn/5974/list.htm'))
    p38.start()


    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
    p11.join()
    p12.join()
    p13.join()
    p14.join()
    p15.join()
    p16.join()
    p17.join()
    p18.join()
    p19.join()
    p20.join()
    p21.join()
    p22.join()
    p23.join()
    p24.join()
    p25.join()
    p26.join()
    p27.join()
    p28.join()
    p29.join()
    p30.join()
    p31.join()
    p32.join()
    p33.join()
    p34.join()
    p35.join()
    p36.join()
    p37.join()
    p38.join()




