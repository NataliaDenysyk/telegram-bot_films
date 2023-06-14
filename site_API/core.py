import requests
from site_API.utils.site_api_handler import SiteApiInterface
from settings import SiteSettings

site = SiteSettings()


headers = {
	"X-RapidAPI-Key": site.api_key.get_secret_value(),
	"X-RapidAPI-Host": site.host_api
}

url = "https://ott-details.p.rapidapi.com/advancedsearch"

params = {"min_imdb":"6","max_imdb":"10","sort":"latest",
		  "page":"1","language":"russian","type":"movie"}

site_api = SiteApiInterface


if __name__ == '__main__':
	site_api()