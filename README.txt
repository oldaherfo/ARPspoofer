**Warning:**
**The use of this tool is restricted only for educational and testing purposes. It should not be used on networks or systems without the explicit permission of the owner.**

# ARP Spoofer Tool
This is a simple ARP spoofing tool built in Python and Tkinter for the graphical interface. It sends spoofed ARP packets to a target IP address and a gateway to perform a Man-in-the-Middle (MITM) attack. The attack can be started and stopped using buttons in the graphical interface.

## Features
- Graphical interface built with Tkinter
- ARP packet spoofing
- Start and stop the attack through the graphical interface
- Simple and lightweight

## Requirements
This project requires Python and the following libraries:
- scapy
- tkinter

## How to Use
1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the `ARPspoofer.py` file.
4. Enter the victim's IP address and the gateway's IP address in the input fields.
5. Click "Start Attack" to initiate the attack.
6. Click "Stop Attack" to halt the attack.

## Program Execution
python ARPspoofer.py

I have also left an executable file "ARPpoissoning.exe" so you can test the program without installing any dependencies in Windows environments.

Make sure you have the necessary permissions and are testing in an authorized environment. ARP spoofing can disrupt network communication.

This project was created by oldaherfo - 2024. Use it responsibly.
