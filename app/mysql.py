from app import db

class User(db.Model):
    __tablenmae__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128),nullable=False)
    gender = db.Column(db.String(4))
    # 定义显示信息，定义之后，查询时显示对象的时候更直观
    def __repr__(self):
        return 'User object: name=%s' % self.name
