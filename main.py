from bottle import route, run, view

@route('/')
@view("templates/default.tpl")
def default():
    return {"title":"Default"}

@route('/club')
@view("templates/club.tpl")
def default():
    stri = """
    <h2>club</h2>
    """
    return {"title":"Club", "body" : stri}

@route('/contact')
@view("templates/contact.tpl")
def default():
    stri = """
    <h2>contact</h2>
    """
    return {"title":"Contact", "body" : stri}

@route('/media')
@view("templates/media.tpl")
def default():
    stri = """
    <h2>media</h2>
    """
    return {"title":"Media", "body" : stri}

@route('/news')
@view("templates/news.tpl")
def default():
    stri = """
    <h2>news</h2>
    """
    return {"title":"News", "body" : stri}

@route('/teams')
@view("templates/teams.tpl")
def default():
    stri = """
    <h2>teams</h2>
    """
    return {"title":"Teams", "body" : stri}


run(host='localhost', port=8080, debug=True)