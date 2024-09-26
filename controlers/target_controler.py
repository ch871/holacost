from flask import Blueprint, jsonify
from dictalchemy.utils import asdict
from sqlalchemy import inspect

from repository.target_repository import find_target_by_id,get_all_targets

target_bluprint = Blueprint("mission", __name__)


@target_bluprint.route("/<int:target_id>", methods=['GET'])
def get_by_id(target_id):
    target = find_target_by_id(target_id).value_or("")
    if target is not "":
        return jsonify(asdict(target)), 200
    else:
        return jsonify({}), 400


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}


@target_bluprint.route('/', methods=['GET'])
def get_all():
    targets = get_all_targets()
    if targets:
        return jsonify([asdict(x) for x in get_all_targets()]), 200
    return jsonify([]), 404
