import requests
import json
import time
import cx_Oracle


class RoadEvent:
    code = '860553'

    def get_request_url(self):
        url = 'http://api.jejuits.go.kr/api/infoRoadEventList'
        params = {'code': self.code}
        response = requests.get(url, params=params)
        return response.text

    def to_oracle(self):
        raw_json = json.loads(self.get_request_url())

        if len(raw_json['info']) > 0:
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')

            con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
            cur = con.cursor()
            query = 'merge into ROAD_EVENT ' \
                    'using DUAL on (id = :ocrr_id) ' \
                    'when matched then ' \
                    'update set last_updated_at = :current_time ' \
                    'when not matched then ' \
                    'insert (id, lat, lon, heading, link_id, code, created_at, last_updated_at) ' \
                    'values (:ocrr_id, :lat, :lon, :heading, :link_id, :code, :current_time, :current_time)'

            for info in raw_json['info']:
                ocrr_id = info.get("ocrr_id")
                lat = info.get("latitude")
                lon = info.get("longitude")
                heading = info.get("heading")
                link_id = info.get("link_id")
                code = info.get("code")

                cur.execute(query, (
                    ocrr_id, current_time, ocrr_id, lat, lon, heading, link_id, code, current_time, current_time))

            con.commit()
            cur.close()
            con.close()
