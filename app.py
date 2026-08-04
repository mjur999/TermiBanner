from flask import Flask, render_template, request, jsonify
import pyfiglet
import logging

R = '\033[1;31m'  
G = '\033[1;32m'  
Y = '\033[1;33m'  
B = '\033[1;34m'  
C = '\033[1;36m'  
P = '\033[1;35m'  
W = '\033[0m'     


app = Flask(__name__)

# Flask-এর অতিরিক্ত টার্মিনাল লগ বন্ধ রাখা
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

ALL_FONTS = [
    'standard',
    'block',
    'ansi_shadow',
    'slant',
    '3d_diagonal',
    '3-d',
    '3x5',
    '5lineoblique',
    'banner',
    'banner3-D',
    'big',
    'bubble',
    'caligraphy',
    'chunky',
    'cyberlarge',
    'digital',
    'doom',
    'epic',
    'fender',
    'graffiti',
    'isometric1',
    'isometric2',
    'letters',
    'alligator',
    'mini',
    'ogre',
    'puffy',
    'rectangles',
    'shadow',
    'speed',
    'starwars',
    'stop',
    'thin'
]

@app.route('/')
def index():
    active_fonts = sorted([f for f in ALL_FONTS if isinstance(f, str)])
    return render_template('index.html', fonts=active_fonts)

@app.route('/generate', methods=['POST'])
def generate_banner():
    data = request.json
    text = data.get('text', '')
    font = data.get('font', 'standard')
    
    if not text:
        return jsonify({'banner': ''})
    
    try:
        figlet = pyfiglet.Figlet(font=font)
        banner_text = figlet.renderText(text)
        
        if font == 'block':
            replacements = ['_', '-', '|', '/', '\\', '+', '`', "'"]
            for char in replacements:
                banner_text = banner_text.replace(char, '█')
                
    except Exception as e:
        banner_text = f"Error: {str(e)}"
        
    return jsonify({'banner': banner_text})


Banner = f"""
{Y}    █████ █████ ████  █   █ ███ {R}████   ███  █   █ █   █ █████ ████
{Y}      █   █     █   █ ██ ██  █  {R}█   █ █   █ ██  █ ██  █ █     █   █
{Y}      █   ████  ████  █ █ █  █  {R}████  █████ █ █ █ █ █ █ ████  ████
{Y}      █   █     █  █  █   █  █  {R}█   █ █   █ █  ██ █  ██ █     █  █
{Y}      █   █████ █   █ █   █ ███ {R}████  █   █ █   █ █   █ █████ █   █
{W}"""

print(Banner)
print(f"{R}                 ━━━━━━━#{Y}/{R} Create by{Y} mjur999 /{R}#━━━━━━━{W}\n")

print(f"    ━━###/ {Y}github = {G}https://github.com/mjur999/TermiBanner.git {W}/###━━{W}\n\n")


if __name__ == '__main__':
    PORT = 8080
    print("=======================================")
    print(f" [+] Server Running on: {Y}http://127.0.0.1:{PORT}{W}")
    print("=======================================\n")
    
    print(f" Server Running on: {Y}http://127.0.0.1:{PORT}{W}\n")
    app.run(host='127.0.0.1', port=PORT, debug=False, use_reloader=False)
