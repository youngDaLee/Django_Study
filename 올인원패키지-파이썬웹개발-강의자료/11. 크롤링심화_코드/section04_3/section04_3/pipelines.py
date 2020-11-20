# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 파이프라인 실습(1)
# 예) 잘못된 데이터 제거, DB 저장, SNS 전송, SMS 전송, 메일 전송 등

# 엑셀 처리 임포트
import xlsxwriter
import csv
from scrapy.exceptions import DropItem


class TestSpiderPipeline(object):

    # 초기화 메소드
    def __init__(self):
        # 엑셀 처리 선언
        self.workbook = xlsxwriter.Workbook("C:/result_excel.xlsx")
        # CSV 처리 선언(a, w 옵션 변경)
        self.file_opener = open('C:/result_csv.csv', 'w')
        self.csv_writer = csv.DictWriter(self.file_opener, fieldnames=['rank_num', 'site_name', 'daily_time_site', 'daily_page_view', 'is_pass'])
        # 워크 시트
        self.worksheet = self.workbook.add_worksheet()
        # 삽입 수
        self.rowcount = 1

    # 최초 1회 실행
    def open_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Stated.')

    # 아이템 추출 시 항상 실행
    # 40위 초과는 Drop 테스트
    def process_item(self, item, spider):
        if int(item.get('rank_num')) < 41:
            item['is_pass'] = True
            # 엑셀 저장
            self.worksheet.write('A%s' % self.rowcount, item.get('rank_num'))
            self.worksheet.write('B%s' % self.rowcount, item.get('site_name'))
            self.worksheet.write('C%s' % self.rowcount, item.get('daily_time_site'))
            self.worksheet.write('D%s' % self.rowcount, item.get('daily_page_view'))
            self.worksheet.write('D%s' % self.rowcount, item.get('is_pass'))
            self.rowcount += 1

            # CSV 저장
            self.csv_writer.writerow(item)

            return item
        else:
            raise DropItem(f'Dropped Item. Because This Site Rank is {item.get("rank_num")}')

    # 마지막 1회 실행
    def close_spider(self, spider):
        # 엑셀 파일 닫기
        self.workbook.close()
        # CSV 파일 닫기
        self.file_opener.close()
        spider.logger.info('TestSpider Pipeline Stopped.')
