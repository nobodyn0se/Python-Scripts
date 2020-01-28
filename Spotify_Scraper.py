import re
import os
import ssl
import requests
from bs4 import BeautifulSoup


def scrape():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = "https://open.spotify.com/playlist/2a3sHKCJKiph2JNHVSuzca"
    hds = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

    html = requests.get(url, headers=hds)
    soup = BeautifulSoup(html.content, "html5lib")
    data = soup.find_all('span', attrs={'class': 'total-duration'})
    dlist = []
    for items in data:
        dlist.append(items.text)
    return dlist


def proc(dlist):
    r = re.compile("[0-9]+:[0-9]+")
    new = list(filter(r.match, dlist))
    sec = []
    mins = []
    for items in new:
        mins.append(int(items[0]))
        sec.append(int(items[2:]))

    min_sum = sum(mins)
    sec_sum = sum(sec)

    s = sec_sum % 60
    m = (min_sum + int(sec_sum/60))
    h = int(m / 60)
    m = m % 60

    print("Your Spotify playlist is {}hours {}minutes {}seconds long".format(h, m, s))
    totsongs = len(mins)
    avg = (h*3600 + m*60 + s)/totsongs

    s = round(avg % 60)
    m = int(avg/60)
    print("The average length of a song in your playlist is {}minutes {}seconds".format(m, s))


def main():
    d = scrape()
    proc(d)


if __name__ == "__main__":
    main()