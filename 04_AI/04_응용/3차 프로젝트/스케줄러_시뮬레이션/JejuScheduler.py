from RoadWork import RoadWork
from RoadEvent import RoadEvent
from RoadCondition import RoadCondition
from RoadClose import RoadClose
from GasPriceInfo import GasPriceInfo
from EvInfo import EvInfo
import time

class JejuScheduler :

    def __init__(self):
        self.roadWork = RoadWork()
        self.roadEvent = RoadEvent()
        self.roadCondition = RoadCondition()
        self.roadClose = RoadClose()
        self.gasPriceInfo = GasPriceInfo()
        self.evInfo = EvInfo()

    def scheduler(self):

        print('데이터 수집기 스케줄러 동작.\n')

        while True:
            self.roadWork.to_oracle()
            print("도로 공사 수집 완료")
            self.roadEvent.to_oracle()
            print("도로 돌발 상황 수집 완료")
            self.roadCondition.to_oracle()
            print("도로 기상 수집 완료")
            self.roadClose.to_oracle()
            print("도로 통제 수집 완료")
            self.gasPriceInfo.to_oracle()
            print("주유소 정보 수집 완료")
            self.evInfo.to_oracle()
            print("충전소 정보 수집 완료")

            print(time.strftime('%Y-%m-%d %H:%M:%S'))

            time.sleep(300)



JejuScheduler().scheduler()