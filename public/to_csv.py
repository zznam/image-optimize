import json
import csv

FILE_NAME = ['homepage', 'portfolio', 'gamepage', 'metaverse']
LANGUAGES = ['en', 'vi', 'zh', 'ko', 'es']

for filename in FILE_NAME:
    with open(f'locales/en/{filename}.json') as fr:
        data = json.load(fr)
        trans = {}
        for language in LANGUAGES:
            f = open(f'locales/{language}/{filename}.json')
            trans[language] = json.load(f)
            f.close()

        with open(f'./{filename}.csv', 'w') as fw:
            spamwriter = csv.writer(fw, delimiter='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['key', 'en', 'vi', 'zh', 'kor', 'es', 'ja'])
            for key, value in data.items():
                row = [key] + [trans[l].get(key, '') for l in LANGUAGES]
                spamwriter.writerow(row)
