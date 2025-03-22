# Crestwood College Scheduling System - Milestone 2

This directory contains the implementation of Milestone 2 of the Crestwood College Scheduling System, which focuses on the scheduling algorithm and visualization.

## Overview

Milestone 2 is the "ADVANCED" milestone that implements the scheduling algorithm to assign students to courses based on their preferences while respecting constraints like room capacity, teacher availability, and time blocks.

## Files in this Milestone

- `scheduler.py` - Implementation of the scheduling algorithm
- `scheduling_report.md` - Detailed report of the scheduling results
- `student_schedules.json` - Generated student schedules
- `teacher_schedules.json` - Generated teacher schedules
- `requirements.txt` - Python dependencies required to run the scripts

## How to Run

This milestone depends on the processed data from Milestone 1 (`processed_data.json`).

1. Ensure Python is installed
2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Make sure `processed_data.json` is available (copy from Milestone 1 if needed)
4. Run the scheduling script:
   ```
   python scheduler.py
   ```

This will:
- Load the processed data
- Generate course schedules for students
- Create teacher schedules
- Generate statistics and a detailed report

## Scheduling Algorithm

The scheduling algorithm:
- Processes student requests in order of priority (required → requested → recommended)
- Assigns students to course sections while respecting constraints:
  - No teacher conflicts (same teacher in different locations at the same time)
  - No room capacity issues (too many students in a room)
  - No student conflicts (same student in different courses at the same time)
- Tracks statistics on fulfilled and unfulfilled requests
- Generates reports including student and teacher schedules

## Output Files

- `student_schedules.json` - Contains block-wise schedules for all students
- `teacher_schedules.json` - Contains block-wise schedules for all teachers
- `scheduling_report.md` - Detailed report with statistics and analysis

## Implementation Notes

This implementation follows operational research approaches, modeling the scheduling problem as a combination of assignment and transportation problems. The current implementation provides a foundation that can be further refined and optimized.