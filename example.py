graph = {
    'vertices': [
        {
            'id': 1, #节点id
            'attr': {
                'id':2, #这里是词项的id
                'name': 'Data Mining'
            }
        },
        {
            'id': 2, #节点id
            'attr': {
                'id':1,  #这里是词项的id
                'name': 'Machine Learning'
            }
        }
    ],

    'edges': [
        {
            'start': 1, #节点id
            'end': 2, #节点id
            'attr': {
                'weight': 2.0
            }
        }
    ]
}

searchlist = [
    {
        'id': 1,
        'title': 'Machine Learning',
        'desc': 'Machine Learning and related topics'
    },
    {
        'id': 2,
        'title': 'Data Mining',
        'desc': 'Data Mining and related topics'
    }
]

details = {
    'title': 'Data mining',
    'ns': 0,
    'id': 2,
    'redirect': 1,
    'revision': {
        'id': 124567,
        'parentid': 87654,
        'timestamp': '2015-02-29T25:61:61Z',
        'contributor': {
            'username': 'Tang',
            'id': '13239239',
            'ip': ''
        },
        'comment': {
            'model': 'wikitext',
            'format': 'text/x-wiki',
            'text': 'some modifications'
        }
    }
}
