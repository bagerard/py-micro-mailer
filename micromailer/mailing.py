import logging

from flask import current_app as app

from micromailer.extensions import mailer

LOG = logging.getLogger(__name__)


def _send_email(from_, to_, title, plain_content, rich_content=None):
    """Send an email

    :param mailer: Instance of the mailer to use
    :type mailer: Mailer
    :param from_: The email of the recipient
    :type from_: str
    :param to_: The email of the author
    :type to_: str
    :param title: The email title
    :type title: str
    :param plain_content: The plain/text content that is not enriched
    :type plain_content: str
    :param rich_content: Optional enriched HTML content that will be send in email body
    :type rich_content: str
    """
    message = mailer.new(author=from_,
                         to=to_,
                         subject=title,
                         plain=plain_content,
                         rich=rich_content)
    mailer.send(message)


def send_email(to_, title, plain_content, rich_content=None):
    """Formatting and sending an email with some hardcoded fields coming from the config file

    :param to_: The email of the recipient
    :type to_: str
    :param title: The title of the email
    :type title: str
    :param plain_content: The plain/text content that is not enriched
    :type plain_content: str
    :param rich_content: Optional enriched HTML content that will be send in email body
    :type rich_content: str
    """
    config = app.config
    from_ = config['NO_REPLY_CLUEPOINTS']
    _send_email(from_, to_, title, plain_content, rich_content)
