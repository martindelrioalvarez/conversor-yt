# conversor-yt

## **📌 Instalación y Configuración**  

### **1️⃣ Clonar el repositorio**  
```bash
git clone https://github.com/tu-usuario/conversoryt.git
cd conversoryt
```

### **2️⃣ Configurar el entorno**  

#### **Backend**  
```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### **Frontend**  
```bash
cd frontend
npm install
```

### **3️⃣ Instalar ffmpeg** 
#### Windows
1. Descarga FFmpeg desde: https://www.gyan.dev/ffmpeg/builds/
2. Extrae el archivo ZIP y mueve la carpeta a ```C:\ffmpeg```
2. Agrega ```C:\ffmpeg\bin``` a la variable de entorno **Path**:
   + Abre *Configuración de Windows* > *Variables de Entorno*
   + Busca la variable ```Path```, edítala y agrega: ```C:\ffmpeg\bin```
4. Verifica la instalación ejecutando en PowerShell:
    ```bash
    ffmpeg -version
    ```
#### Linux/macOS
```bash
sudo apt update && sudo apt install ffmpeg  # Ubuntu/Debian
brew install ffmpeg  # macOS con Homebrew
```

---

## **🖥️ Ejecución del Proyecto**  

### **1️⃣ Iniciar el Backend**  
```bash
cd backend
python app.py
```


### **2️⃣ Iniciar el Frontend**  
```bash
cd frontend
npm start
```
Abrir en el navegador:  
📌 [http://localhost:3000](http://localhost:3000)  

---