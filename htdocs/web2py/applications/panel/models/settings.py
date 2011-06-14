# coding: utf8

from gluon.tools import *


mail = Mail()                                  
auth = Auth(globals(),db)                      
crud = Crud(globals(),db)                      
service = Service(globals())                   
plugins = PluginManager()


mail.settings.server = 'logging' #'smtp.gmail.com:587'  
#mail.settings.sender = 'nekrox@gmail.com'         
#mail.settings.login = 'nekrox@password'     

auth.settings.hmac_key = 'sha512:9d5fa437-0bf2-47e0-9c59-44163e46fcc6'   
auth.define_tables()                           
auth.settings.mailer = mail                    
auth.settings.create_user_groups = False
auth.settings.actions_disabled.append('register')
auth.settings.formstyle = 'divs'
auth.settings.remember_me_form = False

crud.settings.auth = None
crud.settings.formstyle = 'divs'
