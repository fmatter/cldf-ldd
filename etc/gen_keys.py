import pandas as pd
import yaml
keys = pd.read_csv("etc/foreignkeys.csv")
keys["Target_Key"] = keys["Target_Key"].fillna("ID")
keys["Source"] = keys["Source"].apply(lambda x: f"{x}.csv" if x[0].upper() != x[0] else x)
keys["Target"] = keys["Target"].apply(lambda x: f"{x}.csv" if x[0].upper() != x[0] else x)
out = []
for i, key in keys.iterrows():
    out.append(list(key.values))
with open("src/cldf_ldd/components/keys.yaml", "w") as f:
    yaml.dump(out, f)