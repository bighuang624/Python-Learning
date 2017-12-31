#coding=utf-8
'''
武大教务系统 计算绩点
用法：在命令行中输入 python whu_grade_points.py
会自动在目录内下载验证码图片，在命令行中输入验证码
'''

import requests
import hashlib
from bs4 import BeautifulSoup
import re
from datetime import datetime

public_compulsory_sum = 0    # 公共必修
pro_compulsory_sum = 0
public_elective_sum = 0
pro_elective_sum = 0
public_compulsory_credits = 0
pro_compulsory_credits = 0
public_elective_credits = 0
pro_elective_credits = 0
public_compulsory_credits_with_scores = 0
pro_compulsory_credits_with_scores = 0
public_elective_credits_with_scores = 0
pro_elective_credits_with_scores = 0


'''
处理验证码的方法，可以随时修改
'''
def kill_captcha(data):
    with open('captcha.png', 'wb') as fp:
        fp.write(data)
    return input('captcha: ').encode('UTF-8')


'''
登录
'''
def login(idNum, password, oncaptcha, attempts):
    headers = {
        'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '210.42.121.241',
        'Referer': 'http://210.42.121.241/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
    }
    session = requests.session()
    session.get('http://210.42.121.241/', headers=headers)
    captcha_img = session.get('http://210.42.121.241/servlet/GenImg').content

    m2 = hashlib.md5()
    m2.update(password.encode('utf-8'))

    data = {
        'id': idNum,
        'pwd': m2.hexdigest(),
        'xdvfb': oncaptcha(captcha_img)
    }
    resp = session.post('http://210.42.121.241/servlet/Login', data=data, headers=headers, allow_redirects=False)
    resp.encoding = 'utf-8'
    try:
        if resp.headers['location'] == 'http://210.42.121.241/servlet/../stu/stu_index.jsp':
            print(u'登录成功！')
            return session
    except BaseException as e:
        if attempts > 3:
            print(u'验证码错误次数过多！停止操作')
            return None
        print(u'验证码错误！请重试，剩余尝试次数 %d' % (4 - attempts))
        login(idNum, password, oncaptcha, attempts+1)


'''
 获取 csrftoken 参数
'''
def getCsrftoken(session):
    headers = {
        'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '210.42.121.241',
        'Referer': 'http://210.42.121.241/stu/stu_index.jsp',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
    }
    html = session.get('http://210.42.121.241/stu/stu_score_parent.jsp', headers=headers).text
    groups = re.search(r'.+?/servlet/Svlt_QueryStuScore\?csrftoken=([\w\-]+).+', html)  
    return groups.group(1)


'''
获取时间参数
'''
def getT():
    now = datetime.now()
    return now.strftime('%a %b %d %Y %X ') + 'GMT+0800 (CST)'


'''
获得成绩页面的 html
'''
def getScoreHtml(session, csrftoken):

    headers = {
        'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '210.42.121.241',
        'Referer': 'http://210.42.121.241/stu/stu_score_parent.jsp',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
    }
    t = getT()
    params = {
        'csrftoken': csrftoken,
        'year': '0',
        'term': '',    
        'learnType': '',
        'scoreFlag': '0',
        't': t
    }
    html = session.get('http://210.42.121.241/servlet/Svlt_QueryStuScore', headers=headers, params=params)
    return html.text


'''
处理成绩页面的 html
'''
def processScoreHtml(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', {'class': 'table listTable'})
    trs = table.find_all('tr')
    for tr in trs:
        if tr.find('td') != None:
            tds = tr.find_all('td')
            lessonType = tds[2].get_text()
            credit = tds[3].get_text()
            score = tds[9].get_text()
            calGradePoint(lessonType, credit, score)



'''
打印报告
'''
def printReport():
    print(u'-----------------')
    print(u'公共必修已选学分：%.1f' % public_compulsory_credits)
    print(u'专业必修已选学分：%.1f' % pro_compulsory_credits)
    print(u'公共选修已选学分：%.1f' % public_elective_credits)
    print(u'专业选修已选学分：%.1f' % pro_elective_credits)
    print(u'必修绩点：%.3f' % ((public_compulsory_sum + pro_compulsory_sum) / (public_compulsory_credits_with_scores + pro_compulsory_credits_with_scores)))
    print(u'选修绩点：%.3f' % ((public_elective_sum + pro_elective_sum) / (public_elective_credits_with_scores + pro_elective_credits_with_scores)))
    print(u'总绩点：%.3f' % ((public_compulsory_sum + pro_compulsory_sum + public_elective_sum + pro_elective_sum) / (public_compulsory_credits_with_scores + pro_compulsory_credits_with_scores + public_elective_credits_with_scores + pro_elective_credits_with_scores)))



'''
计算学分、绩点
'''
def calGradePoint(lessonType, credit, score):
    global public_compulsory_sum, pro_compulsory_sum, public_elective_sum, pro_elective_sum
    global public_compulsory_credits, pro_compulsory_credits, public_elective_credits, pro_elective_credits
    global public_compulsory_credits_with_scores, pro_compulsory_credits_with_scores, public_elective_credits_with_scores, pro_elective_credits_with_scores
    if lessonType == u'公共必修':
        public_compulsory_credits += float(credit)
        if score != '':
            public_compulsory_credits_with_scores += float(credit)
            public_compulsory_sum += float(credit) * getGradePoint(float(score))

    elif lessonType == u'专业必修':
        pro_compulsory_credits += float(credit)
        if score != '':
            pro_compulsory_credits_with_scores += float(credit)
            pro_compulsory_sum += float(credit) * getGradePoint(float(score))

    elif lessonType == u'公共选修':
        public_elective_credits += float(credit)
        if score != '':
            public_elective_credits_with_scores += float(credit)
            public_elective_sum += float(credit) * getGradePoint(float(score))

    else:
        pro_elective_credits += float(credit)
        if score != '':
            pro_elective_credits_with_scores += float(credit)
            pro_elective_sum += float(credit) * getGradePoint(float(score))


'''
根据成绩获得绩点
'''
def getGradePoint(score):
    if score >= 90:
        return 4.0
    elif score >= 85:
        return 3.7
    elif score >= 82:
        return 3.3
    elif score >= 78:
        return 3.0
    elif score >= 75:
        return 2.7
    elif score >= 72:
        return 2.3
    elif score >= 68:
        return 2.0
    elif score >= 64:
        return 1.5
    elif score >= 60:
        return 1.0
    else:
        return 0.0


# 请在这里填写自己的学号和密码
if __name__ == '__main__':
    session = login('*************', '********', kill_captcha, 1)
    if session != None:
        csrftoken = getCsrftoken(session)
        html = getScoreHtml(session, csrftoken)
        processScoreHtml(html)
        printReport()

