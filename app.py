from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <head>
        <title>WebApp</title>
        <style>
          .shadow{
            padding: 10px; color: #CCC; font-weight: bold; font-size: 30px; margin: 0;
            text-shadow: 3px 3px 0px #000, -3px -3px 0px #000, -3px 3px 0px #000, 3px -3px 0px #000,
                         3px 0px 0px #000, -3px -0px 0px #000,  0px 3px 0px #000, 0px -3px 0px #000;
          }
          body {
            background-image: url('/static/kabe2.jpg');
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;
          }
        </style>
        <link rel="manifest" href="/manifest.json" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <link rel="apple-touch-icon" href="/static/icon-192.png" />
        </head>
        <body>
        <div style="text-align: center;">
        <h2><p class="shadow">TestApp</p></h2>
        <img src="/static/natu.jpg" width="600"><br>
        <br>
        こんにちは！これはRenderで公開されたアプリです。<br>
        <br>
        <form action="/run-script" method="post">
            <button type="submit">Run Python Script</button>
        </form>
        </div>
        <script>
          if ("serviceWorker" in navigator) {
            navigator.serviceWorker.register("/service-worker.js")
              .then(() => console.log("Service Worker registered"))
              .catch(console.error);
          }
        </script>
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
