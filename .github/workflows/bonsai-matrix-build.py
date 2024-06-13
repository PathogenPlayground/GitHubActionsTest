#!/usr/bin/env python3
import json
import os

import gha

matrix = { }

def add(name: str, runner_os: str, rid: str, configurations: list[str] = ['Debug', 'Release']):
    platform = {
        'name': name,
        'os': runner_os,
        'rid': rid,
    }

    ret = { }
    for configuration in configurations:
        job = { 'platform': platform.copy(), 'configuration': configuration }
        matrix.append(job)
        ret[configuration] = job
    return ret

windows = add('Windows x64', 'windows-latest', 'win-x64')
linux = add('Linux x64', 'ubuntu-latest', 'linux-x64')

# Create packages and install from Windows Release x64
windows['Release']['create-packages'] = True
windows['Release']['create-installer'] = True

# Build dummy packages to determine which ones changed
def add_dummy(name: str):
    dummy = add(name, 'ubuntu-latest', 'linux-x64', 'Release')['Release']
    dummy['skip-tests'] = True
    dummy['dummy-build'] = True

add_dummy('Previous Dummy')
add_dummy('Next Dummy')

# Output
print(json.dump(matrix))
gha.set_output('matrix', json.dump(matrix))

gha.fail_if_errors()
