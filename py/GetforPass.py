import getpass
user = getpass.getuser()    #自动获取当前用户名
yourPas = getpass.getpass('input you password: ')
print(user, yourPas)