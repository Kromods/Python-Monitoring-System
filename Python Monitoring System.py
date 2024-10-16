import psutil
import time

#Funktion zum Überwachen der CPU-Auslastung
def monitor_cpu():
    print("CPU-Auslastung:")
    print(f" Gesamte CPU-Auslastung: {psutil.cpu_percent(interval=1)}%")
    print(f" CPU-Kerne: {psutil.cpu_count(logical=True)}")
    print(f" CPU-Frequenz: {psutil.cpu_freq().current} MHZ\n")

#Funktion zum überwachen des Arbeitsspeichers
def monitor_memory():
    memory = psutil.virtual_memory()
    print("Arbeitsspeicher:")
    print(f" Gesamter RAM: {memory.total / (1024**3):.2f} GB")
    print(f" Verfügbarer RAM: {memory.available / (1024**3):.2f} GB")
    print(f" RAM-Auslastung: {memory.percent}%\n")

#Funktion zum Überachen der Festplatte
def monitor_disk():
    disk = psutil.disk_usage('/')
    print("Festplatteninformation:")
    print(f"  Gesamter Speicherplatz: {disk.total / (1024**3):.2f} GB")
    print(f"  Verfügbarer Speicherplatz: {disk.free / (1024**3):.2f} GB")
    print(f"  Speicherplatz-Auslastung: {disk.percent}%\n")

#Funktion zum Überachen des Netzwerks 
def monitor_network():
    net_io = psutil.net_io_counters()
    print("Netzwerkdaten:")
    print(f" Gesendete Daten: {net_io.bytes_sent / (1024**2):.2f} MB")
    print(f" Empfange Daten: {net_io.bytes_recv / (1024**2):.2f} MF\n")

#Hauptüberwachungsfunktion
def monitor_system():
    while True:
        print("_" * 40)
        monitor_cpu()
        monitor_memory()
        monitor_disk()
        monitor_network()
        print("_" * 40)

        #Wartezeit von 10 Sekunden
        time.sleep(10)

#Überachung starten
if __name__ == "__main__":
    monitor_system()
