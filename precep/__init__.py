from flask import Flask, render_template, url_for, request

def create_app():
    
    app = Flask(__name__)

    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'devprece'
    )
    
    from . import prece
    app.register_blueprint(prece.bp)

    @app.route('/')
    def index():
        return render_template('index.html')


    return app