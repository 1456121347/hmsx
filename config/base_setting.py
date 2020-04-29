SERVER_PORT = 9000
SQLALCHEMY_DATABASE_URI = 'mysql://root:xi19970410@127.0.0.1/hmsx_db?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Cookie 
AUTH_COOKIE_NAME = "hmsx_1903C"

# 设置拦截器忽略规则
IGNORE_URLS = [
    "^/user/login"
]
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

STATUS = {
    "1":"正常",
    "0":"已删除"
}