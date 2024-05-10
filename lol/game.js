let blueName = localStorage.getItem("blue")
let blueScore = localStorage.getItem("blueScore")
let redName = localStorage.getItem("red")
let redScore = localStorage.getItem("redScore")
let game = localStorage.getItem("game")
let patch = localStorage.getItem("patch")

if (!blueName) { blueName = "Blue" }
if (!blueScore) { blueScore = "0" }
if (!redName) { redName = "Red" }
if (!redScore) { redScore = "0" }
if (!game) { game = "Game 1" } else { game = "Game " + game }
if (patch == "Latest") { patch = "Latest Patch" } else if (!patch) { patch = "Latest Patch" } else { patch = "Patch " + patch }

document.getElementById("blueScore").textContent = blueScore
document.getElementById("redTeam").textContent = redName
document.getElementById("redScore").textContent = redScore
document.getElementById("game_game").textContent = game
document.getElementById("game_patch").textContent = patch