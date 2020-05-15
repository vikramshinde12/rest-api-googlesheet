import logging
import gspread
import json

from flask import Blueprint
from oauth2client.service_account import ServiceAccountCredentials

api_sheet = Blueprint('api',__name__, url_prefix='/api')
scope = ['https://www.googleapis.com/auth/drive']
service_account_path = 'app/credentials/client-secret.json'

logging.getLogger().setLevel(logging.INFO)


@api_sheet.route('/<id>', methods=['GET'])
def api_get(id):
    logging.info('Getting the id {}'.format(id))
    record = get_record(id)
    return json.dumps(record)


def get_client():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(service_account_path, scope)
    client = gspread.authorize(credentials)
    return client


def get_record(id):
    client = get_client()
    sheet = client.open('googlesheet-python').sheet1
    # client.open_by_url()
    data = sheet.get_all_records()

    for d in data:
        if d['id'] == int(id):
            return d
