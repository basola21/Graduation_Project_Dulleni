import requests
import pandas as pd

url = "https://www.naukrigulf.com/spapi/jobapi/search"

querystring = {"ClusterInd":"25,24","Experience":"","Keywords":"it","KeywordsAr":"","Limit":"30","Location":"egypt","LocationAr":"","Offset":"30","SortPreference":"relevance","breadcrumb":"1","clusterSelected":"1","geoIpCityName":"Al Mansurah","geoIpCountryName":"Egypt","isPagination":"true","locationId":"3","nationality":"","nationalityLabel":"","pageNo":"2","requestsource":"mr","seo":"1","showBellyFilters":"true","srchId":"16630818931663081893365_3","ts":"1663023779000","xz":"1_2_5"}

payload = ""
headers = {
    "cookie": "aka_location=Country=EG; mboost=false; profileCom=y; chatbotonorganicresman=n; chatbotonmarketingresman=y; _t_ds=c27c2121662286175-170c27c212-0c27c212; _gcl_au=1.1.1815766133.1662286415; _ga=GA1.2.947665346.1662286177; _fbp=fb.1.1662286418582.1228185632; G_ENABLED_IDPS=google; __atuvc=2%7C36; g_state={'ip':1663628567345,'i_l':3}; _ngUP=4de3977ad5a6450e6e18c1c91adacd3541e9b1d8c050588aa621c59de30ccab3; countryc=EG; countryn=Egypt; city=Cairo; state=Cairo Governorate; bm_mi=A1422DF432AE71DB1CB4DE3B62241446~YAAQhuzAF3CVzgODAQAAimFmNxFuO+A42B3e6KjylyKybGtfOyIjcZaX9YUarv8Moc2VfrrwpA8NJSIsfwglRLTrB0wbMQmIMBDq8xbeMd0h92aAFMuO0X30Ri8448udw/ijGnQdfzNZNdoUBe4pLxblbYlN26LeEYYByK/v62hhvc2nOHiFwMLIlzCaWtXrj1V0TJzOWlS2XWKlCAIrUf5WQJh49bv/068m9D29AsEFWO6tosSLGDHYcY8PtO230BegIV4PlLhThAN0gLt0FBIlWEeSE3iKjoJHwQ68Xbdqxc0Q7Q28S17D3xUxL/uPBA==~1; _ngenv1[lang]=en; puppeteer=n; resmanexp=; __utma=127812882.947665346.1662286177.1663023744.1663081801.9; __utmc=127812882; __utmz=127812882.1663081801.9.6.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; ak_bmsc=B378132324A1C1A50283B3E476F211C3~000000000000000000000000000000~YAAQhuzAF92VzgODAQAAK2dmNxHhc1t7y611qFU+4Joxkn8B7IPc7vpf3+5GhlCD59fnFQCbIeVyhWQ7eO+DtS1xYpGpY7NNTk4+KMdnLhypFHOdi6ze9WoeFVRTt6XD0jtWv4awLVATtfbTuYpeiQO6X/0BZ2R6Yxsn43nIAW8exPgqZkJjeTyCM4r2gHH0oO/uqDhbwKqCPjmLyGD2Z8SKDLCcuFxHvYAC8J+MVdSvFQjoLTWb/ZUVo59bOcLZoD3eV5HI5RWqKDvcwg6IfVcM17TUkZD5ZrfvZ9nQNIANKtW9cmuTPJH5ICp7mURMuK3hHujamuqDmjYBWthlh8e2LtRXKqMhC0ft8o8UbZZyDDJ/m+rXAt8KtGwib6+1jS0zjIE6K8yOXlExrr0CgufsOBd+s7Vo9Sh6T/HO+BoMlFP4p+wjyNUaJd8PUSiePSmzOHIGMhzlpwE4yEtB85bksyOHwf29BPjBwaMSivnpyOz406nLboLIPg/Hpj8vXvxSGtE=; pwa_lang=en; PHPSESSID=fcd5cf7a17920c57468c0caf925c211f; __ccode=EG; aka_location=Country=EG; __utmb=127812882.22.8.1663081948420; bm_sv=78B3D4AB4BA18026E85B0967F47155E1~YAAQhuzAFyfLzgODAQAARdNoNxFcSNdsVpJQHcVgh7UBpiTpZcvyvl6GygCoWksNPJ7KXEUn2GcN3xDhmFYyL8SluKMBdEeOEc+xQ7ow4XqyIWUCeV9TkMu9HZ+YM7NkQI/iDVQRbdjcvBum3aqc++xw+AyIgPV11ibk+/I4EjqEDmtk1G6adLE0V+gmZJ8cLhQaQ2a/VHMnuUXzR5lkEt5rrHe3uuTnAW0zJtwbhUzVv9c+6XLLV2o87kl4nPVLnDwwU58=~1; HOWTORT=ul=1663081890513&r=https%3A%2F%2Fwww.naukrigulf.com%2Fit-jobs-in-egypt%3FindustryType%3D25%2C24%26recentSearch%3Dfalse%26requestsource%3Dmr%26ts%3D1663023779000%26xz%3D1_2_5&hd=1663081890849&cl=1663081996028&nu=https%3A%2F%2Fwww.naukrigulf.com%2Fit-jobs-in-egypt-2%3FindustryType%3D25%2C24%26recentSearch%3Dfalse%26requestsource%3Dmr%26ts%3D1663023779000%26xz%3D1_2_5",
    "authority": "www.naukrigulf.com",
    "accept": "application/json",
    "accept-format": "strict",
    "accept-language": "ENGLISH",
    "appid": "205",
    "cache-control": "no-cache",
    "client-type": "desktop",
    "clientid": "desktop",
    "device-type": "desktop",
    "locationid": "3",
    "nationality": "",
    "puppeteer": "false",
    "referer": "https://www.naukrigulf.com/it-jobs-in-egypt-2?industryType=25,24&recentSearch=false&requestsource=mr&ts=1663023779000&xz=1_2_5",
    "sec-ch-ua": "'Google Chrome';v='105', 'Not')A;Brand;v='8', 'Chromium';v='105'",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "systemid": "1112",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "userdata": "|US"}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

df = pd.json_normalize(response)
df.head()

