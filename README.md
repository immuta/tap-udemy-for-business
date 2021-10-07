# tap-udemy-for-business

`tap-udemy-for-business` is a Singer tap for Udemy For Business. API documentation can be found
on the [Udemy website](https://business-support.udemy.com/hc/en-us/articles/360005792753-Udemy-Business-API-Reference).
This tap uses the "course sync and daily reporting API". One caveat to be aware of
is that the daily reporting API is not continuously updated, but is instead updated once a day,
so high-frequency syncs are generally not necessary.

Built with the [Singer SDK](https://gitlab.com/meltano/singer-sdk).

## Installation

To install this tap, use the latest version on PyPi:

```bash
pip install tap-udemy-for-business
```

## Configuration

### Accepted Config Options

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-udemy-for-business --about
```

## Usage

You can easily run `tap-udemy-for-business` by itself or in a pipeline using [Meltano](www.meltano.com).

### Executing the Tap Directly

```bash
tap-udemy-for-business --version
tap-udemy-for-business --help
tap-udemy-for-business --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

You will need a development environment to begin:

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_udemy_for_business/tests` subfolder and then run:

```bash
poetry run pytest
```

You can also test the `tap-udemy-for-business` CLI interface directly using `poetry run`:

```bash
poetry run tap-udemy-for-business --help
```

### Singer SDK Dev Guide

See the [dev guide](../../docs/dev_guide.md) for more instructions on how to use the Singer SDK to 
develop your own taps and targets.
