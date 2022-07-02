import pandas as pd

g = open(f'query.txt', 'w', encoding='utf-8')

for z in range(17, 24):
    day = str(z)

    df = pd.read_csv(f'202206{day}.csv').drop('Unnamed: 0', axis=1)
    df = df.fillna('')

    form = '{{'
    for col in df.columns:
        form += f'"{col}":{{}},'
    form += '"date": {}}}\n'
    date = f'"2022-06-{day}"'

    for i in range(len(df)):
        res = []
        for col in df.columns:
            txt = df.loc[i, col]
            if type(txt) == str:
                res.append(f'"{txt}"')
            else:
                res.append(txt)
        
        res.append(date)
        g.write(f'{{"index": {{"_index": "demo_yuha9", "_id": "202206{day}_{i + 1}"}}}}\n')
        g.write(form.format(*res))