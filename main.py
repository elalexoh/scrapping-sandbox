import re
from colorama import Fore
import requests

website = 'https://www.vulnhub.com/?page=2'
results = requests.get(website)
content = results.text #To Text


pattern = r"/entry/[\w-]*" #Expresion regular
duplicate_machines = re.findall(pattern, str(content))
non_duplicate_machines = list(set(duplicate_machines)) #Remove Duplicates

final_machines = []

for machine in non_duplicate_machines:
  machine_name = machine.replace('/entry/', '')
  final_machines.append(machine_name)
  print(machine_name)
print('\n')

###############################################
new_machine = "noob-1"
have_new_machine = False

for machine in final_machines:
  if machine == new_machine:
    have_new_machine = True
    break

success_color = Fore.GREEN
warning_color = Fore.YELLOW

if have_new_machine == True:
  print(success_color + '---No New Machine---')
else:
  print(warning_color + '---New machine---')