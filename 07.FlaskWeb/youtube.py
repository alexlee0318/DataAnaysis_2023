from flask import Flask, render_template
import crawl_util_youtube as cu

app = Flask(__name__)

@app.route("/youtube_ranking")
def youtube():
    youtube_list = cu.youtube()
    return render_template("prototype/youtube.html", youtube_list=youtube_list)

# @app.route("/youtube20")
# def youtube20():
#     youtube_list = cu.youtube()
#     return render_template("prototype/youtube20.html", youtube_list=youtube_list)

# @app.route("/youtube15")
# def youtube20():
#     youtube_list = cu.youtube()
#     return render_template("prototype/youtube20.html", youtube_list=youtube_list)

if __name__ == '__main__':
    app.run(debug=True)