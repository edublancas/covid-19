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

    cwd = tempfile.mkdtemp()
    tmps.append(cwd)
    pipeline_converted = Path(cwd, 'pipeline.ipynb')
    pipeline_converted.write_text(nbformat.v4.writes(nb))

    out = str(p / 'pipeline.ipynb')

    pm.execute_notebook(str(pipeline_converted), out, cwd=cwd)


for tmp in tmps:
    shutil.rmtree(tmp)
