from flask import Flask, render_template, request

app = Flask(__name__)

bt="UT"
rt="UT"
bs="0"
rs="0"
pn="14.1"
gn="1"

@app.route("/")
def index():
    # Path to your HTML file relative to the Python file
    return render_template("overlay.html", btAbr=bt, rtAbr=rt, btScr=bs, rtScr=rs, patchno=pn, gameno=gn)

@app.route("/submit", methods=['Get','POST'])
def submit():
    global bt, rt, bs, rs, pn, gn
    if request.method == 'POST':
        bt=request.form['btAbr']
        rt=request.form['rtAbr']
        bs=request.form['btScr']
        rs=request.form['rtScr']
        pn=request.form['patchno']
        gn=request.form['gameno']
        swap = request.form.get("swap")
        if swap:
            bt, rt = rt, bt
            bs, rs = rs, bs
    return render_template("submit.html", btAbr=bt, rtAbr=rt, btScr=bs, rtScr=rs, patchno=pn, gameno=gn)