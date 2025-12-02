from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <body>
        <div style="text-align: center;">
        <h2>TestApp</h2>
        <img src="/static/natu.jpg" width="600"><br>
        <br>
        こんにちは！これはRenderで公開されたアプリです。<br>
        <br>
        <form action="/run-script" method="post">
            <button type="submit">Run Python Script</button>
        </form>
        </div>
        </body>
        </html>
    '''

@app.route('/run-script', methods=['POST'])
def run_script():
    # 実行したいPythonスクリプトを指定
    subprocess.run(['python3', 'my_script.py'])
    return "Script executed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
