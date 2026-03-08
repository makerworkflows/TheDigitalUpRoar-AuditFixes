import urllib.request

urls = {
    "tao.png": "https://logo.clearbit.com/taogroup.com",
    "50eggs.png": "https://logo.clearbit.com/50eggsinc.com",
    "driscoll.png": "https://logo.clearbit.com/driscollchildrens.org",
    "neuehouse.png": "https://logo.clearbit.com/neuehouse.com"
}

headers = {'User-Agent': 'Mozilla/5.0'}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            with open(name, 'wb') as f:
                f.write(response.read())
        print(f"Downloaded {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")
