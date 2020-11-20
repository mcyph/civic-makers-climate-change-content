import csv
from datetime import datetime, timedelta
from time import sleep

# Needs historic all-data-csv.zip from
# https://hotspots.dea.ga.gov.au/files


DATE_FORMAT = '%Y/%m/%d %H:%M:%S'


with open('data_csv/hotspot_historic_out2.csv', 'w', newline='\n') as fout:
    out = csv.DictWriter(fout, fieldnames=['lat', 'long', 'temp_kelvin', 'power', 'confidence', 'date'])
    out.writeheader()
    written = set()

    with open(r'D:\Docs\Downloads\all-data-csv\hotspot_historic.csv', 'r') as f:
        for x, item in enumerate(csv.DictReader(f)):
            if not item['temp_kelvin'].strip():
                continue
            #print(item)

            item['id'] = int(item['id'])
            #item['start_dt'] = datetime.strptime(item['start_dt'].split('.')[0].split('+')[0], DATE_FORMAT)
            item['latitude'] = float(item['latitude'])
            item['longitude'] = float(item['longitude'])

            # Filter to only Australia
            if not -47.655947 < item['latitude'] < -5.825793:
                continue
            elif not 104.924160 < item['longitude'] < 165.240103:
                continue

            item['temp_kelvin'] = float(item['temp_kelvin'])

            if item['confidence']:
                item['confidence'] = float(item['confidence'])
            else:
                item['confidence'] = None

            item['datetime'] = datetime.strptime(item['datetime'].split('.')[0].split('+')[0], DATE_FORMAT)
            item['age_hours'] = int(item['age_hours'])
            item['australian_state'] = item['australian_state'].strip()

            if item['power']:
                item['power'] = float(item['power'])
            else:
                item['power'] = None

            if not item['australian_state']:
                continue
            elif item['temp_kelvin'] < 420: # ~150 degrees c
                continue
            elif item['confidence'] is not None and item['confidence'] < 75:
                continue

            # Get so values are over e.g. 2019-2020's summer
            print(item)
            date = (item['datetime']+timedelta(days=183)).strftime('%Y')
            key = (date, '%.1f' % (item['latitude']*12.0), '%.1f' % (item['longitude']*12.0))
            if key in written:
                continue   # INFORMATION LOSS WARNING!!!! ====================================================
            written.add(key)

            out.writerow({
                'lat': item['latitude'],
                'long': item['longitude'],
                'temp_kelvin': item['temp_kelvin'],
                'confidence': item['confidence'],
                'power': item['power'],
                'date': date
            })

            #if x > 100:
            #    break

print("DONE!!!")
