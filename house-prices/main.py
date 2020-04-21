from pathlib import Path

from ploomber import DAG
from ploomber.tasks import ShellScript
from ploomber.products import File

out_dir = Path('output')
out_dir.mkdir(exist_ok=True)

dag = DAG()

# get data using kaggle API
source = ('kaggle competitions download '
          'house-prices-advanced-regression-techniques --path {{product}}')
compressed = ShellScript(source, File(out_dir / 'compressed'), dag,
                         name='compressed')

# unzip downloaded data
source = ('unzip {{upstream.first}}'
          '/house-prices-advanced-regression-techniques.zip -d {{product}}')
raw = ShellScript(source, File(out_dir / 'raw'), dag, name='raw')

compressed >> raw


dag.build()
