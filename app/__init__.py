from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__) #创建Flask对象

from config import * #导入数据库配置
app.config.from_object(Config)#配置数据库sqlalchemy

#导入蓝图
from app.admin.views import admin_bp 
from app.developer.views import dev_bp
#注册蓝图
app.register_blueprint(admin_bp)
app.register_blueprint(dev_bp)

# 创建数据库SQLAlchemy的工具对象
db = SQLAlchemy(app)
