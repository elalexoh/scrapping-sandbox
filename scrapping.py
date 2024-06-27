import re
from colorama import Fore
import requests

website = 'https://www.vulnhub.com/'
results = requests.get(website)
content = results.text #To Text
