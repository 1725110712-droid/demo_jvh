import web

urls = (
    '/', 'index'
)
app = web.application(urls, globals())

class index:
    def GET(self):
        return 'Hola mundo desde web.py'

if __name__ == "__main__":
    app.run()
