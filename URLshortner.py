import pyshorteners

url = input('Enter the URL: ')


def shortenurl(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    print("YOUR SHORT URL IS :",shortened_url)


shortenurl(url)