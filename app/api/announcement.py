from . import api
from ..models import Announcement
from flask import jsonify


@api.route('/announcement/')
def get_announcement():
    content = Announcement.query.first()
    return jsonify(content.to_json())
