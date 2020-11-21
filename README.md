# Netscanning
### The tool for scanning your network

The script scans your network (WiFi, mobile hotspot and ethernet) and determines the devices connected to it. To setup the program for the first time just run the setup script. From then on scanning is possible by running the command `python3 main.py` in the folder where it is stored.

The setup scripts asks for the host router's IP. The network that is scanned is the network that is hosted by this IP. Then number of devices that need to be monitored is asked. Then for every device, it's local IP and device name is asked. After the setup just run the main.py script. It will scan the Local network, and display the devices name that are connected to the system network.

The network properties are stored in the .env file as environment variables. The setup script writes to it, for installing the system for the first time.

Also, I understand that asking user's for there devices IP is kind of complicated. I will soon add functionality that will make the onboarding process and the associated friction easier.

Setup instructions:
- Install the requisite modules from pip3 using:
    `pip3 install -r requirements.txt`
- Run the setup.sh file, after changing it's permissions:
    `chmod +x setup.sh`
    `./setup.sh`
- When, monitoring just run:
    `python3 main.py`

Tech Stack Used:
<ol>
    <li> C++ </li>
    <li> Python3 </li>
    <li> Bash Script </li>
    <li> Unix Pipelining </li>
</ol>
