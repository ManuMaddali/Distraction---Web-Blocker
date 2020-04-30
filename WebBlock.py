import time
from datetime import datetime as dt

hosts_temp = "hosts"
host_path = "/etc/hosts"
redirect = "127.0.0.1"
# Below is where you can add websites to block and change the timings for the block.
website_blocks = ["www.facebook.com","facebook.com" "www.youtube.com", "reddit.com", "www.reddit.com", "www.twitter.com", "twitter.com", "www.stockx.com", "stockx.com", "amazon.com", "www.amazon.com", "tiktok.com", "www.tiktok.com", "zappos.com", "www.youtube.com", "lookmovie.com", "www.lookmovie.com", "ebay.com", "www.ebay.com", "youtube.com"]
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Working Hours... ")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_blocks:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_blocks):
                    file.write(line)
        print("Fun Hours...! ")
    time.sleep(5)
