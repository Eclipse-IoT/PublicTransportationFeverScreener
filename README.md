
# Contactless Fever-Screening in Public Transportation

An RFID bus-pass reader with an IR thermal imager for mass fever detection in a public transportation or digital building setting.
(v 1.0.0 Mar 3, 2021)

## Use Cases

#### What is the problem?
> “In light of the global outbreak of the coronavirus (COVID-19), which is now officially a pandemic, society is deeply concerned about the spread of infection and seeking tools to help slow and ultimately stop the spread of the virus” [1]

“Advancements in transportation coupled with the growth and movement of human populations enable efficient transport of infectious diseases almost anywhere in the world within 24 hours” [2]. However, shutting down public transportation services is difficult to do as many people heavily rely on it.  “Public transportation is an essential service that helps to keep communities functioning. Limiting the availability of public transit disproportionately affects segments of the population that rely on it to get to school or work or to access essential goods or services”[3]. Because of this, many transit staff and young and/or lower income passengers who rely on public transportation on a daily basis, have no choice but to face a disproportionately higher risk of COVID-19 exposure [3]. This is why having implemented measures to mitigate these risks are essential, such as the use of PPE (personal protective equipment), physical distancing, constant disinfection/sanitization, and advising passengers to stay at home if they feel any symptoms [3]. 

Unfortunately, physical distancing may prove difficult to do when large numbers of people are forced to crowd the same vehicle, and self-reports are subjective and may be unreliable [2], [3]. Because of this, there is a clear need for a more effective passenger symptom screening tool.

#### What is the solution?
“Infrared thermal detection systems (ITDS) offer a potentially useful alternative to contact thermometry. This technology was used for fever screening at hospitals, airports, and other mass transit sites during the severe acute respiratory syndrome and influenza A pandemic (H1N1) 2009 outbreaks” [2]. “In settings such as travel sites (e.g., airports) and the workplace, ITDS could provide an objective means for the mass detection of fever as part of a comprehensive public health screening strategy because ITDS had greater accuracy than self-reports” [2]. 

The proposed solution consists of a simple IR thermal sensor collecting temperature data on the passenger and RFID scanner to act as a contactless payment method for a bus pass. The user must tap their pass for the fare, and immediately after scan their face for a temperature check. If the thermal sensor does not detect a fever, the passenger is allowed to board the vehicle/enter the station. If the sensor does detect a fever, the passenger will be identified as a potential COVID-19 risk, and will be escorted for further screening. 

#### *Why is this important?*

Transit staff and frequent passengers have no choice but to rely on public transportation, and since maintaining a physical distance may be difficult on a crowded vehicle, identifying COVID-19 carriers through this contactless screening method may prove extremely beneficial in mitigating their risk of transmission. 

#### *Key benefits*

**Keywords/Verticals:** 

## Architecture

#### What components is the demo using?

###### Software Components
- **[Eclipse Mosquitto](https://mosquitto.org/)**
  - MQTT broker implementation
- **[Cedalo Management Center](https://docs.cedalo.com/latest/docs/management-center/mc-overview)**
  - Web based management of Mosquitto instances
- **[Eclipse Paho Python](https://www.eclipse.org/paho/index.php?page=clients/python/index.php)**
  - Python implementation of Paho, used to implement MQTT clients

**Hardware Components**
- Raspberry Pi Model 3 B+
- Computer/Laptop
- AMG8833 Thermal Sensor
- RC522 RFID Reader/Writer
- 7 inch Touchscreen
- 3D printed components 

## Implementation

**Cloud Layer:**

**Internet of Things Layer:**

## Hardware Assembly

#### 1) 3D print the parts 
The parts are designed to be printed without needing supports, so ensure that the parts are correctly oriented on the buildplate. Printing is obviously optional, but it ensures that the thermal sensor is in a better position to detect your face. Otherwise, you may have to hold the sensor up to yourself with one hand , while also interacting with the RFID scanner with the other, which may prove difficult

#### 2) Heat set the brass threaded inserts
Position M3 brass threaded inserts into the holes of the RFIDHolder and the DisplayFront mounts, and gently press into place with a soldering iron

#### 3) Fasten RC522 scanner into mount
Using M3 screws, fasten the RC522 scanner into the RFIDHolder mount

#### 4) Fasten AMG8833 and Raspberry Pi
Using M2 screws and nuts, fasten the AMG8833 sensor to the top of the FrontDisplay mount, and the Raspberry Pi to the BackDisplay mount respectively

#### 5) Fasten touchscreen, FrontDisplay, and BackDisplay mount together
Place the touchscreen into the FrontDisplay mount, and sandwich the BackDisplay mount ontop of it, ensure that the holes are lined up correctly and screw them together using M3 screws

#### 6) Wire the AMG8833 sensor accordingly
- Sensor Vin to Pi 3v3
- Sensor GND to Pi GND
- Sensor SCL to Pi SCL
- Sensor SDA to Pi SDA

#### 7) Wire the RC522 scanner accordingly
- Sensor 3v3 to Pi 3v3
- Sensor RST to Pi GPIO 22
- Sensor GND to Pi GND
- Sensor MISO to Pi MISO
- Sensor MOSI to Pi MOSI
- Sensor SCK to Pi SCK
- Sensor SDA to Pi SDA

## How to run

### 1) Ensure that you have Eclipse Mosquitto and Cedalo Management Center installed on your desired server machine
Follow the installation instructions for your desired machine from the following link: https://docs.cedalo.com/latest/docs/installation

### 2) Ensure that you have CircuitPython installed on your Raspberry Pi
Follow the instructions from the following link: https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

### 3) Ensure that you have Paho installed on your client devices
Can be installed easily using:
```bash
pip install paho-mqtt
```

### 4) Launch Mosquitto and Management Center
This can be done by launching the start.bat file included with your installation (for Windows). When successfully started, the Management Center will be visible on http://localhost:8088. 

### 5) Create Client security details
Using the sidebar menu, navigate to the Client menu and create instances of clients with username and passwords for each client you are using

### 6) Launch Python scripts on their respective machines
Launch BusFeverDetector.py on the Raspberry Pi, and BusServer.py on your server machine.


