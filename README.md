# Arduino windows Audio volume control

This POC is to control Windows Audio Volume from Arduino using ultrasonic-sensor-hc-sr04 (Proximity sensor) and stream the information (by serial on COM3) to python and then through websocket.
The information is displayed in plain c3js chart.

## known Issues:
You dont have full control au audio controller so I'm using I hack from :
[https://github.com/Paradoxis/Windows-Sound-Manager](https://github.com/Paradoxis/Windows-Sound-Manager)
Sometime the level is set to 100 or 0 without reason.

## Docs: 
- [Music](https://www.musicscreen.be/musique-libre-de-droit-jazz1.html)
- [Arduino docs from HC SR04](https://howtomechatronics.com/tutorials/arduino/ultrasonic-sensor-hc-sr04/)
- [Paradoxis/Windows-Sound-Manager](https://github.com/Paradoxis/Windows-Sound-Manager)
- [pypi.org doc websockets](https://pypi.org/project/websockets/)
- [c3js.org gauge chart](https://c3js.org/samples/chart_gauge.html)