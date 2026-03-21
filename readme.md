# PSYOPS

Python Systems and Ops Tools (PsyOps). A basic set of tools for server and terminal admin/ops.

## Description

This project provides a set of tools for server and terminal administration and operations. It includes functionality for port scanning, process scanning, checking system performance, getting logged-in users, and a memory game (for fun).

## Installation

1. Clone the repository.
2. Install the required dependencies:
   - psutil library: `pip install psutil networkscan`

## Usage

1. Run the application:
   - `python psyops.py`
   - Alternatively, you can run specific modules directly:
     - Port Scanning: `python modules/servscan.py`
     - Process Scanning: `python modules/processchk.py`
     - Check Performance: `python modules/stats.py`
     - Get Logged-in Users: `python modules/users.py`
     - Check installed Software: `python modules/software.py`
     - Get all devices on your network: `python modules/netscan.py`
     - Memory Game: `python modules/memgame.py`

## Modules

- `modules/servscan.py`: Port Scanning module.
- `modules/processchk.py`: Process Scanning module.
- `modules/stats.py`: System Performance module.
- `modules/users.py`: Get Logged-in Users module.
- `modules/software.py`: Check installed Software module.
- `modules/netscan.py` : Get all devices on your netwotk.
- `modules/memgame.py`: Memory Game module.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact [Federico Guzman](mailto:federicoguzman@gmail.com).
