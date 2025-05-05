import json
import os

from utils import reclog

config_path = "/media/luan/seagate/workspace/coding/projects/software/recovr/config.json"

def get_current_prefix():
    # checar se já existe um prefixo definido, e se não tiver, instruir a criar um
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            try:
                data = json.load(f)
                prefix = data["prefix"]
            except:
                prefix = None
    else:
        prefix = None

    if not prefix:
        print("You havent set a prefix yet, set one with: prefix --set '<new prefix>'")
        return
    
    return prefix

def write_new_prefix(new_prefix):
    # checar se o arquivo existe, e se existe, pelo seu conteúdo
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                # o arquivo existe mas está vazio ou malformado
                data = {}
    else:
        # criar o dict do json caso o arquivo não exista
        data = {}

    data["prefix"] = new_prefix

    with open(config_path, "w") as f:
        json.dump(data, f, indent=4)