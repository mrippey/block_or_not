#!/usr/bin/env python3
__author__ = 'Mike R @nahamike01'
__description__ = 'Quickly scan an IPv4 address, host, or get a screen shot of a suspicious host domain '
__date__ = '2020/03/30'

import argparse
from greynoise import GreyNoise
from dnsdb import Dnsdb
from selenium import webdriver
from time import sleep
import dns.resolver
import os, sys


def lkup_sus_ip_address(susp_addr):
    """Find RDNS of IP address and return info using GreyNoise API.

    Args:
        susp_addr: Suspect IPv4 address.
    Returns:
        Domain (if found) & GreyNoise Output (if found).
    Raises:
        Error: if susp_addr domain name cannot be found.
    """
    try:
        rev = dns.reversename.from_address(susp_addr)
        output = str(dns.resolver.query(rev, 'PTR')[0])

        api_client = GreyNoise(api_key="", timeout=15)
        bring_the_noise = api_client.ip(susp_addr)

        print("Found domain: {}".format(output))
        print('*'*80)
        print(bring_the_noise)

    except dns.resolver.NXDOMAIN as e:
        print(e)


def lkup_susp_host(susp_host):
    """Find host information using dnsdb.

    Args:
        susp_host: Suspect host.
    Returns:
        Domain & historical information using PassiveDNS (if applicable). File is placed in current directory /
        as host_lookup_report.json.

    """
    print('Starting domain lookup...')
    file_write_to_cwd = os.getcwd()
    dnsdb_api_key = ""
    dnsdb = Dnsdb(dnsdb_api_key)
    output_of_host = dnsdb.search(name=susp_host)

    output_to_document = output_of_host.records

    with open(os.path.join(sys.path[0], "host_lookup_report.json"), "a") as targetfile:
        targetfile.write(str(output_to_document))
        targetfile.write("/n")

    print(f"File written to {file_write_to_cwd}")


def get_screen_shot(susp_site):
    """Find host information using dnsdb.

        Args:
            susp_site: Suspect host to get screen shot for.

        Returns:
            PNG file of host name entered, written to current directory.
    """
    screen_shot_to_dir = os.getcwd()
    driver = webdriver.Firefox()
    driver.get(susp_site)
    sleep(1)

    driver.get_screenshot_as_file('host_lookup_screen.png')
    driver.quit()
    print(f"Screenshot successfully saved to {screen_shot_to_dir}")


def main():
    print("""
    
 __ )  |            |     _ \        \  |       |   
 __ \  |  _ \   __| |  / |   |  __|   \ |  _ \  __| 
 |   | | (   | (      <  |   | |    |\  | (   | |   
____/ _|\___/ \___|_|\_\\___/ _|   _| \_|\___/ \__|
    

BlockOrNot Quick IP/Domain Lookup Tool
----------------------------------------------------------------
Purpose: Provide three quick options to lookup a suspicious IP address or host name

Examples:
python block_or_not.py --ip 1.2.3.4
python block_or_not.py --host example.com
python block_or_not.py --screen http://example.com
    
    """)

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description="IP/Host quick info lookup")

    parser.add_argument('--ip', help="Provide target ipv4 address", type=lkup_sus_ip_address, dest='ip')

    parser.add_argument('--host', help ="Provide target domain name", type=lkup_susp_host, dest='host')

    parser.add_argument('--screen', help= "Provide host name to capture screenshot", type=get_screen_shot, dest='screen')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()

