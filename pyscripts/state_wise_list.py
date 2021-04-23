import json
from urllib.request import urlopen
url = "https://api.covid19india.org/v4/min/data.min.json"
response = urlopen(url)
data_json = json.loads(response.read())
print(" State             Active cases")
print("-----------------------------------")
for x in data_json.keys():
    confirmed = 0
    deceased = 0
    recovered = 0
    if "confirmed" in data_json[x]["delta7"]:
        confirmed = data_json[x]["delta7"]["confirmed"]

    if "deceased" in data_json[x]["delta7"]:
        deceased = data_json[x]["delta7"]["deceased"]

    if "recovered" in data_json[x]["delta7"]:
        recovered = data_json[x]["delta7"]["recovered"]

    print("{}                   {}".format(x, (confirmed-deceased-recovered)))
