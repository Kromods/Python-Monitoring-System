import psutil
import time

#Funktion zum Überwachen der CPU-Auslastung
def monitor_cpu():
    cpu_info = []
    cpu_info.append("CPU-Auslastung:")
    cpu_info.append(f" Gesamte CPU-Auslastung: {psutil.cpu_percent(interval=1)}%")
    cpu_info.append(f" CPU-Kerne: {psutil.cpu_count(logical=True)}")
    cpu_info.append(f" CPU-Frequenz: {psutil.cpu_freq().current} MHZ\n")
    return "\n".join(cpu_info)

#Funktion zum überwachen des Arbeitsspeichers
def monitor_memory():
    memory = psutil.virtual_memory()
    memory_info = []
    memory_info.append("Arbeitsspeicher:")
    memory_info.append(f" Gesamter RAM: {memory.total / (1024**3):.2f} GB")
    memory_info.append(f" Verfügbarer RAM: {memory.available / (1024**3):.2f} GB")
    memory_info.append(f" RAM-Auslastung: {memory.percent}%\n")
    return "\n".join(memory_info)

#Funktion zum Überachen der Festplatte
def monitor_disk():
    disk = psutil.disk_usage('/')
    disk_info = []
    disk_info.append("Festplatteninformation:")
    disk_info.append(f"  Gesamter Speicherplatz: {disk.total / (1024**3):.2f} GB")
    disk_info.append(f"  Verfügbarer Speicherplatz: {disk.free / (1024**3):.2f} GB")
    disk_info.append(f"  Speicherplatz-Auslastung: {disk.percent}%\n")
    return "\n".join(disk_info)

#Funktion zum Überachen des Netzwerks 
def monitor_network():
    net_io = psutil.net_io_counters()
    net_info = []
    net_info.append("Netzwerkdaten:")
    net_info.append(f" Gesendete Daten: {net_io.bytes_sent / (1024**2):.2f} MB")
    net_info.append(f" Empfange Daten: {net_io.bytes_recv / (1024**2):.2f} MF\n")
    return "\n".join(net_info)

#Hauptüberwachungsfunktion mit eingabe in eine Datei
def monitor_system():
    with open("monitoring_results.txt", "a") as file:
      while True:
        file.write("_" * 40+"\n")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n" ) #aktuelle Zeit wird hinzugefügt
        file.write(monitor_cpu())
        file.write(monitor_memory())
        file.write(monitor_disk())
        file.write(monitor_network())
        file.write("_" * 40 + "\n\n")

        #Wartezeit von 10 Sekunden
        time.sleep(15)

#Warnsystem hier einfügen

#Überwachung starten
if __name__ == "__main__":
    monitor_system()

