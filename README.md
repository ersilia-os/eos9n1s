# Hemozoin inhibitor prediction using simple physicochemical parameters

Flags inhibitors of hemozoin formation, by which Plasmodium crystallises the haem released during haemoglobin digestion and the mechanism targeted by quinine and chloroquine. Huy and colleagues screened 9,600 compounds in a cell-free assay, confirmed 224 hits by dose-response against 199 random negatives, and fitted a multivariate logistic regression on three physicochemical properties, for AUC 0.736. Ersilia replicates that equation with RDKit logP, hydrogen bond donors and hydrogen count replacing the original ChemSpider values; the Bayesian variant is omitted as it needs refractive index.

This model was incorporated on 2026-02-03.
Last packaged on 2026-02-04.

## Information
### Identifiers
- **Ersilia Identifier:** `eos9n1s`
- **Slug:** `hemozoin-inhibition-physchem`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Malaria`
- **Target Organism:** `Plasmodium falciparum`
- **Tags:** `Antiparasitic activity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of inhibiting hemozoin crystallisation, with 0.536 the cut-off reported as optimal in the original study.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| tmm_proba | float | high | Traditional multivariate model probability of hemozoin inhibition |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Replicated`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos9n1s](https://hub.docker.com/r/ersiliaos/eos9n1s)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9n1s.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9n1s.zip)
- **Apptainer**: [https://models-sif.s3.eu-north-1.amazonaws.com/eos9n1s_v1.sif](https://models-sif.s3.eu-north-1.amazonaws.com/eos9n1s_v1.sif)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `500`
- **Image Size (Mb):** `450.49`

**Computational Performance (seconds):**
- 10 inputs: `27.78`
- 100 inputs: `17.49`
- 10000 inputs: `31.41`

### References
- **Source Code**: [https://github.com/ersilia-os/eos9n1s](https://github.com/ersilia-os/eos9n1s)
- **Publication**: [https://doi.org/10.1128/aac.01607-16](https://doi.org/10.1128/aac.01607-16)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2017`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9n1s
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9n1s
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
