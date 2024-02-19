# LoLOverpy
Python based webserver for adding a very simple overlay for casting league of legends or smash in OBS or other programs

## How to use
### run `overpy.bat`
- This will start the flask server on your pc

### Add `http://127.0.0.1:5000/lolgame` or `http://127.0.0.1:5000/smash` to your obs as a browser source
- Make sure to make the width and height 2000x2000 (just larger than 1920x1080)
- `http://127.0.0.1:5000/lolgame` is for in game, `http://127.0.0.1:500/loldraft` can be used for when in League draft

### Add a custom browser dock or open a browser and goto `http://127.0.0.1:5000/lolsubmit` or `/smashsubmit`
- This page allows you to edit the displayed content.

## Notes
- This overlay was designed specifically for 1920x1080 streams, does not work with other resolutions
- This overlay was designed for the purpose of doing Best of 3 so it includes scores and game number. 