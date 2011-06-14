# coding: utf8

if request.env.web2py_runtime_gae:            
    db = DAL('google:datastore')              
    session.connect(request, response, db = db)
else:  
    db = DAL('mysql://root:@localhost/web2py')
