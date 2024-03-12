#!/usr/bin/env python3
"""
python makepyproject.py



"""
import jjcli
import jinja2
from glob import glob
import os
import json
__version__ = "0.0.1"

def main():
    mods = glob("*.py")
    if len(mods) >= 1 :
        name = mods[0].replace(".py","")
    else:
        name = input("Modulo?")

    version = jjcli.qx(f"grep __version__ {name}.py")
    print(version)

    pp = jinja2.Template("""

    [build-system]
    requires = ["flit_core >=3.2,<4"]
    build-backend = "flit_core.buildapi"

    [project]
    name = "{{name}}"
    authors = [
        {name = "{{author}}", email = "{{email}}"},
    ]
    version = "0.0.1"


    classifiers = [
        "License :: OSI Approved :: MIT License",
    ]
    requires-python = ">=3.8"
    dynamic = [ "description"]

    dependencies = [
        "jjcli","jinja2"
    ]

    [project.scripts]
    {{name}} = "{{name}}:main"



                         """)

    metadata_path = str(os.path.expanduser('METADATA.json'))
    file = open(metadata_path)
    #FIXME criar se não existir
    data = json.load(file)
    autor = data["Username"]
    email = data["Email"]

    out  = pp.render({"name":name,"author":autor, "email":email})
    print("DEBUG:",out)

    file_output = open("pyproject.toml","w")
    file_output.write(out)

if __name__ == "__main__" :
    main()