import { useState } from "react";
import axios from "axios";

function App() {
  const [url, setUrl] = useState("");
  const [format, setFormat] = useState("mp3");
  const [downloadLink, setDownloadLink] = useState("");

  const handleConvert = async () => {
    try {
      const response = await axios.post(
        "http://localhost:5000/download",
        { url, format },
        { headers: { "Content-Type": "application/json" } } // 🔥 Asegura que se envían los datos correctamente
      );
  
      setDownloadLink(response.data.file);
    } catch (error) {
      console.error("Error al convertir:", error);
    }
  };

  return (
    <div>
      <h2>Conversor de YouTube a {format.toUpperCase()}</h2>
      <input
        type="text"
        placeholder="Introduce URL de YouTube"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />
      <select onChange={(e) => setFormat(e.target.value)}>
        <option value="mp3">MP3</option>
        <option value="mp4">MP4</option>
      </select>
      <button onClick={handleConvert}>Convertir</button>
      {downloadLink && <a href={downloadLink} download>Descargar {format.toUpperCase()}</a>}
    </div>
  );
}

export default App;
