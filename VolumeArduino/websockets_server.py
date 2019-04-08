import asyncio
import websockets
import serial
from sound import Sound


def update_volume():
    line = ser.readline()
    deco = line.decode("utf-8")
    sensor_value = int(deco)
    target_volume = min(4 * sensor_value, 100)
    Sound.volume_set(target_volume)
    print("Target volume is : {0}".format(target_volume))
    return str(target_volume)


async def push_volume(websocket, path):
    while True:
        await websocket.send(update_volume())


if __name__ == '__main__':
    ser = serial.Serial('COM3', 9600)
    print('Connected to {0}'.format(ser.name))
    start_server = websockets.serve(push_volume, 'localhost', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()