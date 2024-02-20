from flask import Flask, render_template, request
from math import ceil
import time

app = Flask(__name__)

#LoL vars
LoL_blue="UT"
LoL_red="UT"
LoL_blueScore="0"
LoL_redScore="0"
LoL_patch="14.1"
LoL_game="1"

#Smash Vars
Smash_red="UT"
Smash_blue="UT"
Smash_redScore="0"
Smash_blueScore="0"
Smash_redStocks=12
Smash_blueStocks=12
Smash_redPlayerCount=""
Smash_bluePlayerCount=""

empty_circle = "○"
filled_circle = "●"

#LoL Pages
@app.route("/lolgame")
def lolgame():
    return render_template("lol_game.html", blue=LoL_blue, red=LoL_red, blueScore=LoL_blueScore, redScore=LoL_redScore, patch=LoL_patch, game=LoL_game)

@app.route("/loldraft")
def loldraft():
    return render_template("lol_draft.html", blue=LoL_blue, red=LoL_red, blueScore=LoL_blueScore, redScore=LoL_redScore, patch=LoL_patch, game=LoL_game)

@app.route("/lolsubmit", methods=['Get','POST'])
def lolsubmit():
    global LoL_blue, LoL_red, LoL_blueScore, LoL_redScore, LoL_patch, LoL_game
    if request.method == 'POST':
        LoL_blue=request.form['blue']
        LoL_red=request.form['red']
        LoL_blueScore=request.form['blueScore']
        LoL_redScore=request.form['redScore']
        LoL_patch=request.form['patch']
        LoL_game=request.form['game']
        swap = request.form.get("swap")
        if swap:
            LoL_blue, LoL_red = LoL_red, LoL_blue
            LoL_blueScore, LoL_redScore = LoL_redScore, LoL_blueScore
        return render_template("lol_submit.html", blue=LoL_blue, red=LoL_red, blueScore=LoL_blueScore, redScore=LoL_redScore, patch=LoL_patch, game=LoL_game, time="Updated at "+time.strftime("%H:%M:%S"))
    else:
        return render_template("lol_submit.html", blue=LoL_blue, red=LoL_red, blueScore=LoL_blueScore, redScore=LoL_redScore, patch=LoL_patch, game=LoL_game, time="")
    
#Smash Pages
@app.route("/smash")
def smash():
    Smash_redPlayerCount = redPlayerCt()
    Smash_bluePlayerCount = bluePlayerCt()
    return render_template("smash_game.html", blue=Smash_blue, red=Smash_red, blueScore=Smash_blueScore, redScore=Smash_redScore, blueStocks=Smash_blueStocks, redStocks=Smash_redStocks, bluePlayerCount=Smash_bluePlayerCount, redPlayerCount=Smash_redPlayerCount)

def redPlayerCt():
    ret = ""
    players = playerCt(Smash_redStocks)
    elim = 4-players
    for i in range(players):
        ret += filled_circle + " "
    for i in range(elim):
        ret += empty_circle + " "
    return ret.strip()

def bluePlayerCt():
    ret = ""
    players = playerCt(Smash_blueStocks)
    elim = 4-players
    for i in range(elim):
        ret += empty_circle + " "
    for i in range(players):
        ret += filled_circle + " "
    return ret.strip()

def playerCt(stocks):
    return ceil(stocks/3)

@app.route("/smashbrb")
def smashbrb():
    Smash_redPlayerCount = redPlayerCt()
    Smash_bluePlayerCount = bluePlayerCt()
    return render_template("smash_brb.html", blue=Smash_blue, red=Smash_red, blueStocks=Smash_blueStocks, redStocks=Smash_redStocks, bluePlayers=Smash_bluePlayerCount, redPlayers=Smash_redPlayerCount)

@app.route("/smashsubmit", methods=['Get','POST'])
def smashsubmit():
    global Smash_red, Smash_redScore, Smash_redStocks, Smash_blue, Smash_blueScore, Smash_blueStocks
    if request.method == "POST":
        Smash_red = request.form["red"]
        Smash_redScore = request.form["redScore"]
        Smash_redStocks = int(request.form["redStocks"])
        Smash_blue = request.form["blue"]
        Smash_blueScore = request.form["blueScore"]
        Smash_blueStocks = int(request.form["blueStocks"])
        swap = request.form.get("swap")
        if swap:
            Smash_red, Smash_blue = Smash_blue, Smash_red
            Smash_redScore, Smash_blueScore = Smash_blueScore, Smash_redScore
            Smash_redStocks, Smash_blueStocks = Smash_blueStocks, Smash_redStocks
        return render_template("smash_submit.html", red=Smash_red, redScore=Smash_redScore, redStocks=Smash_redStocks, blue=Smash_blue, blueScore=Smash_blueScore, blueStocks=Smash_blueStocks, time="Updated at "+time.strftime("%H:%M:%S"))
    else:
        return render_template("smash_submit.html", red=Smash_red, redScore=Smash_redScore, redStocks=Smash_redStocks, blue=Smash_blue, blueScore=Smash_blueScore, blueStocks=Smash_blueStocks, time="")