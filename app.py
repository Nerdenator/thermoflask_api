import json
import subprocess

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Raspberry Pi Thermal API</h1><p>This site maps out CPU and thermal information.</p>"


def get_temp():
    """
    returns output of vcgencmd measure_temp
    :return: temperature in degrees c to one-tenth of one degree
    """
    temp_c = subprocess.run(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE, text=True)
    len_temp_c = len(temp_c.stdout)
    # trim off "temp=" at the front and "'C" at the end
    if len_temp_c == 10:    # temp=x.x'C
        print(temp_c.stdout[-5:-2])
        return temp_c.stdout[-5:-2]
    elif len_temp_c == 11:  # temp=xx.x'C
        print(temp_c.stdout[-6:-2])
        return temp_c.stdout[-6:-2]
    elif len_temp_c == 12:  # temp=xxx.x'C
        print(temp_c.stdout[-7:-2])
        return temp_c.stdout[-7:-2]


def get_cpu_clock():
    """
    returns output of vcgencmd measure_clock arm
    :return: speed in Hz
    """
    cpu_clock = subprocess.run(['vcgencmd', 'measure_clock', 'arm'], stdout=subprocess.PIPE, text=True)
    print(cpu_clock.stdout[-10])
    return cpu_clock.stdout[-10]

@app.route('/api/v1/information/combined/immediate', methods=['GET'])
def api_immediate():
    """
    get the temperature and clock speed at the time of the API call.
    :return: json object with clock speed and temperature
    """
    dict_obj = {
        'temp': get_temp(),
        'clock_speed': get_cpu_clock()
    }

    json_frame = json.dumps(dict_obj)

    return json_frame


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
