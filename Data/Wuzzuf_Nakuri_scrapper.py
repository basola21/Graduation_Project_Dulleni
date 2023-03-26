import requests
import math
import pandas as pd
import re
import os
from bs4 import BeautifulSoup


url = "https://wuzzuf.net/api/search/job"

querystring = {"filter^\\[other^\\]^\\[slug^\\]":"=IT-Software-Development-Jobs-in-Egypt","page^\\[limit^\\]":"20","page^\\[offset^\\]":"1","filter[other][slug]":"=IT-Software-Development-Jobs-in-Egypt","page[limit]":"1","page[offset]":"0"}

payload = ""
headers = {
    "authority": "wuzzuf.net",
    "accept": "application/vnd.api+json",
    "accept-language": "en-GB,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-US;q=0.6,af;q=0.5",
    "cookie": "_ga=GA1.2.1887984789.1642518415; __gads=ID=034401b27adf0086:T=1642518462:S=ALNI_Mbc5dbCoCZrf2lJCxFXDmwtfDskDw; _fbp=fb.1.1659374298462.481822549; _hjSessionUser_2811765=eyJpZCI6IjM0YjgxNTBhLWRmOTMtNWQwNC1iNzQ4LTg0ZWJhNzdlYWU3MiIsImNyZWF0ZWQiOjE2NTkzNzQyOTg5NjIsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.2079773432.1660826896; __gpi=UID=00000a6d84ba692d:T=1659374300:RT=1660826897:S=ALNI_MbN-7afk2zPDGGExCTsngogEAHJYg; _hjSession_2811765=eyJpZCI6IjgxMjc3MjQ4LTUzYjQtNGZmNi1hYmQzLWI1ODM2Mjg2YmE2OSIsImNyZWF0ZWQiOjE2NjA4MjY4OTc3NDcsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; ci_sessions=ehtbcpsaf4ig80icegam4r1ahbb4g16p; LiToken=feedcca6bf220d9ae3c4150f1f246c621660832443; __insp_wid=1101373123; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93dXp6dWYubmV0L2pvYnMvZWd5cHQ^%^3D; __insp_targlpt=Sm9icyBpbiBFZ3lwdCAtIFdVWlpVRiB8INmI2LjZgS7Zg9mI2YU^%^3D; __insp_identity=Z3Vlc3QtNWQyNjc4MTctMDY4OC00NTg2LWI1YzYtZDM3Njk5NGMyYzY5; __insp_norec_sess=true; __insp_slim=1660832453954; mp_f65e85d232fcb7d93f8de265b9818087_mixpanel=^%^7B^%^22distinct_id^%^22^%^3A^%^20^%^22182b1545664596-03cd53d876e0b9-26021d51-1fa400-182b1545665a15^%^22^%^2C^%^22^%^24device_id^%^22^%^3A^%^20^%^22182b1545664596-03cd53d876e0b9-26021d51-1fa400-182b1545665a15^%^22^%^2C^%^22^%^24initial_referrer^%^22^%^3A^%^20^%^22https^%^3A^%^2F^%^2Fwuzzuf.net^%^2Fjobs^%^2Fegypt^%^22^%^2C^%^22^%^24initial_referring_domain^%^22^%^3A^%^20^%^22wuzzuf.net^%^22^%^7D; cto_bundle=eet-al8wN1pkWEVXanJ0VndDd1V2JTJCMUl5TmpTRXRSckhqNWVESDZDSGExRXFJUk9iJTJCRmRZN3dYODd4ejVxVUhJSVBUeVdGZllNMG5oYURFT1ZwOHJxSjVmbUJmbk5BJTJGZWw5eGMzM3olMkJzcVhQc2tUaWNQb1FhSGslMkZhUG5kOEJrR1JtNFNaZk9ndGg0Z3lKVCUyRkk4VElIc1dpaEElM0QlM0Q",
    "referer": "https://wuzzuf.net/a/IT-Software-Development-Jobs-in-Egypt?start=0",
    "sec-ch-ua": "^\^Chromium^^;v=^\^104^^, ^\^"
}

