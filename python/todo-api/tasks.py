#!/home/siyer/workspace/venv/bin/python

from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()


tasks = [
    {
        'id' : 1,
        'title' : 'Make samosa',
        'description' : 'Boil potatos, green peas and make the filling',
        'done' : False
    },
    {
        'id' : 2,
        'title' : 'Study',
        'description' : 'Python, scala, algorithms',
        'done' : False

    }
]

@auth.get_password
def get_password(username):
    if username == 'siyer':
        return 'flask'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'unauthorized access'}),401)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
@auth.login_required
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) ==0:
        abort(404)
    return jsonify({'tasks':task[0]})

if __name__ == '__main__':
    app.run(debug=True)
