document.getElementById("blueTeam").textContent = localStorage.getItem("blue")
document.getElementById("blueScore").textContent = localStorage.getItem("blueScore")
document.getElementById("redTeam").textContent = localStorage.getItem("red")
document.getElementById("redScore").textContent = localStorage.getItem("redScore")
document.getElementById("draft_game").textContent = "Game " + localStorage.getItem("game")
document.getElementById("draft_patch").textContent = "Patch " + localStorage.getItem("patch")