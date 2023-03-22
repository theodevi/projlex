from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hi(name=None):
    return render_template('main_page.html', name=name)

@app.route('/search_page.html')
def search_wrd(name=None):
    return render_template('search_page.html', name=name)

@app.route('/source_search.html')
def search_txt(name=None):
    return render_template('source_search.html', name=name)

if __name__ == '__main__':
    app.run()
