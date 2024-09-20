import subprocess

def test_predict_fen(url):
    cmd = ['python', 'tensorflow_chessbot.py', '--url', url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)

test_predict_fen('https://i.redd.it/nj3r8l4x6uld1.jpeg')
