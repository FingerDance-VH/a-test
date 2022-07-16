from app import app,db
from flask import render_template,request
from app.mysql import *

@app.route("/")
def root():
    return render_template("login.html")

@app.route("/temp",methods=['GET','POST'])
def temp():
    name = request.form.get('un')
    pwd = request.form.get('pwd')
    if User.query.filter(User.name == name,User.password == pwd).all():
        return 'success to load!'
    else:
        return 'That account does not exist.'


if __name__ == '__main__':
    # 清除数据库中的所有数据
    db.drop_all()
    # 创建所有的表
    db.create_all()
    app.run(debug=True)