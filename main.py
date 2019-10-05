from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   flash,
                   session)

from functions import (register_user,
                       check_login_status,
                       get_ideas,
                       save_idea
                       )


app = Flask(__name__)
app.secret_key = 'secret key'


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()

        answer = check_login_status(username, password)

        if answer == "success":
            flash(f"სალამი, {username}. დღეს რა იდეები გაქვს?")

            ideas = get_ideas()
            return render_template("main.html", ideas=ideas)
        else:
            if answer == "incorrect password":
                message = "პაროლი არასწორია"
            else:
                message = f"მომხმარებელი {username} არ მოიძებნა"
        flash(message)
    return render_template("index.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()

        if not (username and password) :
            message = "სახელი და პაროლი უნდა იყოს მინიმუმ 1 სიმბოლო"
        else:
            answer = register_user(username, password)

            if answer == "username is taken":
                message = ("სამწუხაროდ, მომხმარებელი "
                          f"სახელით {username} უკვე არსებობს")
            else:
                flash(f"გილოცავ, {username}, რეგისტრაცია წარმატებით დასრულდა!")
                return render_template("index.html")
        flash(message)
    return render_template("register.html")


@app.route("/save_idea", methods=['POST'])
def add_idea():
    title = request.form.get("title")
    tag = request.form.get("tag")
    text = request.form.get("text")
    if all((title, tag, text)):
        save_idea({"title": title,
                   "tag": tag,
                   "text": text})
        message = "გილოცავ, იდეა წარმატებით დაემატა"
    else:
        message = ("იდეის შესანახად მინიმუმ 1 "
                   "სიმბოლო მაინც გვჭირდება თითოეულ ველში")
    flash(message)
    return render_template("main.html", ideas=get_ideas())


@app.route("/main")
def main():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
