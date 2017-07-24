# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, jsonify, request
from werkzeug.exceptions import NotFound, BadRequest, Forbidden
from voluptuous import Schema, Required, Optional, validators, MultipleInvalid

from micromailer.mailing import send_email

blueprint = Blueprint('emails', __name__, url_prefix='/emails')


EmailSchema = Schema(
    {
        Required('to'): basestring,
        Required('plain_content'): basestring,
        Optional('title', default=""): basestring,
        Optional('rich_content', default=None): basestring,
    }
)


@blueprint.route('/', methods=['POST'])
def send_mail():
    """Sends an emails"""
    try:
        email = EmailSchema(request.get_json() or request.form)
    except MultipleInvalid as exc:
        raise BadRequest(exc)

    send_email(to_=email['to'], title=email['title'],
               plain_content=email['plain_content'],
               rich_content=email['rich_content'])
    return jsonify(success=True, message='Email registered for processing')

