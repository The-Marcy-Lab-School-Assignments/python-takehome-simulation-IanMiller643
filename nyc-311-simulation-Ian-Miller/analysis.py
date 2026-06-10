import csv

rows = []

with open('nyc_311_requests.csv') as f: 
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

open_requests = 0
complaint_types = {}
requests_per_borough = {}

for row in rows:
    if row['resolution_status'] == 'Open':
        open_requests += 1

    complaint_types[row['complaint_type']] = complaint_types.get(row['complaint_type'], 0) + 1
    requests_per_borough[row['borough']] = requests_per_borough.get(row['borough'], 0) + 1

most_common_complaint = max(complaint_types, key=complaint_types.get)

requests_per_borough = dict(sorted(requests_per_borough.items()))

with open('output.txt', 'w') as f:
     f.write(f'Open requests: {open_requests}\n')
     f.write(f'\nMost common complaint type: {most_common_complaint}\n({complaint_types[most_common_complaint]} requests)\n')
     f.write(f'\nRequests per borough:')
     for borough, requests in requests_per_borough.items():
        f.write(f'\n- {borough}: {requests}')


print('Output saved to output.txt')