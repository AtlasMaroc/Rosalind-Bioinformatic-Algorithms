import json

nb_path = 'c:/Users/HP/Documents/pytorch_learning/initialization_optimization.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        new_source = []
        for line in cell['source']:
            if 'from IPython.display import set_matplotlib_formats' in line:
                new_source.append('import matplotlib_inline\n')
            elif "set_matplotlib_formats('svg', 'pdf')" in line:
                new_source.append("matplotlib_inline.backend_inline.set_matplotlib_formats('svg', 'pdf') # For export\n")
            else:
                new_source.append(line)
        cell['source'] = new_source

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
