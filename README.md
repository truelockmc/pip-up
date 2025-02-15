# Python Package Auto-Updater

A simple Python script that checks for outdated packages and automatically updates them using `pip`. It also ensures that `pip` itself is up-to-date.

## Features

- Ensures `pip` is upgraded to the latest version.
- Fetches a list of outdated Python packages.
- Automatically updates each outdated package to the latest version.
- Provides feedback on the update process.

## How It Works

3. First the script updates `pip` to ensure the package manager is up-to-date.
1. The script  fetches a list of all outdated packages by running `pip list --outdated`.
2. It iterates over each outdated package and updates them to the latest version using `pip install --upgrade <package_name>`.
4. Finally, it prints a success message and waits for a few seconds before closing.

## Installation

Clone this repository or download the script.

```bash
git clone https://github.com/truelockmc/pip-pack-grader.git
```

Ensure you have Python installed and available in your system path.

## Usage

Just run the script, using double click or executing the cmd command "python [scriptname].py"

### What happens:

- The script will list and update all outdated packages in your environment.
- `pip` will also be updated to the latest version.

### Example Output:

```
Updating pip...
Successfully updated: pip
...
Getting list of outdated packages...
Updating packages...
Successfully updated: package1
Successfully updated: package2
...

All packages, including pip, have been successfully updated.
```

## Requirements

- Python 3.x
- `pip` package manager

## Contributing

Contributions are welcome! If you find bugs or want to suggest new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
