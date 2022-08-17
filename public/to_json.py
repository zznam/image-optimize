import json
import csv

FILE_NAME = ['homepage', 'gamepage', 'portfolio', 'metaverse']

for filename in FILE_NAME:
    with open(f'./{filename}.csv', 'r') as fr:
        spamreader = csv.reader(fr, delimiter=',', quotechar='"')
        print("filename: ", filename)
        allrows = list(spamreader)
        languages = allrows[0][1:]
        for idx, language in enumerate(languages):
            mapping = {}
            for row in allrows[1:]:
                mapping[row[0]] = row[idx + 1]
            try:
                orginal_data = json.load(open(f'locales/{language}/{filename}.json'))
                orginal_data.update(mapping)
                with open(f'./locales/{language}/{filename}.json', 'w') as fw:
                    json.dump(orginal_data, fw, ensure_ascii=False, indent=2)
            except:
                pass
