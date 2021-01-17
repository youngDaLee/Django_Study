# 파이썬 크롤링 기초.
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req

# 파일 URL
img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDEyMjJfMjM1%2FMDAxNjA4NjEzNTUzODM3.8k1TwdtgJirKfh5CAfI5vPiHHZWpcTKkw5h9NeoZunwg.qh2QE8o4Vc1zBKrC0_OSIufON1UWpZpKqOUJvbIVOYQg.JPEG.wwqwe12%2Fqhfl.jpg&type=sc960_832'
html_url = 'http://google.com'

# 다운받을 경로
save_path1 = 'C:/test1.jpg'
save_path2 = 'C:/index.html'


# 예외 처리
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download faild')
    print(e)
else:
    print(header1)
    print(header2)