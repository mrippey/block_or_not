# block_or_not
Script to quickly glean information on suspect IPv4 addresses and host names utilizing API's from GreyNoise and Farsight Security's DNSDB. Also included is the ability to grab a screen shot of the suspect webpage. The output for the host information and screen shot will be saved to the current working directory from which you ran the script. 

## Requirements
* Python3
* Python GreyNoise  (https://github.com/GreyNoise-Intelligence/pygreynoise) Requires an API Key!
* dnsdb Python Client  (https://pypi.org/project/dnsdb/) Also requires an API Key!
* Selenium

## Usage
![alt text](https://github.com/msec1203/block_or_not/blob/master/block_or_not.png)

## Examples
Output for IPv4 address
![alt text](https://github.com/msec1203/block_or_not/blob/master/block_or_not_ip.png)

Output for host name
![alt text](https://github.com/msec1203/block_or_not/blob/master/block_or_not_host.png)

Output for screen shot
![alt text](https://github.com/msec1203/block_or_not/blob/master/block_or_not_screen.png)
