#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 下午2:19
# @Author  : yinxin
# @File    : utils
# @Software: PyCharm

import re
import hashlib


def split_salary(salary_str):
    salary_min = 0
    salary_max = 0
    several = 12
    if re.search('[kK]', salary_str):
        group = re.findall('([0-9]+)', salary_str)
        salary_min = int(group[0])
        salary_max = 0 if len(group) == 1 else int(group[1])
        try:
            several = group[2]
        except IndexError:
            pass
    elif re.search('[天]', salary_str):
        group = re.findall('([0-9]+)', salary_str)
        salary_min = int(group[0]) * 22 // 1000
        salary_max = int(group[1]) * 22 // 1000
    else:
        pass

    return {'salaryMin': salary_min, 'salaryMax': salary_max, 'several': several}


def split_exp(exp_str):
    exp_min = 0
    exp_max = 0

    if re.search('天/周', exp_str):
        pass
    elif re.search('[年]', exp_str):
        group = re.findall('([0-9]+)', exp_str)
        exp_min = 0 if len(group) == 1 else int(group[0])
        exp_max = int(group[-1])
    else:
        pass

    return {'expMin': exp_min, 'expMax': exp_max}


def split_scale(scale_str):
    scale_min = 0
    scale_max = 0

    if re.search('[0-9]+人', scale_str):
        group = re.findall('([0-9]+)', scale_str)
        if len(group) == 1:
            scale_min = int(group[0]) if group[0] == "2000" else 0
            scale_max = int(group[0]) if group[0] == "15" else 0
        else:
            scale_min = int(group[0])
            scale_max = int(group[-1])
    else:
        pass

    return {'scaleLeft': scale_min, 'scaleRight': scale_max}


def remake_url(url_str: str):
    return url_str.split("?")[0]


def strToHash(str):
    return hashlib.sha256(bytes(str, encoding="utf8")).hexdigest()


if __name__ == '__main__':
    recrStr = '{"srcName": "拉勾", "srcPosId": "6629421", "srcUrl": "https://www.lagou.com/jobs/6629421.html", "advantage": ["公司背景好", "发展稳定", "平台广阔"], "companyMainPage": "https://www.lagou.com/gongsi/559910.html", "companyName": "伽轩成都软件开发中心", "companyNature": ["电商", "移动互联网"], "edu": "本科及以上", "exp": "经验3-5年", "hrName": "人事", "hrPosition": "HRM", "salary": "15k-30k", "posDesc": "（某国企正式编制工作机会）工作职责：根据银行项目管理流程、技术设计与开发规范，完成项目的详细设计、代码开发与版本控制、单元测试、集成测试、上线文档填写和应急方案制定等工作。工作方向：（1）可稳定持续发展。新成立软件研发中心，晋升机会较多，且银行类平台较稳定，可长期发展。（2）技术面广。核心系统业务，开发主要以银行的交易系统为主，独立开发，给全行做软件支持，因此接触的技术面较广。任职资格：1、具有1年及以上商业银行或其他金融机构信息技术相关工作经验；2、熟练掌握Java或C/C++语言等编程语言及主流开源相关技术，掌握银行IT系统开发规范、IT系统架构及数据库相关知识，近两年主要工作方向为Java或C/C++开发，具有J2EE开发平台，特别是中间业务平台设计工作经验者优先；3、具有总、分行中间业务系统开发、金融互联网产品研发工作经验者优先，如行内与跨行支付，代理财政、社会保障，资金监管，公共资源账户管理，公共事业缴费（含BS客户端）等中间业务系统。", "position": "java开发工程师", "scale": "150-500人", "stage": "B轮", "publishTime": "2019-12-09", "tagList": ["银行", "Java"], "spiderUuid": "adc03b4a-1b00-11ea-b5b4-54759502c5a0", "address": "成都-高新区-天府新区兴隆湖", "city": "成都", "salaryMin": 15, "salaryMax": 30, "several": 12, "expMin": 3, "expMax": 5, "scaleLeft": 150, "scaleRight": 500}'

    print(strToHash(recrStr))

    # print(remake_url(r"https://www.lagou.com/jobs/6629421.html?show\u003dc328dded782942f091fb26cc9b096125"))