import cv2
import numpy as np
import os
import random
from flask import Flask, render_template, request

app   = Flask(__name__)
queue = []


def num2pattern(num):
    if num == 0:
        return [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0]
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


@app.route('/answer', methods=['POST'])
def Answer():
    nickname = request.form['nickname']
    if nickname is None or len(nickname) == 0:
        print "Nickname not set"
        return render_template('error.html', error="Nichname not set")

    q1 = request.form['q1']
    if q1 is None or len(q1) == 0:
        print "q1 not set"
        return render_template('error.html', error="Question 1 not set")
    q1 = len(q1)
    q1 = num2pattern(q1)

    q2 = request.form['q2']
    if q2 is None or len(q2) == 0:
        print "q2 not set"
        return render_template('error.html', error="Question 2 not set")
    try:
        q2str = str(q2)
        q2 = sum([int(i) for i in q2str])
    except:
        print "Error in q2"
        return render_template('error.html', error="Question 2 not a number")
    q2 = num2pattern(q2)

    q3 = request.form['q3']
    if q3 is None or len(q3) == 0:
        return render_template('error.html', error="Question 3 not set")
    try:
        q3 = int(q3)
        if q3 < 1 or q3 > 10:
            return render_template('error.html', error="Question 3 not a valid number")
    except:
        return render_template('error.html', error="Question 3 not a valid number")
    q3 = num2pattern(q3)

    q4 = request.form['q4']
    if q4 is None or len(q4) == 0:
        return render_template('error.html', error="Question 4 not set")
    try:
        q4 = int(q4)
        if q4 < 1 or q4 > 10:
            return render_template('error.html', error="Question 4 not a valid number")
    except:
        return render_template('error.html', error="Question 4 not a valid number")
    q4 = num2pattern(q4)

    q5 = request.form['q5']
    if q5 is None or len(q5) == 0:
        return render_template('error.html', error="Question 5 not set")
    try:
        q5 = int(q5)
        if q5 < 0 or q5 > 100:
            return render_template('error.html', error="Question 5 not a valid number")
    except:
        return render_template('error.html', error="Question 5 not a valid number")
    if q5 == 0:
        q5 = 1
    q5 = num2pattern(q5)

    q6 = request.form['q6']
    if q6 is None or len(q6) == 0:
        return render_template('error.html', error="Question 6 not set")
    try:
        q6 = int(q6)
        if q6 < 0 or q6 > 100:
            return render_template('error.html', error="Question 6 not a valid number")
    except:
        return render_template('error.html', error="Question 6 not a valid number")
    q6 = num2pattern(q6)

    q7 = request.form['q7']
    if q7 is None or len(q7) == 0:
        return render_template('error.html', error="Question 7 not set")
    try:
        q7 = int(q7)
        if q7 < 1 or q7 > 10:
            return render_template('error.html', error="Question 7 not a valid number")
    except:
        return render_template('error.html', error="Question 7 not a valid number")
    q7 = num2pattern(q7)

    q8 = request.form['q8']
    if q8 is None or len(q8) == 0:
        return render_template('error.html', error="Question 8 not set")
    if q8 == "yes":
        q8 = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
    else:
        q8 = [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0]

    q9 = request.form['q9']
    if q9 is None or len(q9) == 0:
        return render_template('error.html', error="Question 9 not set")
    try:
        q9 = int(q9)
        if q9 < 0 or q9 > 24:
            return render_template('error.html', error="Question 9 not a valid number")
    except:
        return render_template('error.html', error="Question 9 not a valid number")
    q9 = num2pattern(q9)

    q10 = request.form['q10']
    if q10 is None or len(q10) == 0:
        return render_template('error.html', error="Question 10 not set")
    try:
        q10 = int(q10)
        if q10 < 1 or q10 > 10:
            return render_template('error.html', error="Question 10 not a valid number")
    except:
        return render_template('error.html', error="Question 10 not a valid number")
    q10 = num2pattern(q10)

    q = [nickname, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    queue.append(q)
    print "q=%s" % q
    print len(queue)
    return render_template('thankyou.html', nickname= nickname, id=len(queue)-1)

@app.route('/admin')
def Admin():
    return app.send_static_file('admin.html')


@app.route('/random')
def Random():
    name = random.randint(1000,9999)
    for i in range(23):
        nickname = "%d-%d" % (name, i)
        q1=num2pattern(random.randint(1, 10))
        q2=num2pattern(random.randint(1, 10))
        q3=num2pattern(random.randint(1, 10))
        q4=num2pattern(random.randint(1, 10))
        q5=num2pattern(random.randint(1, 10))
        q6=num2pattern(random.randint(1, 10))
        q7=num2pattern(random.randint(1, 10))
        q8=random.choice([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]])
        q9=num2pattern(random.randint(1, 10))
        q10=num2pattern(random.randint(1, 10))
        q = [nickname, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
        queue.append(q)
    return "Done"


@app.route('/one')
def One():
    myid = int(request.args.get('id'))
    num = int(request.args.get('num'))
    one_image = np.zeros((num * 10, 100 , 1), np.uint8)
    for index in range(num):
        for i in range(10):
            for x in range(10):
                line = queue[myid][x + 1]
                for y in range(10):
                    one_image[(index * 10) + x, (i * 10) + y] = line[y]
    cv2.imwrite("static/one-%d.png" % myid, one_image)
    d = {}
    d['nickname'] = queue[myid][0]
    d['name'] = "one-%d.png" % myid
    d['id'] = myid
    d['num'] = num
    return render_template("one.html", data=d)


@app.route('/result')
def Result():
    index = 0
    r = []
    complete_image = np.zeros((len(queue) * 10, 100, 1), np.uint8)
    for user in queue:
        nickname = user[0]
        blank_image = np.zeros((10, 100, 1), np.uint8)
        try:
            for i in range(10):
                for x in range(10):
                    line = user[x + 1]
                    for y in range(10):
                        blank_image[x, (i * 10) + y] = line[y]
                        complete_image[(index * 10) + x, (i * 10) + y] = line[y]
        except:
            print "Error with data:%s" % user
        name = "nitting-%d.png" % index
        cv2.imwrite("static/%s" % name, blank_image)
        d = {}
        d['nickname'] = nickname
        d['name'] = name
        d['id'] = index
        r.append(d)
        index += 1
    cv2.imwrite("static/complete.png", complete_image)
    return render_template("result.html", data=r)


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    random.seed()
    port = os.getenv('PORT', '5000')
    app.run(host='0.0.0.0', port=int(port))
