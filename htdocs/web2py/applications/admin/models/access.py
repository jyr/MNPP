from gluon.admin import apath
# ###########################################################
# ## make sure administrator is on localhost or https
# ###########################################################

http_host = request.env.http_host.split(':')[0]

if request.env.web2py_runtime_gae:
    session_db = DAL('gae')
    session.connect(request, response, db=session_db)
    hosts = (http_host, )
else:
    hosts = (http_host, socket.gethostname(),
             socket.gethostbyname(http_host),
             '::1','127.0.0.1','::ffff:127.0.0.1')

remote_addr = request.env.remote_addr

if request.env.http_x_forwarded_for \
        or request.env.wsgi_url_scheme in ['https', 'HTTPS'] \
        or request.env.https == 'on':
    session.secure()
elif not remote_addr in hosts and not DEMO_MODE:
    raise HTTP(200, T('Admin is disabled because insecure channel'))

try:
    _config = {}
    port = int(request.env.server_port or 0)
    restricted(open(apath('../parameters_%i.py' % port, request), 'r').read(), _config)

    if not 'password' in _config or not _config['password']:
        raise HTTP(200, T('admin disabled because no admin password'))
except IOError:
    import gluon.fileutils
    if request.env.web2py_runtime_gae:
        if gluon.fileutils.check_credentials(request):
            session.authorized = True
            session.last_time = time.time()
        else:
            raise HTTP(200,
                       T('admin disabled because not supported on google app engine'))
    else:
        raise HTTP(200, T('admin disabled because unable to access password file'))


def verify_password(password):
    session.pam_user = None
    if DEMO_MODE:
        return True
    elif not 'password' in _config:
        return False
    elif _config['password'].startswith('pam_user:'):
        session.pam_user = _config['password'][9:].strip()
        import gluon.contrib.pam
        return gluon.contrib.pam.authenticate(session.pam_user,password)
    else:
        return _config['password'] == CRYPT()(password)[0]



# ###########################################################
# ## session expiration
# ###########################################################

t0 = time.time()
if session.authorized:

    if session.last_time and session.last_time < t0 - EXPIRATION:
        session.flash = T('session expired')
        session.authorized = False
    else:
        session.last_time = t0

if not session.authorized and not \
    (request.controller == 'default' and \
     request.function in ('index','user')):

    if request.env.query_string:
        query_string = '?' + request.env.query_string
    else:
        query_string = ''

    url = request.env.path_info + query_string
    redirect(URL(request.application, 'default', 'index', vars=dict(send=url)))
elif session.authorized and \
     request.controller == 'default' and \
     request.function == 'index':
    redirect(URL(request.application, 'default', 'site'))


if request.controller=='appadmin' and DEMO_MODE:
    session.flash = 'Appadmin disabled in demo mode'
    redirect(URL('default','sites'))

