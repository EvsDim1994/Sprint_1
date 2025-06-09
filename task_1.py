
time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

time_values = time_string.split(',')

total_minutes = 0

for value in time_values:

    value = value.replace(' ', '')
    
    if 'h' in value:
        hours = int(value.split('h')[0])
        total_minutes += hours * 60

    if 'm' in value:
        minutes = int(value.split('m')[0].split('h')[-1])
        total_minutes += minutes

    if 's' in value:
        seconds = int(value.split('s')[0].split('h')[-1].split('m')[-1])
        if seconds % 60 == 0:
            total_minutes += seconds // 60

print("Общее количество минут:", total_minutes)
