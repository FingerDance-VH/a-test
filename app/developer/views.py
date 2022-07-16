from flask import Blueprint,render_template
#创建蓝图对象
dev_bp = Blueprint('developer',__name__,url_prefix='/developer')

@dev_bp.route('/')
def index():
    return render_template('developer/index.html',times=123456,dic={'a':111,'b':222})