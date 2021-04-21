## Promotions

[![Build Status](https://www.travis-ci.com/DevOpsS21-Promotions/promotions.svg?branch=main)](https://www.travis-ci.com/DevOpsS21-Promotions/promotions)
[![codecov](https://codecov.io/gh/DevOpsS21-Promotions/promotions/branch/main/graph/badge.svg?token=RPDAV3A5I6)](https://codecov.io/gh/DevOpsS21-Promotions/promotions)


## Overview

The promotions resource is a representation of a special promotion or sale that is running against a product or perhaps the entire store. Some examples are "buy 1 get 1 free", "20% off", etc. Discount promotions usually apply for a given duration (e.g., sale for 1 week only).

## Contents

The project contains the following:

```text
service/            - service python package
├── __init__.py     - package initializer
├── models.py       - module with promotion models
└── service.py      - module with service routes

tests/              - test cases package
├── __init__.py     - package initializer
├── test_models.py  - test suite for promotion models
└── test_service.py - test suite for service routes

.coveragerc         - settings file for code coverage options
.gitignore          - this will ignore vagrant and other metadata files
.travis.yml         - travis configuration file
dot-env-example     - copy to .env to use environment variables
requirements.txt    - list if Python libraries required by your code
manifest.yml        - ibm cloud foundry configuration file
runtime.txt         - python version to be used at runtime
Procfile            - a command to run by the container
config.py           - configuration parameters
setup.cfg           - nosetests configuration file
LICENSE             - Apache 2.0
Vagrantfile         - Vagrant file that installs Python 3 and PostgreSQL
```

## Setup

### Prerequisite Installation using Vagrant
The easiest way to use this is with Vagrant and VirtualBox. If you don't have this software the first step is download and install it. If you have an 2020 Apple Mac with the M1 chip, you should download Docker Desktop instead of VirtualBox. Here is what you need:
Download: Vagrant
Intel Download: VirtualBox
Apple M1 Download: Apple M1 Tech Preview
Install each of those. Then all you have to do is clone this repo and invoke vagrant:

### Using Vagrant and VirtualBox
```bash
Git clone https://github.com/DevOpsS21-Promotions/promotions.git
cd promotions
vagrant up
```
You can now ssh into the virtual machine and run the service and the test suite:
```bash
vagrant ssh
cd /vagrant
```

### Starting Service
To run the service use honcho (Press Ctrl+C to exit):
```bash
cp dot-env-example .env
honcho start
```
Open the web page in a local browser at: http://localhost:5000

### Running the Tests
## Manually running the Tests

This repository has both unit tests and integration tests. You can now run `nosetests` and `behave` to run the TDD and BDD tests respectively.

### Test Driven Development (TDD)

This repo also has unit tests that you can run `nose`

```sh
nosetests
```

Nose is configured to automatically include the flags `--with-spec --spec-color` so that red-green-refactor is meaningful. If you are in a command shell that supports colors, passing tests will be green while failing tests will be red.

### Behavior Driven Development (BDD)

These tests require the service to be running becasue unlike the the TDD unit tests that test the code locally, these BDD intagration tests are using Selenium to manipulate a web page on a running server.

Run the tests using `behave`

```sh
honcho start &
behave
```

Note that the `&` runs the server in the background. To stop the server, you must bring it to the foreground and then press `Ctrl+C`

Stop the server with

```sh
fg
<Ctrl+C>
```

Alternately you can run the server in another `shell` by opening another terminal window and using `vagrant ssh` to establish a second connection to the VM. You can also suppress all log output in the current shell with this command:

```bash
honcho start 2>&1 > /dev/null &
```

or you can supress info logging with this command:

```bash
gunicorn --bind 0.0.0.0 --log-level=error service:app &
```
## Promotion Model
```text
“name” - name of promotion
“description” - description of promotion
“promo_code” - promotion code for promotion
“start_date” - start date of promotion
“end_date” - end date of promotion
“is_active” - Is the promotion active
```
## How To Use 
RESTful service for Promotions
```text
GET /promotions - Returns a list all of the Promotions
GET /promotions/{id} - Returns the Promotion with a given id number
POST /promotions - creates a new Promotion record in the database
PUT /promotions/{id} - updates a Promotion record in the database
DELETE /promotions/{id} - deletes a Promotion record in the database
PUT /promotions/{id}/cancel - cancels a Promotion record in the database
```
---
<sub> This repository is part of the NYU class **CSCI-GA.2810-001: DevOps and Agile Methodologies** taught by John Rofrano, Adjunct Instructor, NYU Curant Institute, Graduate Division, Computer Science.</sub>

