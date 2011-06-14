# coding: utf8

def index(): 
    return dict(message=T('Hello World'))
    
    
def user(): 
    response.menu = []
    return dict(form=auth())
