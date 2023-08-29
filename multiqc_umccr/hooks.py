import pathlib
import yaml


import multiqc.utils


def before_config():
    config_fp = pathlib.Path(__file__).parent / 'umccr_config.yaml'
    with config_fp.open('r') as fh:
        umccr_config = yaml.safe_load(fh)
        multiqc.utils.config.update(umccr_config)