r = requests.request("GET", url, data=payload, headers=headers, params=querystring)
job_number = r.json()
job_number = job_number["meta"].get("totalResultsCount")

job_IDs = []
for i in range (math.ceil(job_number/1000)):
    url = "https://wuzzuf.net/api/search/job"

    querystring = {"filter^\\[other^\\]^\\[slug^\\]":"=IT-Software-Development-Jobs-in-Egypt","page^\\[limit^\\]":"20","page^\\[offset^\\]":"1","filter[other][slug]":"=IT-Software-Development-Jobs-in-Egypt","page[limit]":"1000","page[offset]":{i*1000}}

    payload = ""
    headers = {
        "authority": "wuzzuf.net",
        "accept": "application/vnd.api+json",
        "accept-language": "en-GB,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-US;q=0.6,af;q=0.5",
        "cookie": "_ga=GA1.2.1887984789.1642518415; __gads=ID=034401b27adf0086:T=1642518462:S=ALNI_Mbc5dbCoCZrf2lJCxFXDmwtfDskDw; _fbp=fb.1.1659374298462.481822549; _hjSessionUser_2811765=eyJpZCI6IjM0YjgxNTBhLWRmOTMtNWQwNC1iNzQ4LTg0ZWJhNzdlYWU3MiIsImNyZWF0ZWQiOjE2NTkzNzQyOTg5NjIsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.2079773432.1660826896; __gpi=UID=00000a6d84ba692d:T=1659374300:RT=1660826897:S=ALNI_MbN-7afk2zPDGGExCTsngogEAHJYg; _hjSession_2811765=eyJpZCI6IjgxMjc3MjQ4LTUzYjQtNGZmNi1hYmQzLWI1ODM2Mjg2YmE2OSIsImNyZWF0ZWQiOjE2NjA4MjY4OTc3NDcsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; ci_sessions=ehtbcpsaf4ig80icegam4r1ahbb4g16p; LiToken=feedcca6bf220d9ae3c4150f1f246c621660832443; __insp_wid=1101373123; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93dXp6dWYubmV0L2pvYnMvZWd5cHQ^%^3D; __insp_targlpt=Sm9icyBpbiBFZ3lwdCAtIFdVWlpVRiB8INmI2LjZgS7Zg9mI2YU^%^3D; __insp_identity=Z3Vlc3QtNWQyNjc4MTctMDY4OC00NTg2LWI1YzYtZDM3Njk5NGMyYzY5; __insp_norec_sess=true; __insp_slim=1660832453954; mp_f65e85d232fcb7d93f8de265b9818087_mixpanel=^%^7B^%^22distinct_id^%^22^%^3A^%^20^%^22182b1545664596-03cd53d876e0b9-26021d51-1fa400-182b1545665a15^%^22^%^2C^%^22^%^24device_id^%^22^%^3A^%^20^%^22182b1545664596-03cd53d876e0b9-26021d51-1fa400-182b1545665a15^%^22^%^2C^%^22^%^24initial_referrer^%^22^%^3A^%^20^%^22https^%^3A^%^2F^%^2Fwuzzuf.net^%^2Fjobs^%^2Fegypt^%^22^%^2C^%^22^%^24initial_referring_domain^%^22^%^3A^%^20^%^22wuzzuf.net^%^22^%^7D; cto_bundle=eet-al8wN1pkWEVXanJ0VndDd1V2JTJCMUl5TmpTRXRSckhqNWVESDZDSGExRXFJUk9iJTJCRmRZN3dYODd4ejVxVUhJSVBUeVdGZllNMG5oYURFT1ZwOHJxSjVmbUJmbk5BJTJGZWw5eGMzM3olMkJzcVhQc2tUaWNQb1FhSGslMkZhUG5kOEJrR1JtNFNaZk9ndGg0Z3lKVCUyRkk4VElIc1dpaEElM0QlM0Q",
        "referer": "https://wuzzuf.net/a/IT-Software-Development-Jobs-in-Egypt?start=0",
        "sec-ch-ua": "^\^Chromium^^;v=^\^104^^, ^\^"
    }

    r = requests.request("GET", url, data=payload, headers=headers, params=querystring)


    data = r.json()

    for j in data['data']:
        job_IDs.append(j["id"])

    job_IDs_string = ",".join(job_IDs)

    
