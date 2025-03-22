# Crestwood College Scheduling System - Milestone 1

This directory contains the implementation of Milestone 1 of the Crestwood College Scheduling System, which focuses on data processing and validation.

## Overview

Milestone 1 is the "BASIC" milestone that cleans the raw Excel data, converts it to a structured JSON format, and validates it according to the specified rules.

## Files in this Milestone

- `dataset.xlsx` - Original dataset containing lecturer details, room data, course list, and student requests
- `process_dataset.py` - Script to clean the Excel data and convert to JSON format
- `examine_dataset.py` - Utility script to examine the raw dataset
- `processed_data.json` - Cleaned dataset in JSON format
- `validation_results.json` - Results of data validation checks
- `validation_report.md` - Documentation of data validation and insights
- `requirements.txt` - Python dependencies required to run the scripts

## How to Run

1. Ensure Python is installed
2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the data processing script:
   ```
   python process_dataset.py
   ```

This will:
- Read the dataset.xlsx file
- Clean and transform the data
- Generate processed_data.json
- Validate the data and generate validation_results.json

## Validation Process

The validation process checks for:
- Teacher conflicts (teacher assigned to multiple courses in the same block)
- Room capacity issues (too many students assigned to a room)
- Student conflicts (student requesting multiple courses in the same block)

The results of these validations are stored in `validation_results.json` and summarized in `validation_report.md`.