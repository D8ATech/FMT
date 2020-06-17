from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Craig'}
    return '''
<html>
    <head>
        <title>Home Page Microblog</title>
    </head>
    <body>    
        <h1>Hello ''' + user['username'] + '''! Would you like to play a game?</h1>
    </body>
</html>'''
