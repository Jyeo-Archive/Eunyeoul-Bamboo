#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import threading
from flask import Flask, render_template, request, flash, redirect, url_for
from post import *

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/write', methods=['GET'])
def write():
    message = request.args.get('message')
    # 다른 API에서 사용하기 좋도록 GET 방식 (추후 급식봇 연동 예정)
    if message == '':
        return redirect(url_for('home')) # 시작 페이지로 리디렉션
    now = time.localtime()
    count = '?'
    with open('count.txt', 'r') as f:
        count = int(f.read().strip())
    # 현재 게시물의 수가 저장된 count.txt
    count += 1
    with open('count.txt', 'w') as f:
        f.write(str(count) + '\n')
    # 1 늘려서 저장
    header = '#' + str(count) + '번째_날개\n' + '%04d년 %02d월 %02d일 %02d시 %02d분 %02d초\n\n' % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    # 포스트 번호 + 현재 시간
    message = header + filterMessage(message)
    t = threading.Thread(target=postOnBamboo, args=(message,))
    t.start()
    # 토큰 발급에 시간이 오래 걸릴 수 있으므로 쓰레드를 생성하여 처리 
    flash('posted')
    # 게시글 발급이 완료되었음을 템플릿에 알림
    return redirect(url_for('home')) # 시작 페이지로 리디렉션

@app.route('/terms')
def show_term():
    return render_template('term.html')
    # 이용약관 및 개인정보처리방침

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)
    # 앱 실행
