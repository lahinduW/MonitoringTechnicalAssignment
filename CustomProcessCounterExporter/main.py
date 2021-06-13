from prometheus_client import start_http_server, Gauge
import socket
import time
import psutil

if __name__ == '__main__':
   gauge = Gauge('system_process_count', 'System Process Count', [ 'HostName', 'HostIP'])
   start_http_server(8080)

   try:
      while True:
         gauge.labels( socket.gethostname(), socket.gethostbyname(socket.gethostname())).set(len(psutil.pids()))
         print("Running")
         time.sleep(1)
   except KeyboardInterrupt:
      print("Stoped")
