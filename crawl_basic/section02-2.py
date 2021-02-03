# 파이썬 크롤링 기초
# urlopen함수 기초 사용법

import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명
path_list = ["C:/Users/DY/Documents/Django_Study/crawl_basic/output/test1.jpg", "C:/Users/DY/Documents/Django_Study/crawl_basic/output/index.html"]

# 다운로드 리소스
target_url = ["https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAxMDlfMTky%2FMDAxNjEwMTk1OTYzMDg2.N4Xn6ik7cx63UpW0Ipuctxgov_06xgCiqBQxxBW51bIg._YZ2PVIUmMVasm0uEHHyEzPxue6wh4etyX5KLmKc-80g.JPEG.erasw0715%2FNate%25A3%25DF20210109%25A3%25DF205352.jpg&type=sc960_832",
"http://google.com"]

for i, url in enumerate(target_url):
    # 예외처리
    try:
        # 웹 수신 정보 읽기
        responce = req.urlopen(url)

        # 수신 내용
        contents = responce.read()

        print("---------------------------------------")

        # 상태 정보 중간 출력
        print('Header Info-{} : {}'.format(i, responce.info()))
        print('HTTP Status Code : {}'.format(responce.getcode()))
        print()
        print("---------------------------------------")


        with open(path_list[i], 'wb') as c:
            c.write(contents)
        
    except HTTPError as e:
        print("Download failed")
        print("HTTPError Code : ",e.code)
    except URLError as e:
        print("Download failed")
        print("URLError Code : ",e.code)
    # 성공
    else:
        print()
        print("Download Succed.")