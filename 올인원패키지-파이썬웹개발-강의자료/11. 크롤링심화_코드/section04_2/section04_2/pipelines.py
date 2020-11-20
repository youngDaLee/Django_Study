# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 파이프라인 실습(1)
# 예) 잘못된 데이터 제거, DB 저장, SNS 전송, SMS 전송, 메일 전송 등

from scrapy.exceptions import DropItem


class TestSpiderPipeline(object):
    # 최초 1회 실행
    def open_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Stated.')

    # 아이템 추출 시 항상 실행
    # 40위 초과는 Drop 테스트
    def process_item(self, item, spider):
        if int(item.get('rank_num')) < 41:
            item['is_pass'] = True
            return item
        else:
            raise DropItem(f'Dropped Item. Because This Site Rank is {item.get("rank_num")}')

    # 마지막 1회 실행
    def close_spider(selfs, spider):
        spider.logger.info('TestSpider Pipeline Stopped.')