res = []

for i in range(0,len(job_IDs),100):
    job_IDs_string = ",".join(job_IDs[i:i+100])

    url = "https://wuzzuf.net/api/job?filter[other][ids]="+ job_IDs_string

    querystring = {"filter^\\[other^\\]^\\[ids^\\]": job_IDs_string}

    '''payload = ""
    headers = {
        "authority": "wuzzuf.net",
        "accept": "application/vnd.api+json",
        "accept-language": "en-GB,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-US;q=0.6,af;q=0.5",
        "cookie": "_ga=GA1.2.1887984789.1642518415; __gads=ID=034401b27adf0086:T=1642518462:S=ALNI_Mbc5dbCoCZrf2lJCxFXDmwtfDskDw; _fbp=fb.1.1659374298462.481822549; _hjSessionUser_2811765=eyJpZCI6IjM0YjgxNTBhLWRmOTMtNWQwNC1iNzQ4LTg0ZWJhNzdlYWU3MiIsImNyZWF0ZWQiOjE2NTkzNzQyOTg5NjIsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.2079773432.1660826896; __gpi=UID=00000a6d84ba692d:T=1659374300:RT=1660826897:S=ALNI_MbN-7afk2zPDGGExCTsngogEAHJYg; _hjIncludedInSessionSample=0; _hjSession_2811765=eyJpZCI6IjgxMjc3MjQ4LTUzYjQtNGZmNi1hYmQzLWI1ODM2Mjg2YmE2OSIsImNyZWF0ZWQiOjE2NjA4MjY4OTc3NDcsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; ci_sessions=ehtbcpsaf4ig80icegam4r1ahbb4g16p; LiToken=b6bed86c553420d9b7c4aec65e0f43641660826906; __insp_wid=1101373123; __insp_slim=1660826910166; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93dXp6dWYubmV0L2pvYnMvZWd5cHQ^%^3D; __insp_targlpt=Sm9icyBpbiBFZ3lwdCAtIFdVWlpVRiB8INmI2LjZgS7Zg9mI2YU^%^3D; __insp_identity=Z3Vlc3QtNWQyNjc4MTctMDY4OC00NTg2LWI1YzYtZDM3Njk5NGMyYzY5; __insp_norec_sess=true; _gat=1; mp_f65e85d232fcb7d93f8de265b9818087_mixpanel=^%^7B^%^22distinct_id^%^22^%^3A^%^20^%^22182b0ffa2df1ba-0cdd4929f13d8e-26021d51-1fa400-182b0ffa2e0153^%^22^%^2C^%^22^%^24device_id^%^22^%^3A^%^20^%^22182b0ffa2df1ba-0cdd4929f13d8e-26021d51-1fa400-182b0ffa2e0153^%^22^%^2C^%^22^%^24initial_referrer^%^22^%^3A^%^20^%^22https^%^3A^%^2F^%^2Fwuzzuf.net^%^2Fjobs^%^2Fegypt^%^22^%^2C^%^22^%^24initial_referring_domain^%^22^%^3A^%^20^%^22wuzzuf.net^%^22^%^7D; cto_bundle=cBvTYF8wN1pkWEVXanJ0VndDd1V2JTJCMUl5Tmx6YlFWbWpxbUdBbEJaM0ZiU2dZNVU1Qm5RVVVBeHp2TlB4YWJmNVpxTFhOQUZZTVhLWWhpUU53Ym1WJTJCSjM4VGdoJTJCMjhSUWlOOHJ3OSUyQkQyZWZJUnl6VkNJb0xpNEdXaWNHMVBIN09waEp1VEw2dE5ZVVlvNG1sd1lkTm5leWJ1ZyUzRCUzRA",
        "referer": "https://wuzzuf.net/a/IT-Software-Development-Jobs-in-Egypt?ref=browse-jobs&start=20",
        "sec-ch-ua": "^\^Chromium^^;v=^\^104^^, ^\^"
    }'''

    r = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    data = r.json()
    for j in data["data"]:
        res.append(j)

