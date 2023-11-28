# UMCCR MultiQC template

A MultiQC template that organises data and adds additional formatting to the base MultiQC report.

This template provides:

* colouring of samples (tumor [red], normal [blue], references [grey])
* automatic hiding and renaming of duplicate normal sample entries<sup>\*</sup>
* ordering of sample and reference entries according to configuration
* sash variant counts as custom MultiQC content
* module configuration and display order
* table column display settings

<br />

*<sup><sup>\*</sup>MultiQC shows different data under two normal sample entries for the DRAGEN module when provided outputs
from DRAGEN somatic and DRAGEN normal runs.</sup>*
