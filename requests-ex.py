import requests

r = requests.get("https://imgs.xkcd.com/comics/science_fair.png")

print(r.status_code)

#with open("comic.png", "wb") as image:
#   image.write(r.content)

