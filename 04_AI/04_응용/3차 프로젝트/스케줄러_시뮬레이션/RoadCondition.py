import requests
import json
import time
import cx_Oracle


class RoadCondition:
    code = '860553'
    def get_request_url(self):
        url = 'http://api.jejuits.go.kr/api/infoRwisList'
        params = {'code': self.code}
        response = requests.get(url, params=params)
        return response.text
    def to_oracle(self) :
        raw_json = json.loads(self.get_request_url())

        if len(raw_json['info']) > 0 :
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')

            con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
            cur = con.cursor()
            query = 'insert into ROAD_CONDITION values (ROAD_CONDITION_SEQ.NEXTVAL, :lat, :lon, :heading, :link_id, :visibility, :snow, :road_temp, :water_film, :friction, :code, :current_time)'

            for info in raw_json['info'] :
                lat = info.get("latitude")
                lon = info.get("longitude")
                heading = info.get("heading")
                link_id = info.get("link_id")
                visibility = info.get("visibility")
                snow = info.get("snow")
                road_temp = info.get("road_temp")
                water_film = info.get("water_film")
                friction = info.get("friction")
                code = info.get("code")

                cur.execute(query, (lat, lon, heading, link_id, visibility, snow, road_temp, water_film, friction, code, current_time))

            con.commit()
            cur.close()
            con.close()