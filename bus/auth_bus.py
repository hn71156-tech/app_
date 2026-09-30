from dal import auth_dal

def login(u, p):
    return auth_dal.login(u, p)
