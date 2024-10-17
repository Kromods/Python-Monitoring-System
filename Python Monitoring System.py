import psutil
import time

#Schwellenwert definieren
CRITICAL_CPU_THRESHOLD = 50.0 
CRITICAL_MEMORY_THRESHOLD = 80.0

#Funktion zum Überwachen der CPU-Auslastung
def monitor_cpu():
    cpu_info = []
    cpu_usage = psutil.cpu_percent(interval=1)

    cpu_info.append("CPU-Auslastung:")
    cpu_info.append(f" Gesamte CPU-Auslastung: {psutil.cpu_percent(interval=1)}%")
    cpu_info.append(f" CPU-Kerne: {psutil.cpu_count(logical=True)}")
    cpu_info.append(f" CPU-Frequenz: {psutil.cpu_freq().current} MHZ\n")

    #Warnung bei zu hoher CPU Auslastung 
    if cpu_usage >=CRITICAL_CPU_THRESHOLD:
        warning_message = f"!!! WARNUNG: CPU-Auslastung hat {CRITICAL_CPU_THRESHOLD}% überschritten ({cpu_usage}%) !!!"
        cpu_info.append(warning_message)
        print(warning_message) #Gib die Warnung in der Konsole aus 
        return "\n".join(cpu_info), warning_message #Rückgabe der CPU-Information und der Warnung
    
    return "\n".join(cpu_info), None #keine Warunung, nur CPU Daten zurückgeben


#Funktion zum überwachen des Arbeitsspeichers
def monitor_memory():
    memory = psutil.virtual_memory()
    memory_info = []

    memory_info.append("Arbeitsspeicher:")
    memory_info.append(f" Gesamter RAM: {memory.total / (1024**3):.2f} GB")
    memory_info.append(f" Verfügbarer RAM: {memory.available / (1024**3):.2f} GB")
    memory_info.append(f" RAM-Auslastung: {memory.percent}%\n")

    #Warnung bei zu Hohem RAM verbrauch
    if memory.percent >=CRITICAL_MEMORY_THRESHOLD:
        warning_message = f"!!! WARNUNG: RAM-Auslastung hat{CRITICAL_MEMORY_THRESHOLD}% überschritten ({memory.percent}%) !!!"
        memory_info.append(warning_message)
        print(warning_message) #Gib die Warnung in der Konsole aus 
        return "\n".join(memory_info), warning_message #Rückgabe der RAM INFO und der Warnung 
    
    return "\n".join(memory_info), None #Keine Warung, nur Memory Daten zurückgeben

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

#Hauptüberwachungsfunktion mit eingabe(&Warnungen) in eine Datei
def monitor_system():
    #Anzahl der Überwachungszyklen
    max_interations = 5 #nur 5 Durchläufe, dann stoppen 
    current_interation = 0 

    with open("monitoring_results.txt", "a") as file:
      while current_interation < max_interations:
        file.write("_" * 40+"\n")
        file.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n" ) #aktuelle Zeit wird hinzugefügt

        #Überwache CPU und speichere evtl.Warnung 
        cpu_data, cpu_warning = monitor_cpu()
        file.write(cpu_data)

        #CPU-Warnung in die Datei schreiben, falls vorhanden
        if cpu_warning:
            file.write(cpu_warning + "\n")

        #überwache RAM und speichere evtl.Warnung
        memory_data, memory_warning = monitor_memory()
        file.write(memory_data)

        #RAM-Warnung in die Datei schreiben, falls vorhanden
        if memory_warning:
            file.write(memory_warning + "\n")
        
        #Festplatten sowie Netzwerküberwachung
        file.write(monitor_disk())
        file.write(monitor_network())
        file.write("_" * 40 + "\n\n")

        #iterationszähler erhöhen
        current_interation +=1

        #Wartezeit von 15 Sekunden
        time.sleep(15)

#Warnsystem hier einfügen

#Überwachung starten
if __name__ == "__main__":
    monitor_system()

