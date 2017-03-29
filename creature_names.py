#!/usr/bin/python

import sys
import os
import json

def set_to_names(code):
    with open(os.path.join("sets", code + ".json")) as f:
        set_data = f.read()
    return creature_names(set_data)

def creature_names(data):
    return [c["name"] for c in json.loads(data)["cards"]
            if "Creature" in c["types"]]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("\n".join(set_to_names(sys.argv[1])))
    else:
        print("\n".join(creature_names(sys.stdin.read())))
