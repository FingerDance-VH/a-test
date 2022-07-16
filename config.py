class Config(object):
    # Python3中连接MySQL需要使用pymysql，连接格式如下：
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Fhy13420203185!@127.0.0.1:3306/test'
     # 数据跟踪，数据库中的表格式修改后，模型类会跟着自动修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时显示原始SQL语句
    SQLALCHEMY_ECHO = True
    # 每次请求结束后自动提交数据库中的改动
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True