import web

urls = (
    '/', 'Index',
    '/parametros', 'Parametros'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()
class Parametros:
    def GET(self):
        titulo = "Título desde python"
        descripcion = """alkndklnalefaefnlahfe"""
        return render.parametros(titulo,descripcion)

if __name__ == "__main__":
    app.run()