import json

myjsonfile = open('doc.json', 'r')
jsondata = myjsonfile.read()

obj = json.loads(jsondata)
table = dict()
fixtures = obj['fixtures']
for ls in fixtures:
    scores = ls['ft']
    goaldiff = scores[0] - scores[1]
    if scores[0] > scores[1]:
        # print(ls['team1']+' wins')
        table['team'] = ls['team1']
        table['points'] = 3
        table['gf'] = goaldiff
        table['game'] = ls['gameno']
        print(table)
        table['team'] = ls['team2']
        table['points'] = 0
        table['gf'] = -goaldiff
        table['game'] = ls['gameno']
        print(table)
    elif scores[0] < scores[1]:
        # print(ls['team2']+' wins')
        table['team'] = ls['team2']
        table['points'] = 3
        table['gf'] = goaldiff
        table['game'] = ls['gameno']
        print(table)
        table['team'] = ls['team1']
        table['points'] = 0
        table['gf'] = -goaldiff
        table['game'] = ls['gameno']
        print(table)

    else:
        # print('Draw')     
        table['team'] = ls['team1']
        table['points'] = 1
        table['gf'] = goaldiff
        table['game'] = ls['gameno']
        print(table)
        table['team'] = ls['team2']
        table['points'] = 1
        table['gf'] = goaldiff
        table['game'] = ls['gameno']
        print(table)



# print(table)