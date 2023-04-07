from cassandra.cluster import Cluster
from flask import Flask, render_template

app = Flask(__name__)

cluster = Cluster(['localhost'])
session = cluster.connect('rss_data')

@app.route('/')
def home():
    rows = session.execute('SELECT * FROM lemonde_data LIMIT 10')
    return render_template('templates/index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)