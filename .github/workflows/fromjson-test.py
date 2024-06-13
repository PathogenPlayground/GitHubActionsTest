#!/usr/bin/env python3
import json

import gha

gha.set_output('matrix', '{"include":[{"project":"foo","config":"Debug"},\n{"project":"bar","config":"Release"}]}')
