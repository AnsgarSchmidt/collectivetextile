import cv2
import numpy as np
import os
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
queue = []

def num2pattern(num):
    if num == 1:
        return [  0,   0,   0,   0, 255,   0,   0,   0,   0,   0]
    if num == 2:
        return [  0,   0, 255,   0,   0,   0,   0,   0, 255,   0]
    if num == 3:
        return [  0,   0, 255, 255, 255,   0,   0,   0,   0,   0]
    if num == 4:
        return [  0,   0, 255,   0, 255,   0,   0,   0, 255, 255]
    if num == 5:
        return [255, 255, 255,   0,   0,   0, 255,   0, 255,   0]
    if num == 6:
        return [255,   0, 255, 255, 255,   0,   0, 255, 255,   0]
    if num == 7:
        return [255, 255, 255,   0, 255, 255, 255, 255,   0,   0]
    if num == 8:
        return [255, 255, 255, 255, 255, 255, 255,   0,   0, 255]
    if num == 9:
        return [255, 255, 255, 255, 255,   0, 255, 255, 255, 255]
    if num >= 10:
        return [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/questions-en')
def QuestionsEN():
    return app.send_static_file('questions-en.html')

@app.route('/questions-de')
def QuestionsDE():
    return app.send_static_file('questions-de.html')

@app.route('/answer', methods=['POST', 'PUSH', 'GET'])
def Answer():
    nickname = request.form['nickname']
    if nickname is None or len(nickname) == 0:
        print "Nickname not set"
        return app.send_static_file('error.html')

    q1 = request.form['q1']
    if q1 is None or len(q1) == 0:
        print "q1 not set"
        return app.send_static_file('error.html')
    q1 = len(q1)
    q1 = num2pattern(q1)

    q2 = request.form['q2']
    if q2 is None or len(q2) == 0:
        print "q2 not set"
        return app.send_static_file('error.html')
    try:
        q2str = str(q2)
        q2 = sum([int(i) for i in q2str])
    except:
        print "Error in q2"
        return app.send_static_file('error.html')
    q2 = num2pattern(q2)

    q3 = request.form['q3']
    if q3 is None or len(q3) == 0:
        return app.send_static_file('error.html')
    try:
        q3 = int(q3)
        if q3 < 1 or q3 > 10:
            return app.send_static_file('error.html')
    except:
        return app.send_static_file('error.html')
    q3 = num2pattern(q3)

    q4 = request.form['q4']
    if q4 is None or len(q4) == 0:
        return app.send_static_file('error.html')
    try:
        q4 = int(q4)
        if q4 < 1 or q4 > 10:
            return app.send_static_file('error.html')
    except:
        return app.send_static_file('error.html')
    q4 = num2pattern(q4)

    q5 = request.form['q5']
    if q5 is None or len(q5) == 0:
        return app.send_static_file('error.html')
    try:
        q5 = int(q5)
        if q5 < 0 or q5 > 100:
            return app.send_static_file('error.html')
    except:
        return app.send_static_file('error.html')
    if q5 == 0:
        q5 = 1
    q5 = num2pattern(q5)

    q6 = request.form['q6']
    if q6 is None or len(q6) == 0:
        return app.send_static_file('error.html')
    try:
        q6 = int(q6)
        if q6 < 0 or q6 > 100:
            return app.send_static_file('error.html')
    except:
        return app.send_static_file('error.html')
    q6 = num2pattern(q6)

    q7 = request.form['q7']
    if q7 is None or len(q7) == 0:
        return app.send_static_file('error.html')
    try:
        q7 = int(q7)
        if q7 < 1 or q7 > 10:
            return app.send_static_file('error.html')
    except:
        return app.send_static_file('error.html')
    q7 = num2pattern(q7)

    q8 = request.form['q8']
    if q8 is None or len(q8) == 0:
        return app.send_static_file('error.html')
    if q8 == "yes":
        q8 = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
    else:
        q8 = [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0]

    q9 = request.form['q9']
    if q9 is None or len(q9) == 0:
        return app.send_static_file('error.html')
    try:
        q9 = int(q9)
        if q9 < 0 or q9 > 24:
            return app.send_static_file('error.html')
    except:
        return app.send_static_file('error.html')
    q9 = num2pattern(q9)

    q10 = request.form['q10']
    if q10 is None or len(q10) == 0:
        return app.send_static_file('error.html')
    try:
        q10 = int(q10)
        if q10 < 1 or q10 > 10:
            return app.send_static_file('error.html')
    except:
        return app.send_static_file('error.html')
    q10 = num2pattern(q10)

    q = [nickname, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    queue.append(q)
    print "q=%s" % q
    print len(queue)
    return app.send_static_file('thankyou.html')

@app.route('/admin')
def Admin():
    return app.send_static_file('admin.html')

@app.route('/result')
def Result():
    if len(queue) > 0:
        user = queue.pop(0)
        nickname = user[0]
        blank_image = np.zeros((10, 100, 1), np.uint8)
        for i in range(10):
            for x in range(10):
                line = user[x + 1]
                for y in range(10):
                    blank_image[x, (i * 10) + y] = line[y]
        cv2.imwrite("static/test.png", blank_image)
        return app.send_static_file('result.html')
    else:
        print "Number of entries=%d" % len(queue)
        return app.send_static_file('error.html')

if __name__ == "__main__":
    port = os.getenv('PORT', '5000')
    app.run(host='0.0.0.0', port=int(port))
