import requests
import matplotlib.pyplot as plt


def get_goldcoast():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    return_data = requests.get("http://www.bom.gov.au/fwo/IDQ60801/IDQ60801.94580.json", headers=headers)

    gc_bom_data = return_data.json()

    goldcoast = []
    records = gc_bom_data['observations']['data']
    i = 30
    while i != 0:
        goldcoast.append("{} {} {} {}".format(records[i]['local_date_time'], records[i]['air_temp'], records[i]['wind_spd_kmh'], records[i]['rel_hum']))
        i -= 1

    with open("response_gc.txt", 'w') as f:
        for i in goldcoast:
            f.write('{}\n'.format(i))

    return "gc"


def get_brisbane():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    return_data = requests.get("http://www.bom.gov.au/fwo/IDQ60901/IDQ60901.94576.json", headers=headers)

    bne_bom_data = return_data.json()

    brisbane = []
    records = bne_bom_data['observations']['data']
    i = 30
    while i != 0:
        brisbane.append("{} {} {} {}".format(records[i]['local_date_time'], records[i]['air_temp'], records[i]['wind_spd_kmh'], records[i]['rel_hum']))
        i -= 1

    with open("response_bne.txt", 'w') as f:
        for i in brisbane:
            f.write('{}\n'.format(i))

    return "bris"


def get_sunshinecoast():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    return_data = requests.get("http://www.bom.gov.au/fwo/IDQ60901/IDQ60901.94569.json", headers=headers)

    suncoast_bom_data = return_data.json()

    suncoast = []
    records = suncoast_bom_data['observations']['data']
    i = 30
    while i != 0:
        suncoast.append("{} {} {} {}".format(records[i]['local_date_time'], records[i]['air_temp'], records[i]['wind_spd_kmh'], records[i]['rel_hum']))
        i -= 1

    with open("response_suncoast.txt", 'w') as f:
        for i in suncoast:
            f.write('{}\n'.format(i))

    return "suncoast"


def make_temp_plot(location):
    x = []
    y = []

    if location == "gc":
        plot = open("response_gc.txt", 'r')
    elif location == "bris":
        plot = open("response_bne.txt", 'r')
    elif location == "suncoast":
        plot = open("response_suncoast.txt", 'r')
    else:
        return

    for row in plot:
        x.append(str(row[:10]))
        y.append(float(row[11:15]))

    print(x, y)

    plt.figure(figsize=(10,10))
    plt.gcf().subplots_adjust(bottom=0.25)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))
    plt.xticks(rotation=45)
    plt.plot(x, y, label='Air Temperature (°C)')
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (°C)')
    plt.savefig('temp.png')
    print("Temperature graph generated")


def make_wind_plot(location):
    x = []
    y = []

    if location == "gc":
        plot = open("response_gc.txt", 'r')
    elif location == "bris":
        plot = open("response_bne.txt", 'r')
    elif location == "suncoast":
        plot = open("response_suncoast.txt", 'r')
    else:
        return

    for row in plot:
        x.append(str(row[:10]))
        y.append(float(row[16:18]))

    print(x, y)

    plt.figure(figsize=(10,10))
    plt.gcf().subplots_adjust(bottom=0.25)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))
    plt.xticks(rotation=45)
    plt.plot(x, y, label='Wind Speed (km/h)')
    plt.xlabel('Date and Time')
    plt.ylabel('Wind speed (km/h)')
    plt.savefig('wind.png')
    print("Wind graph generated")


def make_humid_plot(location):
    x = []
    y = []

    if location == "gc":
        plot = open("response_gc.txt", 'r')
    elif location == "bris":
        plot = open("response_bne.txt", 'r')
    elif location == "suncoast":
        plot = open("response_suncoast.txt", 'r')
    else:
        return

    for row in plot:
        x.append(str(row[:10]))
        y.append(float(row[18:21]))

    print(x, y)

    plt.figure(figsize=(10,10))
    plt.gcf().subplots_adjust(bottom=0.25)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))
    plt.xticks(rotation=45)
    plt.plot(x, y, label='Relative Humidity (%)')
    plt.xlabel('Date and Time')
    plt.ylabel('Humidity (%)')
    plt.savefig('humidity.png')
    print("Humidity graph generated")


make_temp_plot("gc")
make_wind_plot("bris")
make_humid_plot("suncoast")

