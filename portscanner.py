# The socket library was imported to connect two nodes making possible communication between them
import socket 

# The TermColor library has the role of printing different statements using colors
import termcolor


# This function has the role of scanning a target (port) - take port 1 then execute the function scan_port, after taking port 2 executes the function scan_port and so on
def scan(targets, ports):
    print('\n' + ' Starting Scan For ' + str(targets))
    for port in range(1,ports):
        scan_port(targets,port)


#Connection is performed and a function has been created to scan ports by ipaddress address
def scan_port(ipaddress, port):
    try:
        sock = socket.socket() 
        sock.connect(ipaddress, port)
        print("[+] Port Opened" + str(port))
        sock.close()
    except:
        #One can enter the PASS function to see only open ports
        print("[-] Port Closed" + str(port))
        
        
targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
        print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(' '), ports)
else:
        scan(targets,ports)
