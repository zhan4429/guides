# Tufts University Research Technology Guides

[![][website-badge]][website-url]&nbsp;
[![][workflow-badge]](../../actions/workflows/build.yml)&nbsp;
[![][last-commit-badge]](../../commits/main)

Source repository for end user documentation developed by the Research Technology department at Tufts University.

⚠️ **Please see the [published website][website-url] for content.** The following is a development guide intended for staff.

## Environment Setup

Create the development environment using `mamba` or `conda` and the provided `environment.yml` file.

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

## Build Locally

Remove the `build` and `source/tags` directories to ensure a clean build.

```bash
rm -r build && rm -r source/tags
```

```powershell
Remove-Item -Recurse build && Remove-Item -Recurse source/tags
```

```bat
RMDIR /S /Q build && RMDIR /S /Q source/tags
```

### Automatic Build

```bash
sphinx-autobuild source build --ignore */tags/*
```

### Manual Build

```bash
sphinx-build source build
```

<!-- define reference-style links -->

[website-url]: https://tuftsrt.github.io/guides/
[website-badge]: https://img.shields.io/website?url=https://tuftsrt.github.io/guides/
[workflow-badge]: https://img.shields.io/github/actions/workflow/status/tuftsrt/guides/build.yml
[last-commit-badge]: https://img.shields.io/github/last-commit/tuftsrt/guides
