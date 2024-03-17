import flask
from flask import jsonify, make_response, request
from . import db_session
from .users import User


blueprint = flask.Blueprint(
    'user_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'user':
                [item.to_dict(only=('id', 'name', 'surname', 'age', 'address', 'position', 'speciality',
                                    'about', 'email'))
                 for item in users]
        }
    )


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'user': user.to_dict(only=(
                'id', 'name', 'surname', 'age', 'address', 'position', 'speciality',
                'about', 'email'
            ))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def add_user():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['name', 'surname', 'age', 'address',
                  'position', 'speciality', 'about', 'email']):
        return make_response(jsonify({'error': 'Bad Request'}), 400)
    db_sess = db_session.create_session()
    user = User(
        name=request.json['name'],
        surname=request.json['surname'],
        age=request.json['age'],
        address=request.json['address'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        about=request.json['about'],
        email=request.json['email']
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'id': user.id})


@blueprint.route('/api/users/<int:user_id>', methods=['POST'])
def edit_user(user_id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['name', 'surname', 'age', 'address',
                  'position', 'speciality', 'about', 'email']):
        return make_response(jsonify({'error': 'Bad Request'}), 400)
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()
    user.name = request.json['name']
    user.surname = request.json['surname']
    user.age = request.json['age']
    user.address = request.json['address']
    user.position = request.json['position']
    user.speciality = request.json['speciality']
    user.about = request.json['about']
    user.email = request.json['email']
    db_sess.commit()
    return jsonify({'id': user.id})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})