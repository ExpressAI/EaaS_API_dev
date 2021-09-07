# %%
from eaas_api import Client
import jsonlines


def read_jsonlines_to_list(file_name):
    lines = []
    with jsonlines.open(file_name, 'r') as reader:
        for obj in reader:
            lines.append(obj)
    return lines


client = Client()
client.load_config("config.json")  # you can change the settings for each metric in `config.json`

# To see supported metrics
print(client.metrics)

# %%
inputs = [{"src": "This is the source.", "refs": ["This is the reference one.", "This is the reference two."],
           "hypo": "This is the generated hypothesis."}]
metrics = ["bleu", "chrf"]  # Can be None for simplicity if you consider using all metrics

# To see the full metric list, use client.metrics
score_dic = client.score(inputs, metrics)  # inputs is a list of Dict, metrics is metric list
# %%
input_file = "./tests/inputs/multi_ref.jsonl"
inputs = read_jsonlines_to_list(input_file)
res = client.score(inputs)

inputs = [{"src": "This is the source.",
           "refs": ["This is the reference one.", "This is the reference two."],
           "hypo": "This is the generated hypothesis."}]

# %%
inputs = [{"src": "This is the source.",
           "refs": ["This is the reference one.", "This is the reference two."],
           "hypo": "This is the generated hypothesis."}]
metrics = ["bleu", "chrf"] # Can be None for simplicity if you consider using all metrics

# To see the full metric list, use client.metrics
score_dic = client.score(inputs, metrics) # inputs is a list of Dict, metrics is metric list