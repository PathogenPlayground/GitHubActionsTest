#!/usr/bin/env python3
import json

import gha

matrix = {
    'include': [
        {
            'project': 'foo',
            'config': 'Debug'
        },
        {
            'project': 'bar',
            'config': 'Release'
        },
    ]
}

#gha.set_output('matrix', '{"include":[{"project":"foo","config":"Debug"},\n{"project":"bar","config":"Release"}]}')

matrix_json = json.dumps({ "include": matrix }, indent=2)
print(matrix_json)
gha.set_output('matrix', matrix_json)
