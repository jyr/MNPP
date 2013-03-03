# coding: utf8

def index(): 
    return dict(message=T('Hello World'))
    
    
def user(): 
    return dict(form=auth())
