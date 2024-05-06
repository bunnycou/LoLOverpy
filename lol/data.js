var blue = localStorage.getItem("blue")
var blueScore =  localStorage.getItem("blueScore")
var red = localStorage.getItem("red")
var redScore = localStorage.getItem("redScore")
var patch = localStorage.getItem("patch")

if (blue == null) {
    blue == "Blue"
}

if (blueScore == null) {
    blueScore = 0
}

if (red == null) {
    red == "Red"
}

if (redScore == null) {
    redScore = 0
}

if (patch == null) {
    patch == "Latest"
}

document.getElementById("blue").value = blue
document.getElementById("blueScore").value = blueScore
document.getElementById("red").value = red
document.getElementById("redScore").value = redScore
document.getElementById("patch").value = patch

document.getElementById("form").onsubmit = storeVars

function storeVars() {
    let blueVar = document.getElementById("blue").value
    let blueScoreVar = document.getElementById("blueScore").value
    let redVar = document.getElementById("red").value
    let redScoreVar = document.getElementById("redScore").value
    let patchVar = document.getElementById("patch").value
    let swapVar = document.getElementById("swap").checked
    
    if (swapVar) {
        var tmp
        tmp = redVar
        redVar = blueVar
        blueVar = tmp

        tmp = redScoreVar
        redScoreVar = blueScoreVar
        blueScoreVar = tmp
    }

    localStorage.setItem("blue", blueVar)
    localStorage.setItem("blueScore", blueScoreVar)
    localStorage.setItem("red", redVar)
    localStorage.setItem("redScore", redScoreVar)
    localStorage.setItem("game", parseInt(blueScoreVar)+parseInt(redScoreVar)+1)
    localStorage.setItem("patch", patchVar)
}