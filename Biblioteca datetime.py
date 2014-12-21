from datetime import datetime

#datetime.now() pega a data, hora, minutos, segundo atual
now = datetime.now()

print now

current_year = now.year
current_month = now.month
current_day = now.day

print now.year
print now.month
print now.day

print '%s-%s-%s' % (now.year, now.month, now.day)
print '%s/%s/%s' % (now.day, now.month, now.day)
print '%s:%s:%s' % (now.hour, now.minute, now.second)

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)