import logging
import gspread
import json
import os

from flask import Flask

app = Flask(__name__)

service_account_path = 'app/credentials/client-secret.json'
logging.getLogger().setLevel(logging.INFO)


@app.route('/<id>', methods=['GET'])
def api_get(id):
    logging.info('Getting the id {}'.format(id))
    record = get_record(id)
    return json.dumps(record)


def get_client():
    return gspread.service_account(service_account_path)


def get_record(id):
    client = get_client()
    sheet = client.open_by_key(os.environ.get('SHEET_ID')).sheet1
    data = sheet.get_all_records()

    for d in data:
        if d['id'] == int(id):
            return d


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')