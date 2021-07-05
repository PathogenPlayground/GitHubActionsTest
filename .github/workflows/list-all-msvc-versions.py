#!/usr/bin/env python3
import os

install_base = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\"
editions = os.listdir(install_base)

for edition in editions:
    edition_path = os.path.join(install_base, edition)
    msvc_tools_path = os.path.join(edition_path, "VC", "Tools", "MSVC")
    versions = os.listdir(msvc_tools_path)

    print(f"====== Visual Studio 2019 {edition} found in {edition_path} ======")
    for version in versions:
        print(f"    MSVC {version}")
