def instag(link):
    import requests

    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "e862f6eac5msh6227fdf6678b8dcp1b7cf7jsnef217d785d61",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    import json
    rest=json.loads(response.text)
    print("INSTAGR = ",rest)
    return rest
    

def tiktok(link):
    import requests

    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url": link}

    headers = {
            "X-RapidAPI-Key": "e862f6eac5msh6227fdf6678b8dcp1b7cf7jsnef217d785d61",
            "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    import json
    rest = json.loads(response.text)
    print("TIKTOK = ", rest)
    return rest

# tiktok('https://www.instagram.com/p/CWarspYsb6-/')
# print("###############################################################################################################################")
# print("###############################################################################################################################")
# tiktok('https://vt.tiktok.com/ZSdvP6P9N/?k=1')

