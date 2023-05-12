from flask import Flask, render_template, request, redirect, session, flash
from weather_util import get_weather, get_weather_by_coord
import crawl_util_melon as cu
import map_util as mu
import image_util as iu
import os, random, json

app = Flask(__name__)

@app.route("/melon")
def melon():
    song_list = cu.melon()
    return render_template("prototype/melon2.html", song_list=song_list)

if __name__ == '__main__':
    app.run(debug=True)
#



# @app.route("/melon")
# def melon():
#     menu = {"ho": 0, "us": 0, "cr": 1, "sc": 0}
#     song_list = cu.nie()
#     return render_template("prototype/melon.html", song_list=song_list, menu=menu, weather=get_weather(app), 
#         quote=quote, addr=addr)