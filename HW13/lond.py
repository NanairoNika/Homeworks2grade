def WintSummTime(UTC, consttime):
    counter = 0
    for time in UTC:
        for swtime in consttime:
            if time == swtime:
                counter += 1
        if counter == 0:
            consttime.append(time)
        counter = 0
    return consttime


def main():
    import re
    f = open ('lond.html' , 'r', encoding = 'utf-8')
    text = f.read()
    UTC = re.findall('UTC\+?[1234567890]+', text)
    consttime = [UTC[0]]
    consttime = WintSummTime(UTC, consttime)
    print ('Зимнее время >', consttime[0])
    if len(consttime) == 2:
        print ('Летнее время >', consttime[1])


main()
