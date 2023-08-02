# Integration of single cell transcriptomic atlases of the adult human and mouse ventral midbrain
This project is made by Chen Ji Rong "Jack" Jiang in collaboration with the [BasakLab](https://basaklab.com/). Special thanks to Professor [Onur Basak](https://www.linkedin.com/in/onur-basak-a2b96468). This project is still in progress...

## About

The project aims to provide a unified atlas of adult mouse and human ventral midbrain atlases. In order to achieve this goal, a computational pipeline that will facilitate integration of atlases of other brain areas will be established. This repository contains scripts used in this project.

## Installation Python packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [Scanpy](https://scanpy.readthedocs.io/en/stable/), [Harmonypy](https://github.com/slowkow/harmonypy), [SCALEX](https://github.com/jsxlei/SCALEX), [scHPL](https://github.com/lcmmichielsen/scHPL) and [UNIFAN](https://github.com/doraadong/UNIFAN).

### Unix/macOS
```
python -m pip install -r requirements.txt
```

### Windows
```
py -m pip install -r requirements.txt
```

## Installation R packages
Use package developer [devtools](https://www.r-project.org/nosvn/pandoc/devtools.html) to install [Seurat](https://satijalab.org/seurat/), [Harmoney](https://github.com/immunogenomics/harmony), [Escape](https://github.com/ncborcherding/escape), [scMiko](https://github.com/NMikolajewicz/scMiko) and [scPNMF](https://github.com/JSB-UCLA/scPNMF).
```
install.packages(c('devtools','Seurat'))
devtools::install_github(c("ncborcherding/escape", "NMikolajewicz/scMiko","JSB-UCLA/scPNMF", "immunogenomics/harmony" ))
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## License
This repository, [place_holder], is made available under the Open Database License: <http://opendatacommons.org/licenses/odbl/1.0/>. Any rights in individual contents of the database are licensed under the Database Contents License: <http://opendatacommons.org/licenses/dbcl/1.0/>
