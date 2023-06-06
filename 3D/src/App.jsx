// import { useState } from 'react'
// // npm run dev
// const App = () => {

//   return (
//     <div>
//       3D Sorting Visualizer
//     </div>
//   )
// }

// export default App
import React from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Stars } from "@react-three/drei";
import * as THREE from "three";

function Box() {
  return (
    <mesh position={[0,0,1]} rotation={[-Math.PI / 2, 0,0]}>
      <boxBufferGeometry attach="geometry" />
      <meshLambertMaterial attach="material" color="hotpink" />
    </mesh>
  );
}

function Plane() {
  return (
    <mesh position={[0,0,0]}>
      <planeBufferGeometry attach="geometry" args={[100,100]}/>
      <meshLambertMaterial attach="material" color="seafoamgreen" />
    </mesh>
  );
}

const App = () => {
  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <Canvas style={{ background: "#000000" }}>
        3D Sorting Visualizer
        <OrbitControls />
        <Plane/>
        <Stars />
        <ambientLight intensity={0.2} />
        <spotLight position={[10, 15, 10]} angle={0.3} />
        <Box />
      </Canvas>
    </div>
  );
};
export default App;

// const scene = new THREE.Scene();

// const geometry = new THREE.BoxGeometry(10, 10, 10);
// const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
// const mesh = new THREE.Mesh(geometry, material);
// scene.add(mesh);

// // camera
// const camera = new THREE.PerspectiveCamera(
//   45, 800, 600
// );
// scene.add(camera);

// // const renderer = new THREE.WebGLRenderer();
// // renderer.setSize(window.innerWidth, window.innerHeight);
// // document.body.appendChild(renderer.domElement);

// // const cube = new THREE.Mesh(geometry, material);
// // scene.add(cube);

// // camera.position.z = 5;

// // renderer
// const canvas = document.querySelector(".webgl")
// const renderer = new THREE.WebGLRenderer({ canvas })
// renderer.setSize(800, 600)
// renderer.render(scene, camera);
