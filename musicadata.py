import os
import pandas as pd
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3


def cargar_biblioteca(carpeta="musica"):
  canciones = []

  # Crea la carpeta automáticamente si aún no existe
  if not os.path.exists(carpeta):
    os.makedirs(carpeta)
    print(f"Carpeta '{carpeta}/' creada. Guarda ahí tus .mp3 de prueba y vuelve a ejecutar.")
    return pd.DataFrame()

  for i, archivo in enumerate(os.listdir(carpeta), start=1):
    if archivo.lower().endswith(".mp3"):
      ruta = os.path.join(carpeta, archivo)
      audio = MP3(ruta)

      
      try:
        tags = EasyID3(ruta)
      except Exception:
        tags = {}

      canciones.append({
          "Codigo": f"TRK-{i:03d}",
          "Nombre": tags.get("title", [os.path.splitext(archivo)[0]])[0],
          "Artista": tags.get("artist", ["Desconocido"])[0],
          "Genero": tags.get("genre", ["Sin género"])[0],
          "Duracion_seg": round(audio.info.length, 1),
      })

  return pd.DataFrame(canciones)

if __name__ == "__main__":
  df = cargar_biblioteca("musica")
  print(df)