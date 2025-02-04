# CheckGov

CheckGov is a Python script that checks if `.gov` domains are up and publishes the results on a web page with a green check mark if the domain is up and a red X mark if it is not.

## Requirements

- Python 3.x
- Flask
- Requests

## Installation

1. Clone the repository or download the script.
2. Install the required packages using pip:

    ```sh
    pip install flask requests
    ```

3. Create a [domains.txt](http://_vscodecontentref_/0) file in the same directory as [checkgov.py](http://_vscodecontentref_/1) with the list of domains you want to check, one per line. For example:

    ```txt
    https://www.usa.gov
    https://www.nasa.gov
    https://www.fbi.gov
    ```

## Usage

1. Run the script:

    ```sh
    python checkgov.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to see the status of the domains.

## License

This project is licensed under the MIT License.
