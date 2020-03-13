import socket

def scanner(ip, port):
    try:
       socket.setdefaulttimeout(2)
       s = socket.socket()
       s.connect((ip,port))
       banner = s.recv(1024)
       return banner
    except Exception as e:
       return 

def checkVulns(banner):
    f = open("vuln_test.txt","r")
    for line in f.readlines():
        if line.strip('\n') in str(banner):
            print('[+] Server is vulnerable: '+str(banner).strip('\n'))
            
def main():
    ports = [21,22,25,80,110,443]
    for i in range(1,255):
        ip = "10.4.193." + str(i)
        for port in ports:            
            banner = scanner(ip, port)
            if banner:
                print('[+]'+ip+':'+str(banner).strip('\n'))                      
                checkVulns(banner)
                      
            

if __name__ == '__main__':
    main()
