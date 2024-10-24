import json

with open("C:/Users/turs/Desktop/dzz/pp/lab4/json/data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("DN                                                 Description          Speed    MTU")
print("-" * 50, "-" * 20, "-" * 7, "-" * 7)

for x in data["imdata"]:
    inter = x['l1PhysIf']['attributes']
    abc = inter['dn']
    if (len(abc) == 42):
        print(f"{inter['dn']}            {inter['descr']}                  {inter['speed']}  {inter['mtu']}")
    else:
        print(f"{inter['dn']}             {inter['descr']}                  {inter['speed']}  {inter['mtu']}")