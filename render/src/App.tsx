import { useState } from "react";
import './App.css';
import ModelViewer from "./components/ModelViewer";

function App() {
  const [shape, setShape] = useState("sphere");
  const [size, setSize] = useState(2);
  const [uuid, setUuid] = useState<string | null>(null);

  const handleGenerate = async () => {
    const response = await fetch("http://localhost:5000/generate-glb", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ shape, size: Number(size) })
    });
    const data = await response.json();
    setUuid(data.uuid);
  };

  return (
    <div className="App">
      <div>
        <input value={shape} onChange={e => setShape(e.target.value)} placeholder="Shape" />
        <input value={size} type="number" onChange={e => setSize(Number(e.target.value))} placeholder="Size" />
        <button onClick={handleGenerate}>Generate GLB</button>
      </div>
      {uuid && <ModelViewer uuid={uuid} />}
    </div>
  );
}
export default App;