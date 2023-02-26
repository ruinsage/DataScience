import requests
import json
import time
import cx_Oracle


class EvInfo:
    code = '860553'

    def get_request_url(self):
        url = 'http://api.jejuits.go.kr/api/infoEvList'
        params = {'code': self.code}
        response = requests.get(url, params=params)
        return response.text

    def to_oracle(self):
        raw_json = json.loads(self.get_request_url())

        if len(raw_json['info']) > 0:

            con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
            cur = con.cursor()
            query = 'update EV_CHARGING_STATION set fast = :fast, slow = :slow where id = :id'

            for info in raw_json['info']:
                id = info.get("id")
                fast = info.get("slow")
                slow = info.get("fast")

                cur.execute(query, (fast, slow, id))

            con.commit()
            cur.close()
            con.close()
