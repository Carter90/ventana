from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Test Blank Page!'

if __name__ == '__main__':
    app.run()
