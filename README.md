# Tufts University Research Technology Guides

[![][website-badge]][website-url]&nbsp;
[![][workflow-badge]](../../actions/workflows/build.yml)&nbsp;
[![][commit-badge]](../../commits/main)

Source repository for end user documentation developed by the Research Technology department at Tufts University.

⚠️ **Please see the [published website][website-url] for content.** The following is a development guide intended for staff.

## Overview

Documentation is built from source files using [Sphinx][sphinx-url] and the [PyData Sphinx Theme][theme-url] with content structure managed by the [Sphinx External ToC][toc-url] extension. Key repository contents are as follows:

- `/.github/workflows/build.yml` -- action to automatically build and deploy documentation
- `/environment.yml` -- build environment specification
- `/source/_ext/` -- custom Sphinx extensions
- `/source/_static/` -- static HTML content like the website logo and favicon
- `/source/_templates/` -- custom [Jinja][jinja-url] templates including new templates and default overrides
- `/source/_toc.yml` -- [Sphinx External ToC][toc-url] site-map structure configuration file
- `/source/404.md` -- custom 404 page template
- `/source/conf.py` -- [Sphinx][sphinx-url] configuration file
- `/source/index.md` -- documentation/webiste root (default landing page)

Everything else in `/source/` are content source files along with other artifacts like data and images. The following content source file types are supported:

- Jupyter Notebook `.ipynb`
- Markdown `.md`
- R Markdown `.Rmd` (restictions apply)
- reStructuredText `.rst`

The build process generates the following git-ignored directories that should not be manually modified:

- `/buid/` -- all build artifacts
- `/jupyter_execute/` -- executed Jupyter Notebooks derived from source files
- `/source/tags/` -- automatically generated source files for the tags index

## Environment Setup

Clone the repository and create the build environment using `mamba` or `conda` and the provided configuration file. Install and configure [Miniforge](https://github.com/conda-forge/miniforge) if you do not already have a Conda distribution present on your system.

```bash
mamba env install --file environment.yml
```

```bash
conda env install --file environment.yml
```

Remember to activate the environment before proceeding.

```bash
conda activate guides
```

## Local Development Builds

Local development builds can either be triggered manually via tyhe `sphinx-build` command or automatically by using [`sphinx-autobuild`](https://github.com/executablebooks/sphinx-autobuild). The latter continuously scans source files for changes and displays an up-to-date HTML preview using a local web server. Note that URLs relative to the content root will be broken in local builds.

### Automatic Build

The `/source/tags/` directory must be ignored during the automatic build process as its contents are regenerated at the start of every build, which would otherwise result in a continuous rebuild loop.

```bash
sphinx-autobuild source build --ignore */tags/*
```

Navigate to http://127.0.0.1:8000 to display the live-updated HTML preview.

### Manual Build

```bash
sphinx-build source build
```

Open the [`/build/index.html`](./build/index.html) file to display the generated HTML landing page.

### Ensuring a Clean Build

The build process creates various cached artifacts resulting in subsequent builds only updating pages for which the source files have been updated. This results in changes to the documentation configuration, structure, or extensions not being reflected unless all cached artifacts are removed. A clean build is also required in the case of updated tags and to ensure any executable code is re-run. Results of executable code are also cached and code is not re-run by default unless changes to the code are detected. The `build`, `jupyter_execute`, and `source/tags` directories should be removed if present to ensure a clean build. See below for sample commands.

#### Bash and Zsh

```bash Bash
rm -r build && rm -r jupyter_execute && rm -r source/tags
```
#### PowerShell

```powershell
Remove-Item -Recurse build && Remove-Item -Recurse jupyter_execute && Remove-Item -Recurse source/tags
```
#### Command Prompt

```bat
RMDIR /S /Q build && RMDIR /S /Q jupyter_execute && RMDIR /S /Q source/tags
```

<!----------------------------------------------------------------------------->

[jinja-url]: https://jinja.palletsprojects.com
[commit-badge]: https://img.shields.io/github/last-commit/tuftsrt/guides
[sphinx-url]: https://www.sphinx-doc.org
[theme-url]: https://pydata-sphinx-theme.readthedocs.io
[toc-url]: https://sphinx-external-toc.readthedocs.io
[website-badge]: https://img.shields.io/website?url=https://tuftsrt.github.io/guides/
[website-url]: https://tuftsrt.github.io/guides/
[workflow-badge]: https://img.shields.io/github/actions/workflow/status/tuftsrt/guides/build.yml
