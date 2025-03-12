def quater(title, date):
    if date[1] in ('01', '02', '03'):
        return date[0] + ' 1Q ' + title
    elif date[1] in ('04', '05', '06'):
        return date[0] + ' 2Q ' + title
    elif date[1] in ('07', '08', '09'):
        return date[0] + ' 3Q ' + title
    else:
        return date[0] + ' 4Q ' + title


def change_title(title, dates):
    dates = list(dates)
    final = ['' for _ in range(len(dates))]

    for i in range(len(dates)):
        if final[i] == '':
            cnt = []
            cnt.append(i)
        for j in range(i + 1, len(dates)):
            if dates[cnt[0]][0] == dates[j][0]:
                cnt.append(j)
        if len(cnt) == 1:
            final[i] = dates[i][0] + ' ' + title
        elif len(cnt) == 2 and ((int(dates[cnt[0]][1]) <= 6 and int(dates[cnt[1]][1]) >= 7) or (
                int(dates[cnt[0]][1]) >= 7 and int(dates[cnt[1]][1]) <= 6)):
            if (int(dates[cnt[0]][1]) <= 6 and int(dates[cnt[1]][1]) >= 7):
                final[cnt[0]] = dates[cnt[0]][0] + ' 1H ' + title
                final[cnt[1]] = dates[cnt[1]][0] + ' 2H ' + title
            else:
                final[cnt[0]] = dates[cnt[0]][0] + ' 2H ' + title
                final[cnt[1]] = dates[cnt[1]][0] + ' 1H ' + title
            continue
        else:
            for c in cnt:
                final[c] = quater(title, dates[c])
            # print('final=', final)
        return final


def solution(title, dates):
    ## 문서 이름대로 분류
    d = dict()
    for i in range(len(title)):
        if title[i] not in d:
            d[title[i]] = []
            date = dates[i].split("-")
            d[title[i]].append(date)

    # visited = set()
    # ## 각 문서마다 이름 변경해주기
    for t in d.keys():
        # print('변경 전 dates=', d[t])
        d[t] = change_title(t, d[t])
        # print('변경 후 dates=', d[t])
        # print()

    answer = []
    for t in title:
        final_title = d[t].pop(0)
        answer.append(final_title)
    return answer
