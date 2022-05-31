import requests
import matplotlib.pyplot as plt


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

    with open("./img/suncoast/response_suncoast.txt", 'w') as f:
        for i in suncoast:
            f.write('{}\n'.format(i))


def make_temp_plot():
    x = []
    y = []

    plot = open("./img/suncoast/response_suncoast.txt", 'r')

    for row in plot:
        x.append(str(row[:10]))
        y.append(float(row[11:15]))

    plt.figure(figsize=(10 ,10))
    plt.gcf().subplots_adjust(bottom=0.25)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))
    plt.xticks(rotation=45)
    plt.plot(x, y, label='Air Temperature (°C)')
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (°C)')
    plt.savefig('./img/suncoast/temp.png')


def make_wind_plot():
    x = []
    y = []

    plot = open("./img/suncoast/response_suncoast.txt", 'r')

    for row in plot:
        x.append(str(row[:10]))
        y.append(float(row[16:18]))

    plt.figure(figsize=(10 ,10))
    plt.gcf().subplots_adjust(bottom=0.25)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))
    plt.xticks(rotation=45)
    plt.plot(x, y, label='Wind Speed (km/h)')
    plt.xlabel('Date and Time')
    plt.ylabel('Wind speed (km/h)')
    plt.savefig('./img/suncoast/wind.png')


def make_humid_plot():
    x = []
    y = []

    plot = open("./img/suncoast/response_suncoast.txt", 'r')

    for row in plot:
        x.append(str(row[:10]))
        y.append(float(row[18:21]))

    plt.figure(figsize=(10 ,10))
    plt.gcf().subplots_adjust(bottom=0.25)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))
    plt.xticks(rotation=45)
    plt.plot(x, y, label='Relative Humidity (%)')
    plt.xlabel('Date and Time')
    plt.ylabel('Humidity (%)')
    plt.savefig('./img/suncoast/humidity.png')


get_sunshinecoast()
make_humid_plot()
make_temp_plot()
make_wind_plot()
