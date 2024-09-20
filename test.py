import subprocess

# Define the path to the script and the image file
script_path = r"C:\Users\boldr\Downloads\tensorflow_chessbot-chessfenbot\tensorflow_chessbot.py"
image_path = r"C:\Users\boldr\Downloads\chesspdftofen-master\chesspdfpage\page_1_region_1_board_1.jpg"

# Run the command
result = subprocess.run(
    ["python", script_path, "--filepath", image_path],
    capture_output=True,
    text=True
)

# Print the output
print("Standard Output:\n", result.stdout)
print("Standard Error:\n", result.stderr)
