from app import app


@app.route("/")
def index():
    return "This is a basic API server created for my <a href=\"https://github.com/ChristopherLi05/CSC207-Project\">CSC207 Project</a><br>Here is the <a href=\"\">source code</a>"
