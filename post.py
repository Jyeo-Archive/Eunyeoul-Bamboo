#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import bs4
import base64
import facebook
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

def filterMessage(message):
    return message.replace('#', '') # remove tags
    # 사용자가 태그를 남용하면서 문제가 발생할 수 있기 때문에 불필요한 태그를 제거한다.
    # 헤더에 있는 태그까지 필터링되지 않도록 header와 message를 분리하여 다룬다.

# def getPageToken():
#     # 페이지 관리자의 정보를 이용해서 페이지 토큰값을 얻는 함수
#     username = '(관리자계정 이메일)'
#     password = base64.b64decode('(관계자계정 base64로 인코딩한 값)').decode()
#     # 페이지 관리자의 페이스북 계정 정보

#     chrome_options = webdriver.ChromeOptions()
#     # chrome_options.binary_location = '/app/.apt/usr/bin/google-chrome'
#     chrome_options.add_argument('--disable-gpu')
#     chrome_options.add_argument('--no-sandbox')
#     # chrome_driver_path = '/app/.chromedriver/bin/chromedriver'
#     chrome_driver_path = './chromedriver'
#     driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
#     # 드라이버를 설정한다(Chrome과 Chrome driver의 경로)
#     driver.get("http://www.fb.com")
#     # 페이스북 페이지에 접속 
#     assert "Facebook" in driver.title
#     elem = driver.find_element_by_id("email")
#     elem.send_keys(username)
#     elem = driver.find_element_by_id("pass")
#     elem.send_keys(password)
#     elem.send_keys(Keys.RETURN)
#     # 계정 정보를 사용하여 로그인 

#     driver.get("https://developers.facebook.com/tools/explorer")
#     elem = driver.find_element_by_xpath("//div[@class='_1c2l uiPopover _6a _6b']")
#     elem.click()
#     # 페이지 토큰 발급 버튼을 선택 

#     elem = driver.find_element_by_xpath("//span[.='은여울중학교 대나무숲']")
#     elem.click()
#     # 관리하는 페이지의 이름을 사용하여 선택 

#     page = bs4.BeautifulSoup(driver.page_source,'lxml')
#     # after running 'pip3 install lxml'
#     # 현재 페이지 소스를 저장 
#     driver.close()
#     # Chrome 창을 닫음
 
#     token_element = [item for item in page.select('input[type="text"]')]
#     token = str(token_element[1])
#     soup = bs4.BeautifulSoup(token, 'html.parser')
#     token = soup.input['value']  # val now contains the string 'THE_EMAIL_ADDRESS_HERE'
#     # 페이지 소스에서 페이지 토큰값을 구함

#     with open('token.txt', 'w') as f:
#         f.write(str(token) + '\n')
#         # save token in file
#         # 구한 토큰값을 저장 
#     return token # 토큰을 반환 
# # 위는 관리자 계정을 이용해서 토큰을 구하는 매크로(계정 잠금과 많은 에러를 얻을 수 있음)

def postOnBamboo(message):
    pageid = '???' # page id
    token = 'EAACfPfDiRdIBANVmntAiYgTdzEgRd9ve4aj9ZAmtLkhnIavwkgbR6jYIAE109lJTezFTMDLub94jyxegMk2hxvpwpaoebOCjVknZCoZAjhvZCd6paG8g3I77QqgQ3FNmZBQjcrRtCSzLb1mckcyLNkJ16jsJNDkAVuy3Fh6lwFMHorBy3LBgC'
    # 2개월짜리 토큰
    graph = facebook.GraphAPI(token)
    graph.put_object(pageid, 'feed', message=message)
    # try:
    #     with open('token.txt', 'r') as f:
    #         token = f.read().strip()
    #     graph = facebook.GraphAPI(token)
    #     graph.put_object(pageid, 'feed', message=message)
    #     # 파일에 있는 토큰값을 사용해서 게시물을 포스팅하는 것을 시도
    # except:
    #     token = getPageToken()        
    #     graph = facebook.GraphAPI(token)
    #     graph.put_object(pageid, 'feed', message=message)
    #     # 토큰 유효기간 종료로 실패 시, 새로 토큰을 발급받아 포스팅

if __name__ == '__main__':
    postOnBamboo(filterMessage('테스트'))
    # print(getPageToken())
