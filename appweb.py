from flask import Flask, render_template, request

from autocomplete import AutoComplete
from parsecommands import parseargs_autocomplete



app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def autocomplete():
    comps = []
    word_current = ''

    if request.method == 'POST':
        word_current = request.form['word']
        comps = ac.completions(word_current)

    return render_template('autocomplete.html', out_word=comps, 
                           word_current=word_current)


if __name__ == '__main__':

    # parse command line arguments
    args = parseargs_autocomplete()

    # setup trie
    ac = AutoComplete(args.corpus, 
                      nmin=args.nmin, case_sensitive=args.casesensitive)

    app.run()
