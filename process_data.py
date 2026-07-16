import glob

import yaml

data = []
for path in glob.glob("./input/*.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        data.extend(yaml.safe_load(f))

for t in data:
    print(t["title"])

with open("output/already_appeared.txt", "w", encoding="utf-8") as out:
    out.writelines(f"{item['title']}\n" for item in data)
