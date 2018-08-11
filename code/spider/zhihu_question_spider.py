# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
知乎主题问题爬虫
__author__ = 'Huang Siteng'
'''

import requests
import json
import random
import pandas as pd
import time

category_id = {
    '线性模型': [19650500, 20014861],
    '决策树': [19569936],
    '支持向量机': [19583524],
    '贝叶斯统计': [19632220],
    '集成学习': [20033220],
    '聚类': [19627785, 19590190],
    '数据降维': [20010182],
    '特征选择与稀疏学习': [19809410, 20058170],
    '强化学习': [20100750],
    '神经网络': [19607065]
}

user_agents = [
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Chrome/10.0.648.133 Safari/534.16',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:57.0) Gecko/20100101 Firefox/57.0'
]

qdict = {'question': [], 'category': []}

def get_url_by_id(id):
    return 'https://www.zhihu.com/api/v4/topics/' + str(id) + '/feeds/timeline_question?limit=10&offset=0'

def download_page(url):
    headers = {
        'User-Agent': user_agents[random.randint(0, 5)]
    }
    data = requests.get(url, headers=headers).content
    return data

def parse(response, category):
    time.sleep(0.6)
    datas = json.loads(response)
    if datas:
        for q in datas['data']:
            # 获得、存储
            question = q['target']['title']
            qdict['question'].append(question)
            qdict['category'].append(category)

        # 如果 is_end 为 False
        if not datas['paging']['is_end']:
            # 继续爬
            next_url = datas['paging']['next']
            return next_url

        return None
    return None

def main():

    for key, value in category_id.items():
        print(key)
        for id in value:
            start_url = get_url_by_id(id)
            while start_url:
                start_url = parse(download_page(start_url), key)

    pd.DataFrame(qdict).to_csv("zhihu_question.csv", index=False)

if __name__ == '__main__':
    main()