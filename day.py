def ymd(_y,_m,_d):
    f=int((14-_m)/12)
    y=_y-f
    m=_m+12*f-2
    date=str((_d+y+int(31*m/12)+int(y/4)-int(y/100)+int(y/400))%7)
    hz=str.maketrans('0123456','天一二三四五六')
    date=date.translate(hz)
    return date
y=int(input("年："))
m=int(input("月："))
d=int(input("日："))

print("这天是星期%s" % ymd(y,m,d,))
