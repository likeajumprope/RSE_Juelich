# Checklist for Research Software Implementation and Project Management Plan 📝

## Overview
This document seeks to provide a checklist/plan on what to consider when starting a new research project

## 0. Think ahead 🧠
- what needs to be read and accessed by whom (human/machine?)
- what aspects are likely to be relevant for all projects?
- what legacy code will likely become relevant and should be transported in advance
- what choices should best be made now (repository, documentation style, conventions...), and which can be made a little later into the project

## 1. Version Control and Repository Management 📑
- **GitHub/GitLab Use:**
  - Create separate repositories for each study (`pilot_behav_1`, `pilot_behav_2`, `fmri_3`, `fmri_4`).
  - Maintain a shared repository for common scripts and utilities (e.g. `common_tools`).
  - Implement branches (such as `main`, `develop`, `feature/`) for fluent and parallel development.
  - Make use of 'Issues' for tracking of progress 

- **Since I will be using Neuroimaging: Datalad for Data Versioning:**
  - Use Datalad to manage raw, processed, and analysis datasets.
  - Structure datasets as standalone Datalad repositories (e.g., `data_raw`, `data_processed`).
  - Link Datalad datasets with Zenodo for data publication and DOI generation IF appropriate under given data security level.
  - Maintain a `dataset_description.json` file for each Datalad dataset, specifying data origin, structure, and usage guidelines. Adhere to one naming protocol (see below).

## 2. Folder Structure and Naming Conventions 📂
```
├── data/
│   ├── raw/
│   ├── processed/
│   └── analysis/
├── scripts/
│   ├── data_preprocessing/
|   
│   ├── analysis/
│   └── visualization/
├── tests/
├── docs/
├── results/
├── config/
├── environment.yml
├── README.md
└── LICENSE
```
- Use consistent naming conventions e.g. BIDS:
  - Data files: `subject-[id]_session-[id]_[datatype].csv`
  - Scripts: `data_preprocessing.py`, `run_analysis.py`
  - Results: `results_[study_name]_[date].csv`

## 3. Documentation Quality 💬
- Maintain a `README.md` with:
  - Project overview and purpose.
  - Installation instructions.
  - Usage examples.
  - Directory structure.
  - Dependencies and setup instructions.
  - Contribution guidelines.

- Maintain a `docs/` directory with:
  - Study-specific documentation (`pilot_behav_1.md`, `fmri_3.md`).
  - Function/class documentation with docstrings and type annotations.

- Automate documentation where possible?

## 4. Code Structure and Readability 👓
- Follow 1 style (e.g PEP 8 for Python https://peps.python.org/pep-0008/).
- Modularize code into reusable functions and classes.
- Implement object-oriented programming for data processing and analysis modules.
- Establish a shared library for common functions (`time_space_utils`).
- Integrate type checking with `mypy`.
- Refactor legacy code (if any) to reduce redundancy and improve maintainability.

## 5. Testing and Validation ☑️
- Start writing tests & use them!
- Use `pytest` for unit tests:
  - `test_data_loading.py`
  - `test_analysis_pipeline.py`
  - `test_visualization.py`

- Define test datasets with known outputs for validation.
- ideally, implement Continuous Integration/Continuous Delivery oder Deployment (CI/CD) pipelines for automated testing.
- Traack data structure and content integrity with Datalad.

## 6. Licensing and Citation 📘
- Include a `LICENSE` file using for example the MIT or Apache 2.0 license OR reassess licensing choice (https://choosealicense.com/)
- Add a `CITATION.cff` file for proper citation formatting.
- Publish data on Zenodo and OSF to generate DOIs for datasets and code.
- Document citations in a `references.md` file.

## 7. Reusability and Modularity 🏗️
- Develop modular scripts for data preprocessing, analysis, and visualization.
- Document each module with usage examples and expected inputs/outputs.
- Use Datalad to version datasets and track data "evolution".
- Structure analysis pipelines to run independently e.g. with configuration files (`config/params.json`).

## 8. Community Contributions (What community am I seeking? Study group? External?) :accessibility:
- Define contribution guidelines in `CONTRIBUTING.md`.
- Use Zenodo to archive key releases and datasets with persistent DOIs.
- Maintain a `code_of_conduct.md` outlining community standards.

## 9. Automation and CI/CD 🤖
- Consider creating a `Makefile` with common commands:
  - `make install` – Install dependencies.
  - `make test` – Run tests.
  - `make lint` – Run code linting.
  - `make clean` – Remove temporary files.

- Implement CI/CD pipelines using GitHub Actions or GitLab CI:
  - Automated testing and linting.
  - Documentation build and deployment.
  - Data integrity checks with Datalad.

