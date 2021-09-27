import scraper_helper as sh

BOT_NAME = 'solarfinal'

SPIDER_MODULES = ['solarfinal.spiders']
NEWSPIDER_MODULE = 'solarfinal.spiders'
ROBOTSTXT_OBEY = False
AUTOTHROTTLE_ENABLED= True
DEFAULT_REQUEST_HEADERS = sh.get_dict(
'''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: keep-alive
Cookie: PHPSESSID=cdu4agkv0o2d4jb4vp35b0qgno; __gads=ID=db18d7887f2f3f08:T=1632419795:S=ALNI_MbSyR-CrS2SLEs1WRKuF6293Ap-lA; _gcl_au=1.1.1984873870.1632419800; _ga=GA1.2.1800005635.1632419795; homepage_fv_mark=1; currency=67; site_visits_times=11; _gid=GA1.2.1115521386.1632680599; _uetsid=d2b5ca001ef611ecbe51430617eacef1; _uetvid=9a5056301c9711ec8740995047ca4d0f; _gat_UA-15983029-2=1
Host: www.enfsolar.com
sec-ch-ua: "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36
'''
)

