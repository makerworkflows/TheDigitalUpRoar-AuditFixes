import urllib.request
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

logos = {
    "tao.png": "https://upload.wikimedia.org/wikipedia/en/thumb/5/58/Tao_Group_Hospitality_logo.svg/512px-Tao_Group_Hospitality_logo.svg.png",
    "driscoll.png": "https://upload.wikimedia.org/wikipedia/en/thumb/f/fa/Driscoll_Children%27s_Hospital_logo.svg/512px-Driscoll_Children%27s_Hospital_logo.svg.png",
    "50eggs.png": "https://upload.wikimedia.org/wikipedia/commons/4/41/50_Eggs_Inc._Logo.png",
    "neuehouse.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/NeueHouse_Logo.svg/512px-NeueHouse_Logo.svg.png"
}

for filename, url in logos.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=context) as response, open(filename, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
