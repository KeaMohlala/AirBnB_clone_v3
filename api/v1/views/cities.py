#!/usr/bin/python3
"""
new view for City objects that handles all default RESTful
API actions
"""
from flask import jsonify, abort, make_response, request
from models.city import City
from models.state import State
from models import storage
from api.v1.views import app_views


@app_views.route('/api/v1/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id):
    """retrieves list of all city objects"""
    city_list = []
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    for city in state.cities:
        city_list.append(city.to_dict())
    return jsonify(city_list)


@app_views.route('/api/v1/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city(city_id):
    """Retrieves a City object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/api/v1/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city(city_id):
    """deletes city object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/api/v1/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def post_city(state_id):
    """creates a City object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    data = request.get_json()
    new_city = City(**data)
    new_city.state_id = state.id
    new_city.save()
    return make_response(jsonify(new_city.to_dict()), 201)


@app_views.route('/api/v1/cities/<city_id>', methods=['PUT'],
                 strict_slashes=False)
def update_city(city_id):
    """updates a City object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'state_id', 'created_at', 'updated_at']
    data = request.get_json()
    for key, value in data.items():
        if key != not in ignore:
            setattr(city, key, value)
    storage.save()
    return make_response(jsonify(city.to_dict()), 200)
