from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.responses import HTMLResponse

from pathlib import Path

app = FastAPI()

# Directorios para guardar las fotos
ARCHIVO = Path(__file__).parent
ARCHIVO_VIP = ARCHIVO / "usuarios_vip"
ARCHIVO_USUARIO = ARCHIVO / "usuarios"

# Crear carpetas si no existen
ARCHIVO_VIP.mkdir(parents=True, exist_ok=True)
ARCHIVO_USUARIO.mkdir(parents=True, exist_ok=True)

@app.post("/registro_exitoso")
async def upload_user(
    nombre: str = Form(...),
    direccion: str = Form(...),
    vip: bool = Form(False),
    fotografia: UploadFile = File(...)
):
    
    print(f"Nombre: {nombre}")
    print(f"Dirección: {direccion}")
    print(f"Usuario VIP: {'Sí' if vip else 'No'}")
    
    # Guardar la fotografía en el directorio correspondiente
    if vip:
        respuesta = ARCHIVO_VIP / fotografia.filename
    else:
        respuesta = ARCHIVO_USUARIO / fotografia.filename

    with open(respuesta, "wb") as buffer:
        buffer.write(await fotografia.read())

    return {"message": "Usuario registrado correctamente"}

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)