df = pd.json_normalize(res)
df.columns = df.columns.str.replace('attributes', '')
df.columns = df.columns.str.replace('.', ' ')
df.columns = df.columns.str.strip()

def useRegex(input):
    pattern = re.compile(r"'[^']*'", re.IGNORECASE)
    return re.search(pattern,input).group()

for i in range(len(df)):
    keywords_string = df["keywords"][i]
    keywords_array = []
    for x in keywords_string:
        keywords_array.append(useRegex(str(x.values())))

    new_keywords_string = ','.join(keywords_array)
    df["keywords"][i] = new_keywords_string


for i in range(len(df)):
    html = df['description'][i]
    soup = BeautifulSoup(html)
    df['description'][i] = soup.get_text()


# if file does not exist write header 
if not os.path.isfile('wuzzuf_IT_jobs 15-03-2022.csv'):
   df.to_csv('wuzzuf_IT_jobs 15-03-2022.csv', header='column_names')
else: # else it exists so append without writing the header
   df.to_csv('wuzzuf_IT_jobs 15-03-2022.csv', mode='a', header=False)


#Nakuri Scrapper

url = "https://www.naukrigulf.com/spapi/jobapi/search"



querystring = {"ClusterInd":"25,24","Experience":"","Keywords":"it","KeywordsAr":"","Limit":"50","Location":"egypt","LocationAr":"","Offset":"","SortPreference":"relevance","breadcrumb":"1","clusterSelected":"1","geoIpCityName":"","geoIpCountryName":"Egypt","isPagination":"false","locationId":"3","nationality":"","nationalityLabel":"","pageNo":"1","requestsource":"mr","seo":"1","showBellyFilters":"true","srchId":"16630818931663081893365_3","ts":"1663023779000","xz":"1_2_5"}

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

data = response.json()

jobs_data = []
for i in range(int(data['totalJobsCount']/50)):
    querystring = {"ClusterInd":"25,24","Experience":"","Keywords":"it","KeywordsAr":"","Limit":"50","Location":"egypt","LocationAr":"","Offset":"","SortPreference":"relevance","breadcrumb":"1","clusterSelected":"1","geoIpCityName":"","geoIpCountryName":"Egypt","isPagination":"false","locationId":"3","nationality":"","nationalityLabel":"","pageNo":"{i}","requestsource":"mr","seo":"1","showBellyFilters":"true","srchId":"16630818931663081893365_3","ts":"1663023779000","xz":"1_2_5"}

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
    
    new_data = response.json()

    for job in new_data['jobs']:
        jobs_data.append(job)
        
jobs_data = pd.DataFrame(jobs_data)

for i in range(len(jobs_data)):
    html = jobs_data['description'][i]
    soup = BeautifulSoup(html)
    jobs_data['description'][i] = soup.get_text()

# if file does not exist write header 
if not os.path.isfile('Nakuri Egypt IT Jobs 15-03-2022.csv'):
   jobs_data.to_csv('Nakuri Egypt IT Jobs 15-03-2022.csv', header='column_names')
else: # else it exists so append without writing the header
   jobs_data.to_csv('Nakuri Egypt IT Jobs 15-03-2022.csv', mode='a', header=False)