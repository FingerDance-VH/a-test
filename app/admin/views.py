from flask import Blueprint,render_template
#创建蓝图对象
admin_bp = Blueprint('admin',__name__,url_prefix='/admin')

@admin_bp.route('/')
def index():
    return render_template('admin/index.html')