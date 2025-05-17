import  { Suspense } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Environment, useGLTF } from '@react-three/drei';

import type { GLTF } from 'three-stdlib';

function Model({ url }: { url: string }) {
  const gltf = useGLTF(url) as GLTF;
  return <primitive object={gltf.scene} />;
}

export default function ModelViewer({ uuid }: { uuid: string }) {
  const glbUrl = `http://localhost:5000/get-glb/${uuid}`; // Adjust if your API is on a different host/port
  return (
    <Canvas camera={{ position: [2, 2, 2], fov: 50 }} style={{ width: '100vw', height: '100vh' }}>
      <ambientLight intensity={0.8} />
      <Suspense fallback={null}>
        <Model url={glbUrl} />
        <Environment preset="sunset" />
      </Suspense>
      <OrbitControls />
    </Canvas>
  );
}
