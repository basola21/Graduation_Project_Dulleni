import requests
import math
import pandas as pd
import re
import os

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


# if file does not exist write header 
if not os.path.isfile('wuzzuf_IT_jobs 08-11-2022.csv'):
   df.to_csv('wuzzuf_IT_jobs 17-12-2022.csv', header='column_names')
else: # else it exists so append without writing the header
   df.to_csv('wuzzuf_IT_jobs 17-12-2022.csv', mode='a', header=False)