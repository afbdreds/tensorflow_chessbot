import re
from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

# Set working directory to the directory where app.py is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def predict_fen(image_url):
    cmd = ['python', 'tensorflow_chessbot.py', '--url', image_url]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output = result.stdout
        print("Subprocess Output:", output)  # Debugging line
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"
    
    # Use regex to find the FEN more reliably
    fen_match = re.search(r"Predicted FEN:\s*(.*)", output)
    if fen_match:
        fen = fen_match.group(1).strip()
        print("Extracted FEN:", fen)  # Debugging line
        return fen
    
    print("FEN not found in output")  # Debugging line
    return "Error: FEN not found in output"

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        data = request.json
        image_url = data.get('url')
        
        if not image_url:
            return jsonify({'error': 'No image URL provided'}), 400
    elif request.method == 'GET':
        image_url = request.args.get('url')
        
        if not image_url:
            return jsonify({'error': 'No image URL provided'}), 400

    fen = predict_fen(image_url)
    return jsonify({'FEN': fen})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
