import './App.css';
import React, {useState} from 'react';
import axious from 'axios';

function App() {
  const [image, setImage] = useState('');
  const[noiseDim, setNoiseDim] = useState(100);
  const[numImages, setNumImages] = useState(1);
  const generateImage = async () =>{

    try{

      const response = await axious.get('http://127.0.0.1:5000/generate',{
        params:{
          noise_dim: noiseDim,
          num_images: numImages,
        },

      });
      setImage(response.data.image);

    } catch(error){
      console.error('Error when generating image/images', error);
    }

  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>DCGAN Image Generator</h1>
        <div>
          <label>
            Noise Dimension:
            <input
              type="number"
              value={noiseDim}
              onChange={(e) => setNoiseDim(e.target.value)}
            />
          </label>
          <label>
            Number of Images:
            <input
              type="number"
              value={numImages}
              onChange={(e) => setNumImages(e.target.value)}
            />
          </label>
        </div>
        <button onClick={generateImage}>Generate Image</button>
        {/* {error && <p className="error">{error}</p>} */}
        {image && <img src={`data:image/png;base64,${image}`} alt="Generated Face" />}
      </header>
    </div>
  );
}

export default App;
