# ###########################################################
# ## generate menu
# ###########################################################

_a = request.application
_c = request.controller
_f = request.function
response.title = '%s %s' % (_f, '/'.join(request.args))
response.subtitle = 'admin'
response.menu = [(T('site'), _f == 'site', URL(_a,'default','site'))]

if request.args:
    _t = request.args[0]
    response.menu.append((T('edit'), _c == 'default' and _f == 'design',
                         URL(_a,'default','design',args=_t)))
    response.menu.append((T('about'), _c == 'default' and _f == 'about',
                         URL(_a,'default','about',args=_t)))
    response.menu.append((T('errors'), _c == 'default' and _f == 'errors',
                         URL(_a,'default','errors',args=_t)))

    response.menu.append((T('versioning'),
                          _c == 'mercurial' and _f == 'commit',
                          URL(_a,'mercurial','commit',args=_t)))

if not session.authorized:
    response.menu = [(T('login'), True, '')]
else:
    response.menu.append((T('logout'), False,
                          URL(_a,'default',f='logout')))

response.menu.append((T('help'), False, URL('examples','default','index')))

