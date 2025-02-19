## Prerequisites

* Python 3.10

* Poetry 1.7.1

## Setup Instructions

1. Clone the repo
   ```sh
    $ git clone https://github.com/rbojan2000/bc-assignment
   ```
2. Change directory to `ingestion`
   ```sh
    $ cd ingestion
   ```
3. Create virtual environment in project. E.g.:
   ```sh
    $ python -m venv venv
   ```
4. Activate virtual environment
   ```sh
    $ source venv/bin/activate
   ```
5. Install all python libraries
   ```sh
    $ poetry install
   ```
6. Copy the desired CSV file to the ingestion/ directory. For example:
   ```sh
    $ cp dataset.csv ingestion/
   ```
7. Run the ingestion script
   ```sh
    $ python -m ingestion.main
   ```
