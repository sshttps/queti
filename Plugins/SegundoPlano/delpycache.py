import threading
import time
import shutil
import os

def delete_pycache():
    while True:
        for root, dirs, files in os.walk(".", topdown=False):
            for name in dirs:
                if name == "__pycache__":
                    path = os.path.join(root, name)
                    try:
                        shutil.rmtree(path, ignore_errors=True)
                        print(f"Directorio {path} eliminado.")
                    except Exception as e:
                        print(f"No se pudo eliminar {path}: {e}")
        
        time.sleep(10) 


delete_thread = threading.Thread(target=delete_pycache)
delete_thread.start()
