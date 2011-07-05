#!/Applications/MNPP/Library/python26/bin/python
import web

urls = ("/", "index")
app = web.application(urls, globals())

class index:
    def GET(self):
        return 'Hello, worldssss from webpy!'

#if __name__ == "__main__":
#    app.run()

app = app.wsgifunc()

