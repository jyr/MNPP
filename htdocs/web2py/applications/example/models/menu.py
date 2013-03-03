# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application
response.subtitle = T('customize me!')

#http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'you'
response.meta.description = 'Free and open source full-stack enterprise framework for agile development of fast, scalable, secure and portable database-driven web-based applications. Written and programmable in Python'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Enterprise Framework'
response.meta.copyright = 'Copyright 2007-2010'


##########################################
## this is the main application menu
## add/remove items as required
##########################################

response.menu = [
    (T('Home'), False, URL('default','index'), [])
    ]

##########################################
## this is here to provide shortcuts
## during development. remove in production
##
## mind that plugins may also affect menu
##########################################

#########################################
## Make your own menus
##########################################

response.menu+=[
    (T('This App'), False, URL('admin', 'default', 'design/%s' % request.application),
     [
            (T('Controller'), False,
             URL('admin', 'default', 'edit/%s/controllers/%s.py' \
                     % (request.application,request.controller=='appadmin' and
                        'default' or request.controller))),
            (T('View'), False,
             URL('admin', 'default', 'edit/%s/views/%s' \
                     % (request.application,response.view))),
            (T('Layout'), False,
             URL('admin', 'default', 'edit/%s/views/layout.html' \
                     % request.application)),
            (T('Stylesheet'), False,
             URL('admin', 'default', 'edit/%s/static/base.css' \
                     % request.application)),
            (T('DB Model'), False,
             URL('admin', 'default', 'edit/%s/models/db.py' \
                     % request.application)),
            (T('Menu Model'), False,
             URL('admin', 'default', 'edit/%s/models/menu.py' \
                     % request.application)),
            (T('Database'), False,
             URL(request.application, 'appadmin', 'index')),

            (T('Errors'), False,
             URL('admin', 'default', 'errors/%s' \
                     % request.application)),

            (T('About'), False,
             URL('admin', 'default', 'about/%s' \
                     % request.application)),

            ]
   )]


##########################################
## this is here to provide shortcuts to some resources
## during development. remove in production
##
## mind that plugins may also affect menu
##########################################


response.menu+=[(T('Resources'), False, None,
     [
    (T('Documentation'), False, 'http://www.web2py.com/book',
        [
        (T('Preface'), False, 'http://www.web2py.com/book/default/chapter/00'),
        (T('Introduction'), False, 'http://www.web2py.com/book/default/chapter/01'),
        (T('Python'), False, 'http://www.web2py.com/book/default/chapter/02'),
        (T('Overview'), False, 'http://www.web2py.com/book/default/chapter/03'),
        (T('The Core'), False, 'http://www.web2py.com/book/default/chapter/04'),
        (T('The Views'), False, 'http://www.web2py.com/book/default/chapter/05'),
        (T('Database'), False, 'http://www.web2py.com/book/default/chapter/06'),
        (T('Forms and Validators'), False, 'http://www.web2py.com/book/default/chapter/07'),
        (T('Access Control'), False, 'http://www.web2py.com/book/default/chapter/08'),
        (T('Services'), False, 'http://www.web2py.com/book/default/chapter/09'),
        (T('Ajax Recipes'), False, 'http://www.web2py.com/book/default/chapter/10'),
        (T('Deployment Recipes'), False, 'http://www.web2py.com/book/default/chapter/11'),
        (T('Other Recipes'), False, 'http://www.web2py.com/book/default/chapter/12'),
        (T('Buy this book'), False, 'http://stores.lulu.com/web2py'),
        ]),

    (T('Community'), False, None,
        [
        (T('Groups'), False, 'http://www.web2py.com/examples/default/usergroups'),
        (T('Twitter'), False, 'http://twitter.com/web2py'),
        (T('Live chat'), False, 'http://mibbit.com/?channel=%23web2py&server=irc.mibbit.net'),
        (T('User Voice'), False, 'http://web2py.uservoice.com/'),
        ]),

    (T('Web2py'), False, 'http://www.web2py.com',
        [
        (T('Download'), False, 'http://www.web2py.com/examples/default/download'),
        (T('Support'), False, 'http://www.web2py.com/examples/default/support'),
        (T('Quick Examples'), False, 'http://web2py.com/examples/default/examples'),
        (T('FAQ'), False, 'http://web2py.com/AlterEgo'),
        (T('Free Applications'), False, 'http://web2py.com/appliances'),
        (T('Plugins'), False, 'http://web2py.com/plugins'),
        (T('Recipes'), False, 'http://web2pyslices.com/'),
        (T('Demo'), False, 'http://web2py.com/demo_admin'),
        (T('Semantic'), False, 'http://web2py.com/semantic'),
        (T('Layouts'), False, 'http://web2py.com/layouts'),
        (T('Videos'), False, 'http://www.web2py.com/examples/default/videos/'),
        ]),
    ]
   )]
