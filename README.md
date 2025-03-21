# Crestwood College Scheduling System

This project implements a course scheduling system for Crestwood College, designed to allocate students to courses based on their preferences while respecting constraints like room capacity, teacher availability, and time blocks.

## Project Structure

- `dataset.xlsx` - Original dataset containing lecturer details, room data, course list, and student requests
- `process_dataset.py` - Script to clean the Excel data and convert to JSON format
- `processed_data.json` - Cleaned dataset in JSON format
- `validation_report.md` - Documentation of data validation and insights
- `validation_results.json` - Results of data validation
- `scheduler.py` - Implementation of the scheduling algorithm (Milestone 2)
- `status_report.md` - Current status report of the project
- `README.md` - This file, with project overview and instructions

## Current Status

### Milestone 1 (BASIC) - COMPLETED ✅

The basic milestone has been completed:
- Raw Excel data has been cleaned and converted to JSON format
- Validations have been run on the data to check for conflicts and issues
- Insights have been documented in the validation report

### Milestone 2 (ADVANCED) - SKELETON IMPLEMENTATION 🚧

The advanced milestone is in progress:
- A skeleton implementation of the scheduling algorithm has been created in `scheduler.py`
- The code provides the structure for assigning students to courses based on their preferences
- It handles constraints like room capacity and time block conflicts
- Statistics tracking and reporting is implemented

## How to Run

### Environment Setup

1. Ensure Python is installed
2. Install required dependencies:
   ```
   pip install pandas openpyxl
   ```

### Running the Data Processing (Milestone 1)

```
python process_dataset.py
```

This will:
- Read the dataset.xlsx file
- Clean and transform the data
- Generate processed_data.json
- Validate the data and generate validation_results.json

### Running the Scheduler (Milestone 2)

```
python scheduler.py
```

This will:
- Load the processed data
- Generate course schedules for students
- Create teacher schedules
- Generate statistics and reports

## Next Steps for Milestone 2

To complete Milestone 2, the following should be implemented:

1. **Refine the Scheduling Algorithm**:
   - Consider using optimization libraries like PuLP, Google OR Tools, or Gurobi
   - Improve the prioritization logic (required > requested > recommended)

2. **Visual Representations**:
   - Generate blockwise student view schedules
   - Generate blockwise teacher view schedules

3. **Detailed Statistics**:
   - Calculate percentage of resolved vs. unresolved requests
   - Break down statistics by priority level

4. **Testing and Validation**:
   - Test with various scenarios to ensure robust scheduling
   - Verify that all constraints are properly respected

## File Details

### process_dataset.py

This script processes the Excel data and performs validation checks:
- Cleans column names and handles missing values
- Converts the data to a structured JSON format
- Checks for teacher conflicts, student conflicts, and room capacity issues
- Generates insights about the dataset

### scheduler.py

This script implements the scheduling algorithm:
- Processes student requests in order of priority
- Assigns students to course sections while respecting constraints
- Tracks statistics on fulfilled and unfulfilled requests
- Generates reports including student and teacher schedules

## Note

As mentioned in the assignment: "This is not a Leetcode problem, so don't treat it like one. Don't think of edge cases or 100% satisfaction as the first step." The current implementation focuses on providing a working solution that handles the core requirements, rather than aiming for perfect optimization from the start.