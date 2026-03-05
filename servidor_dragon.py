import socket
import threading
import random
import time

servidor_activo = True

def manejar_jugador(conn, addr):
    print(f"[CONEXION] Alumno conectado: {addr}")
    vida_p = 100
    vida_jefe = 150
    duelo_activo = True

    def jefe_ataca():
        nonlocal vida_p, duelo_activo
        # El hilo del jefe depende de la bandera del duelo
        while duelo_activo and vida_p > 0:
            time.sleep(random.randint(3, 5))
            if duelo_activo:
                dano = random.randint(10, 15)
                vida_p -= dano
                try:
                    conn.send(f"JEFE_GOLPE|{dano}|{max(0, vida_p)}".encode())
                except:
                    duelo_activo = False
                if vida_p <= 0: 
                    try: conn.send(b"DERROTA")
                    except: pass
                    duelo_activo = False

    threading.Thread(target=jefe_ataca, daemon=True).start()

    try:
        # El bucle del jugador depende de la bandera del duelo
        while duelo_activo:
            data = conn.recv(1024).decode()
            if not data or data == "SALIR":
                duelo_activo = False
            
            if duelo_activo and data == "ATACAR":
                dano = random.randint(15, 25)
                vida_jefe -= dano
                conn.send(f"PLAYER_GOLPE|{dano}|{max(0, vida_jefe)}".encode())
                
                if vida_jefe <= 0:
                    conn.send(b"VICTORIA")
                    duelo_activo = False
    except:
        duelo_activo = False
    finally:
        print(f"[FIN] Duelo finalizado para {addr}")
        conn.close()

# Configuracion inicial
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 5000))
server.listen()
print("--- SERVIDOR DEL DRAGON JEFE INICIADO EN PUERTO 5000 ---")

try:
    while servidor_activo:
        conn, addr = server.accept()
        threading.Thread(target=manejar_jugador, args=(conn, addr)).start()
except KeyboardInterrupt:
    servidor_activo = False
    print("\nCerrando servidor...")
finally:
    server.close()