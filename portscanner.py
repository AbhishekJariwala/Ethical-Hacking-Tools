import socket #helps us communicate with other machines using TCP/UDP protocols

# FUNCTION TO ITERATE THROUGH ALL PORTS
def scan(target, ports):
    print('\n Starting Scan For ' + str(target))
    for port in range(1,ports):
        scan_port(target,port)

# FUNCTION TO CONNECT TO PORT
def scan_port(ipaddress, port):
    try: #successful connection
        sock = socket.socket()
        sock.connect((ipaddress, port)) 
        print("[+] Port Opened: " + str(port))
        sock.close()
    except: #failed connection
        print("[-] Port Closed: " +str[port]) # displaying closed ports, which should be commented out for a cleaner output. We don't care much about closed ports and we can work backwards to find it out given the open ports


hostname=socket.gethostname()   
host_ip =socket.gethostbyname(hostname)   
print("Your Computer Name is:"+hostname)   
print("Your Computer IP Address is:"+host_ip)   
print("-----")

targets = input("[*] Enter Targets to Scan (split by ,): ")
ports = int(input("[*] Enter Amount of Ports to Scan: "))

if ',' in targets: # if scanning multiple targets
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '),ports)
else: # if scanning one target
    scan(targets,ports)