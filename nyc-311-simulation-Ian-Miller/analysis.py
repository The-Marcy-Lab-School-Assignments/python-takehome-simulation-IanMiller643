import csv

rows = []

with open('nyc_311_requests.csv') as f: 
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

open_requests = 0
complaint_types = {}
requests_per_borough = {}
open_borough_requests = {}


for row in rows:
    if row['resolution_status'] == 'Open':
        open_requests += 1
        open_borough_requests[row['borough']] = open_borough_requests.get(row['borough'], 0) + 1

    complaint_types[row['complaint_type']] = complaint_types.get(row['complaint_type'], 0) + 1
    requests_per_borough[row['borough']] = requests_per_borough.get(row['borough'], 0) + 1
    

most_common_complaint = max(complaint_types, key=complaint_types.get)
most_open_borough_requests = max(open_borough_requests, key=open_borough_requests.get)
complaint_types = dict(sorted(complaint_types.items(), key=lambda item: item[1], reverse=True))

requests_per_borough = dict(sorted(requests_per_borough.items()))
top_three_boroughs = dict(sorted(requests_per_borough.items(), key=lambda item: item[1], reverse=True)[:3])

with open('output.txt', 'w') as f:
    f.write(f'Open requests: {open_requests}\n')
    f.write(f'\nMost common complaint type: {most_common_complaint}\n({complaint_types[most_common_complaint]} requests)\n')
    f.write(f'\nRequests per borough:')
    for borough, requests in requests_per_borough.items():
        f.write(f'\n- {borough}: {requests}')

    f.write(f'\n\nRequests by complaint type:')
    for complaint_type, requests in complaint_types.items():
        f.write(f'\n- {complaint_type}: {requests}')
    
    f.write(f'\n\nBorough with most open requests: {most_open_borough_requests} ({open_borough_requests[most_open_borough_requests]} open)')

    f.write(f'\n\nClosure rate by borough:')
    for borough in requests_per_borough:
        f.write(f'\n- {borough}: {round((requests_per_borough[borough] - open_borough_requests[borough]) / requests_per_borough[borough] * 100, 1)}%')

    f.write(f'\n\nTop 3 boroughs by total requests:')
    for num, borough in enumerate(top_three_boroughs, 1):
        f.write(f'\n{num}. {borough} ({top_three_boroughs[borough]} requests)')

print('Output saved to output.txt')