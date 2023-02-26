import requests
import json
import time
import cx_Oracle


class GasPriceInfo:
    code = '860529'

    def get_request_url(self):
        url = 'http://api.jejuits.go.kr/api/infoGasPriceList'
        params = {'code': self.code}
        response = requests.get(url, params=params)
        return response.text

    def to_oracle(self):
        raw_json = json.loads(self.get_request_url())

        if len(raw_json['info']) > 0:

            con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
            cur = con.cursor()
            query = 'update GAS_STATION set gasoline = :gasoline, diesel = :diesel, lpg = :lpg where id = :id'

            for info in raw_json['info']:
                id = info.get("id")
                gasoline = info.get("gasoline")
                diesel = info.get("diesel")
                lpg = info.get("lpg")

                cur.execute(query, (gasoline, diesel, lpg, id))

            con.commit()
            cur.close()
            con.close()
