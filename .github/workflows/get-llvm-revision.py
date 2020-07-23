#!/usr/bin/env python3
import os
import re
import subprocess

output = subprocess.check_output(["git", "submodule", "status", "external/llvm-project"], encoding='utf-8').strip()

match = re.compile(r"^.(?P<sha1>[a-f0-9]+) external/llvm-project.*").match(output)
assert(match is not None), f"Malformed Git output: '{output}'"

sha1 = match.group('sha1')
print(f"::set-output name=sha1::{sha1}")
