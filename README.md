# pytest-demo
**README**

### Running pytest with `--maxfail=1`

The `--maxfail=1` option in pytest can be incredibly useful when debugging test cases. It prevents you from being overwhelmed by too many failures at once, particularly in large test suites. For instance, if a hundred tests fail in a suite of a thousand, it might indicate a system-wide problem. Ending the test suite early with `--maxfail=1` accelerates the feedback loop and conserves resources.

### Saving Test Results to File

While pytest's console output is helpful for manual testing, saving test results to a file becomes essential for tools like Continuous Integration servers. One common format for these files is JUnit's XML report format. Pytest offers an option to generate JUnit XML files for test results using `--junit-xml`. Simply execute:

```bash
python -m pytest --junit-xml report.xml
```

The generated report file follows the standard JUnit XML format, making it consumable by various reporting tools.

### Configuration

Although command-line options suffice for running tests on the fly, certain options are more suitable for permanent or CI environment configurations. pytest supports configuration files, with `pytest.ini` being a common choice. These files allow setting options more permanently and are loaded from the project's root directory.

A critical option in configuration files is `addopts`, enabling you to set options directly as if entered on the command line. You can explore and set various other options provided by pytest based on your project requirements.

To set up a configuration file, create a `pytest.ini` in your project's root directory and add:

```ini
[pytest]
addopts = -v
```

This configuration sets verbosity (`-v`), but you can tailor it to your needs.

For more information and options, refer to the pytest documentation online.