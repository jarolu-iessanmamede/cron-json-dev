import src.utilidades.utilidades as util
import time
import subprocess

def run():
    trabajos = util.leer_jobs("data/trabajos.json")
    subprocesos_en_ejecucion = []
    try: 
        while(True):
            for t in trabajos:
                if int(time.time())>=t["ultima_ejecucion"]+t["frecuencia"]:
                    t["ultima_ejecucion"] = int(time.time())
                    fichero = open(f"logs/job_{t['id']:03}_{t['ultima_ejecucion']}.txt", "w")

                    s = subprocess.Popen(
                        t["run"],
                        stdout=fichero,
                        stderr=subprocess.STDOUT,
                        shell=True,
                        text=True,
                        encoding="UTF-8"
                    )
                    subprocesos_en_ejecucion.append((s,fichero))

            for s in subprocesos_en_ejecucion:
                if s[0].poll() is not None:
                    s[1].close()

            time.sleep(1)
        
    except KeyboardInterrupt as e:
        print(f"Se paró el programa {e}")



if __name__ == "__main__":
    run()