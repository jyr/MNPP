import smtplib


def email_auth(server="smtp.gmail.com:587",
               domain="@gmail.com"):
    """
    to use email_login:
    from gluon.contrib.login_methods.email_auth import email_auth
    auth.settings.login_methods.append(email_auth("smtp.gmail.com:587",
                                                  "@gmail.com"))
    """

    def email_auth_aux(email,
                       password,
                       server=server,
                       domain=domain):
        if domain:
            if not isinstance(domain,(list,tuple)):
                domain=[str(domain)]
            if not [d for d in domain if email[-len(d):]==d]:
                return False
        (host, port) = server.split(':')
        try:
            server = None
            server = smtplib.SMTP(host, port)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(email, password)
            server.quit()
            return True
        except:
            if server:
                server.quit()
            return False
    return email_auth_aux
