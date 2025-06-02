import speedtest 

def test_speed():
    st = speedtest.Speedtest()  # S mayúscula

    # Obtener el mejor servidor automáticamente
    st.get_best_server()

    # Obtener la velocidad de descarga y subida
    download_speed = st.download() / 1_000_000  # Convertir a Mbps
    upload_speed = st.upload() / 1_000_000  # Convertir a Mbps

    # Obtener la latencia
    ping = st.results.ping

    # Mostrar los resultados
    print(f"Velocidad de descarga: {download_speed:.2f} Mbps")
    print(f"Velocidad de subida: {upload_speed:.2f} Mbps")
    print(f"Latencia: {ping} ms")

if __name__ == "__main__":
    test_speed()
