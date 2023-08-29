#!/usr/bin/env python3
import setuptools


setuptools.setup(
    name='multiqc_umccr',
    version='0.0.1',
    author='UMCCR and contributors',
    url='https://github.com/scwatts/mulitqc_umccr',
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        'multiqc.templates.v1': [
            'umccr = multiqc_umccr.templates.umccr',
        ],
        'multiqc.hooks.v1': [
            'before_config = multiqc_umccr.hooks:before_config',
        ],
    },
)
