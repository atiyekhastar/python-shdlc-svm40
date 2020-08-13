# Python Driver for Sensirion SVM40 Evaluation Kit

This package contains the SHDLC driver for the SVM40 Evaluation Kit as a Python
package. For details, please read the package description in
[README.rst](README.rst).

## Usage

See package description in [README.rst](README.rst) and user manual at
https://sensirion.github.io/python-shdlc-svm40/.

## Development

We develop and test this driver using our company internal tools (version
control, continuous integration, code review etc.) and automatically
synchronize the `master` branch with GitHub. But this doesn't mean that we
don't respond to issues or don't accept pull requests on GitHub. In fact,
you're very welcome to open issues or create pull requests :)

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

### Run tests

Unit tests can be run with [`pytest`](https://pytest.org/):

```bash
pip install -e .[test]          # Install requirements
pytest -m "not needs_device"    # Run tests without hardware
pytest                          # Run all tests
```

The tests with the marker `needs_device` have following requirements:

- An SVM40 device must be connected to the computer.
  - **WARNING: Some tests modify non-volatile configurations of the device,
    restore factory defaults etc.! Do not run the tests on a device which you
    don't want to get modified!**
- You have to specify the serial port (and optionally other connection
  parameters) used to connect to the SVM40 device:
  - `--serial-port`: The serial port where the device is connected
    (e.g. `COM7`).


### Build documentation

The documentation can be built with [Sphinx](http://www.sphinx-doc.org/):

```bash
pip install -e .[docs]          # Install requirements
cd docs && make html            # Build documentation
```

## License

See [LICENSE](LICENSE).
