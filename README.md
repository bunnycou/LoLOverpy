# LoLOverpy
Python based webserver for adding a very simple overlay for casting league of legends

## How to use
### run `loloverlay.bat`
- This will start the flask server on your pc

### Add `http://127.0.0.1:5000/game` to your obs as a browser source
- Make sure to make the width and height 2000x2000 (just larger than 1920x1080)
- `http://127.0.0.1:5000/game` is for in game, `http://127.0.0.1:500/draft` can be used for when in draft

### Add a custom browser dock or open a browser and goto `http://127.0.0.1:5000/submit`
- This page allows you to edit the displayed content.

## Notes
- This overlay was designed specifically for 1920x1080 streams, does not work with other resolutions
- This overlay was designed for the purpose of doing Best of 3 so it includes scores and game number. 