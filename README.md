# Python Selenium Google Search 

Simple Python/Selenium project

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes.

### Prerequisites

In order to run the project we need first to download the Firefox geckodriver and add the executable to the operating system's PATH. It can be found at this [repository](https://github.com/mozilla/geckodriver/releases).

### Installing and running the project

I. First, clone this repository at some directory, cd into it. Then create a virtual environment:

```bash
$ python3 -m venv venv
```

II. Activate the virtual environment and install the project dependencies:

```bash
$ source venv/bin/activate
$ pip install -r requirements.txt
```

III. Create a json file to use as an input to the application, something like:

```json
{
  "google-me": [
    "Nextel",
    "telefonia do futuro",
    "selenium python"
  ]
}
```
We have one ready for you ;)

IV. Run the project:

```bash
$ python main.py -f [json_file]
```

It should generate an `output.json` at the project's directory root, containing the search results from the input file. The results can also be seen in the console.

Also, you can run the unit tests:

```bash
$ py.test -v
```

## Author

* [**Ricardo Burger Schalch**](https://github.com/rschalch)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
