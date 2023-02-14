# Restore Punctuation in multilingual ML translations as an API

## MAC/Linux Workflow for DEV:

### Create VENV

1. python -m venv venv
2. source venv/bin/activate
3. pip install --upgrade pip

### Install Py-Packages

If there is already a reaquirements.txt file:

1. pip install -r app/requirements.txt

If there is no requirements.txt file:

1. Install your Packages
2. pip freeze > app/requirements.txt

### Run Django DEV-Server

If you want to run the internal DEV-Server of Django, change the directory to the "app" directory. Then follow the steps below:

1. python3 manage.py makemigrations
2. python3 manage.py migrate
3. python3 manage.py runserver

The Server should now have the address: localhost:8000

## Run Production Server

The Repository ships with a build in docker-compose.yaml.

## Goal

API für Satzzeichenkorrektur.
Es soll für DEV und PROD funktionieren.
Datenarm über das Internet.

## Usage

### Input

Über die start.py lässt sich die Funktion "prod_call(input_wb, output_wb, model, url, max_row)" importieren.

'input_wb = /pfad/zur/input/excel/input.xlsx'

'output_wb = /pfad/zur/output/excel/output.xlsx'

'model = "fullstop" | "punctall"'

'url = "http://aschenputtel.abinsall.com:8000/punctuation/"'

'max_row = INT'

Als Input wird eine Excel-Tabelle mit dem Format:
| gold_standard | stt_output |
| ---------------- | ---------------- |
| value 1.1 | value 1.2 |
| value 2.1 | value 2.2 |
| ... | ... |

erwartet. Das Erste und einzige Arbeitsblatt _MUSS_ den Titel "Tabelle1" haben!

### Output

Der Output ist eine Excel-Tabelle mit dem Namen "output.xlsx" im Arbeitsdirectory. Die Datei wird bei mehrmaligem Aufruf überschrieben. Folgender Output wird erzeugt:
| original | processed |
| ---------------- | ---------------- |
| value 1.1 | value 1.2 |
| value 2.1 | value 2.2 |
| ... | ... |
