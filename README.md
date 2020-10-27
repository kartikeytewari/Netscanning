# Netscanning
### The tool for scanning your network

The script scans your network (wifi, mobile hotspot and ethernet) and determines the devices connected to it. To setup the programme for the first time just run the setup script. From then on scanning is possible by running the command `python3 main.py` in the folder where it is stored.

The setup scripts asks for the host router's IP. The network that is scanned is the network that is hosted by this IP. Then number of devices that need to be monitored is asked. Then for every device, it's local IP and device name is asked. After the setup just run the main.py script. It will scan the Local network, and display the devices name that are connected to the system network.

The network properties are stored in the .env file as environment variables. The setup script writes to it, for installing the system for the first time.

Also, I understand that asking user's for there devices IP is kind of complicated. I will soon add functionality that will make the onboring process and the associated friction easier.

Tech Stack Used:
<ol>
    <li> C++ </li>
    <li> Python3 </li>
    <li> Bash Script </li>
    <li> Unix Pipelining </li>
</ol>
