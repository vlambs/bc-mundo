from bottle import route, run, template

@route('/')
def default():
    return template('home')
    
@route('/club')
def club():
    return template('club')

@route('/contact')
def contact():
    return template('contact')

@route('/media')
def media():
    return template('media')

@route('/news')
def news():
    return template('news')

@route('/teams')
def teams():
    teams = [
        {
            'name': 'Team A',
            'members': [
                {'name': 'Alice', 'age': 23, 'height': 1.75, 'position': 'Forward'},
                {'name': 'Bob', 'age': 25, 'height': 1.8, 'position': 'Guard'},
                {'name': 'Charlie', 'age': 21, 'height': 1.82, 'position': 'Center'}
            ]
        },
        {
            'name': 'Team B',
            'members': [
                {'name': 'Dave', 'age': 27, 'height': 1.9, 'position': 'Forward'},
                {'name': 'Eve', 'age': 24, 'height': 1.65, 'position': 'Guard'}
            ]
        }
    ]
    return template('teams', teamsList=teams)


run(host='localhost', port=8080, debug=True)