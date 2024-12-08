# https://www.google.com/search?q=weather+patna
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36
# span id=wob_tm class="wob_t q8U8x"
from requests_html import HTMLSession
import speechtotext
def weather():
    s= HTMLSession()
    query="patna"
    url = f'https://www.google.com/search?q=weather+{query}'

    r= s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'})

    temp=r.html.find('span#wob_tm.wob_t.q8U8x', first=True).text
    # print(temp)
    unit=r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    # print(unit)
    desc=r.html.find('span#wob_dc', first=True).text
    # print(desc)

    return temp+" " + unit+" "+ desc