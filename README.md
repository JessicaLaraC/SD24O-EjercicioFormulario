# Registro de Usuarios con FastAPI

Esta practica implementa un sistema básico para el registro de usuarios utilizando **FastAPI**. El sistema incluye un formulario HTML para capturar información del usuario y un servidor que procesa las solicitudes para guardar los datos enviados, como nombre, dirección y fotografía, en carpetas específicas dependiendo de si el usuario es **VIP** o no.

---

## 🚀 Funcionalidades

1. **Formulario de Registro:**
   - Captura los siguientes datos del usuario:
     - Nombre
     - Dirección
     - Fotografía
     - Indicador de usuario VIP (checkbox)
   - El formulario envía los datos al servidor mediante una solicitud `POST`.

2. **Servidor con FastAPI:**
   - Recibe los datos enviados desde el formulario.
   - Guarda las fotografías en carpetas separadas según el tipo de usuario:
     - `usuarios_vip/` para usuarios VIP.
     - `usuarios/` para usuarios regulares.
   - Imprime en la terminal los datos enviados:
     - Nombre.
     - Dirección.
     - Si es VIP o no.

3. **Carpetas Dinámicas:**
   - Si las carpetas `usuarios_vip` o `usuarios` no existen, el sistema las crea automáticamente.

---

## 🛠️ Requisitos

- **Python 3.9+**
- Dependencias del proyecto:
  - `fastapi`
  - `uvicorn`

---

