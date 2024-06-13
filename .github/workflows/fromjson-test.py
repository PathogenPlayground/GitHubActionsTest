#!/usr/bin/env python3
import json

import gha

gha.set_output('matrix', '{"include":[{"project":"foo","config":"Debug"},{"project":"bar","config":"Release"}]}')
