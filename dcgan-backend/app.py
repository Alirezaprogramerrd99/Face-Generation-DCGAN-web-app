from flask import Flask, jsonify, send_file, request
from io import BytesIO
import torch
import torch.nn as nn
from torchvision.utils import save_image
import torchvision.transforms as transforms
import base64
from model import Generator
from constants import *
from pathlib import Path
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
generator = Generator(ngpu=ngpu).to(device)
saved_model_path = Path("model")
generator.load_state_dict(torch.load(saved_model_path / 'Generator.pth', map_location=device))
generator.eval()

@app.route("/") 
def index(): 
    return "Welcome to the face generation AI web app!"

@app.route('/generate', methods=['GET'])
def generate_image():
       # Get parameters from request
    noise_dim = int(request.args.get('noise_dim', 100))
    num_images = int(request.args.get('num_images', 1))
    
    # Generate random noise
    noise = torch.randn(num_images, noise_dim, 1, 1, device=device)
    
    # Generate image
    with torch.no_grad():
        fake_images = generator(noise).detach().cpu()
    
    # Save images to a BytesIO object
    buffer = BytesIO()
    save_image(fake_images, buffer, format='PNG', nrow=num_images)
    buffer.seek(0)
    
    # Encode image to base64
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

    print("Generated Image Data:", img_str[:100])
    
    return jsonify({'image': img_str})

if __name__ == '__main__':
    app.run(debug=True)