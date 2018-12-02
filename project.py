import serial
import requests

ser = serial.Serial('/dev/ttyACM0', 9600)

def enviar_distancia(tacho_id, distancia):
    ENDPOINT = 'https://arduinio.herokuapp.com/api/levels/'
    #ACCESS_TOKEN = 'ce5c8302adb16aa7258a8d6b003dbc9ec3b0e9ea'
    payload = {
        'distance': distancia,
        'trash_can': tacho_id,
    }
    #headers = {
    #    'Authorization': ' '.join(['Token', ACCESS_TOKEN]),
    #}
    return requests.post(ENDPOINT, data=payload, auth=('kenjork', 'kenjork'))


if __name__ == '__main__':
    #distancia = distance()
    #tacho_id = 2
    while True:
        print('Distance:')
        print(ser)
        x = ser.readline()
        distance = x.decode().strip()
        print(x.decode().strip())
        response = enviar_distancia(1, distance)
        print(response)


