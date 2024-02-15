def descomponer_ip(ip):
    try:
        octetos = ip.split('.')
        for octeto in octetos:
            print(octeto)
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo de uso
ip = "192.168.1.1"
descomponer_ip(ip)
