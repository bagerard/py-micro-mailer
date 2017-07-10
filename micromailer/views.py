# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, jsonify

from micromailer.mailing import send_email

blueprint = Blueprint('emails', __name__, url_prefix='/emails')


@blueprint.route('/', methods=['GET'])
def send_mail():
    """Sends an emails"""
    send_email(to_='testos@bob.com', title='MyTitle', plain_content='Blablablablabla')
    return jsonify(success=True, message='Email registered')

