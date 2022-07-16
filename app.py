from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "https://media3.giphy.com/media/FspLvJQlQACXu/giphy.gif?cid=790b7611338ae0eed3be135685192ccd3d44ace45f6b19f7&rid=giphy.gif&ct=g",
    "https://media4.giphy.com/media/8L0Pky6C83SzkzU55a/giphy.gif?cid=790b7611a249dce64841319c64da292e4a7f57a2c4e0417e&rid=giphy.gif&ct=g",
    "https://media1.giphy.com/media/du3J3cXyzhj75IOgvA/200.webp?cid=ecf05e479gimy5nvnsyucdrqp87u7ctp9zk6jksvui4fbray&rid=200.webp&ct=g",
    "https://media2.giphy.com/media/1GEATImIxEXVR79Dhk/200w.webp?cid=ecf05e479gimy5nvnsyucdrqp87u7ctp9zk6jksvui4fbray&rid=200w.webp&ct=g",
    "https://media1.giphy.com/media/M9kgjEsLG6LMbYC9dl/200.webp?cid=ecf05e47g7kou9sqqy3p8pby3eyfg2syda0k32xvdalwp7d2&rid=200.webp&ct=g",
    "https://media4.giphy.com/media/qgQUggAC3Pfv687qPC/200.webp?cid=ecf05e47g7kou9sqqy3p8pby3eyfg2syda0k32xvdalwp7d2&rid=200.webp&ct=g"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
