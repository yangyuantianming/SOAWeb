#!/usr/bin/env python3

from flask import Flask, render_template, jsonify
import example

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('result.html',
                           graph=example.graph,
                           searchlist=example.searchlist)

@app.route('/api/details')
def details():
    """Get detail of an wikipedia entry by ID.

    Method: GET

    Arguments:
        id: the ID of the wikipedia entry.

    Returns:
        retcode: 0 if succeeded, 1 if id does not exist.
        title: the title of the entry.
        ns: unknown.
        id: the id of the entry.
        redirect (optional): the entry may redirect to other entries.
        revision (object): the revision information:
            id
            parentid
            timestamp
            contributor (object): the contributor of the revision:
                username
                id
                ip
            comment:
                model
                format
                text
    """
    try:
        # id = request.form['id']
        return jsonify(dict(retcode=0,details=example.details))
    except KeyError:
        return jsonify(dict(retcode=1))

@app.route('/api/related')
def related():
    """Get the relation graph and related entry list to the entry by id.

    Arguments:
        id: the entry id.

    Returns:
        retcode: 0 if succeeded, 1 if id does not exist.
        graph (object): the graph, see /search.
        searchlist (object): the list, see /search.
    """
    try:
        # id = request.form['id']
        return jsonify(dict(retcode=0,
                            graph=example.graph,
                            searchlist=example.searchlist))
    except KeyError:
        return jsonify(dict(retcode=1))

if __name__ == '__main__':
    app.run()
