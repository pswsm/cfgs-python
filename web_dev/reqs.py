import requests
from requests.models import Response
import pprint as pp

if __name__ == "__main__":
    url: str = "https://animechan.vercel.app/api/random"

    pp.pp(requests.get(url).json())
