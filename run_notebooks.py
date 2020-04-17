"""
Run all notebooks
"""
import tempfile
from pathlib import Path
import os
import shutil

import papermill as pm
import nbformat
import jupytext
import jupyter_client

projects = [Path(p) for p in os.listdir('.')
            if Path(p).is_dir() and not p.startswith('.')]

tmps = []

for p in projects:
    print(f'Running {p}')
    pipeline = str(p / 'pipeline.py')
    nb = jupytext.read(pipeline)

    k = jupyter_client.kernelspec.get_kernel_spec('python3')

    nb.metadata.kernelspec = {
            "display_name": k.display_name,
            "language": k.language,
            "name": 'python3'
        }

    cwd = Path(tempfile.mkdtemp())
    tmps.append(str(cwd))
    pipeline_converted = cwd / 'pipeline.ipynb'
    pipeline_converted.write_text(nbformat.v4.writes(nb))

    out = str(p / 'pipeline.ipynb')

    # include requirements.txt
    shutil.copy(str(p / 'requirements.txt'), str(cwd / 'requirements.txt'))

    pm.execute_notebook(str(pipeline_converted), out, cwd=str(cwd))


for tmp in tmps:
    shutil.rmtree(tmp)
