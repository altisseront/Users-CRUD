from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import User
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    return redirect("/users")

@app.route('/users')
def displayUsers():
    
    return render_template("read_all.html", all_users = User.get_all())

@app.route('/create_user', methods=["POST"])
def createUser():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
        }
    User.save(data)
    x = User.getUserID(data)[0]['id'];
    print (f"=============================================== {x}");
    return redirect(f'/users/{x}')

@app.route('/users/new')
def displayCreate():
    return render_template("create.html")

@app.route('/redir', methods=['POST'])
def redir():
    return redirect('/users/new')

@app.route('/home', methods = ['POST'])
def home():
    return redirect('/users')

@app.route('/update_user/<int:x>', methods = ['POST'])
def updateUser(x):
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "id" : x
        }
    User.update(data)
    return redirect (f'/users/{x}')

@app.route('/users/<int:x>')
def showUserx(x):
    data = {"id" : x}
    theuser = User.oneUser(data)
    print(f'========{theuser}')
    return render_template('show.html', theuser = theuser)

@app.route('/users/<int:x>/edit')
def editUserx(x):
    return render_template('update.html', x=x)

@app.route('/users/<int:x>/delete')
def deleteUserx(x):
    data = {
    "id": x,
    }
    User.delete(data)
    return redirect('/users')