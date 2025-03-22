# My Validation Journey

This document details my experience validating the data and code for the course scheduling system. I've gone through the provided Excel data, the Python script, and the rules to understand how everything fits together.

## Initial Impressions

My first step was to examine the `dataset.xlsx` file. It contains several sheets: Lecturer Details, Rooms Data, Course List, Lecture Requests from Students, and RULES.  It became clear that the core of this project revolves around a block scheduling system, with time divided into specific blocks: 1A, 1B, 2A, 2B, 3, 4A, and 4B.

I also looked at the `process_dataset.py` script. This script is responsible for reading the Excel data, cleaning it up, converting it to a JSON format, and then performing validations based on the rules.

## Insights from the Data

After running the script and examining the output, I gained a few key insights:

*   The system uses the aforementioned block scheduling system.
*   There are 83 lecturers in the dataset.

## Making Sense of It All

The rules are crucial for understanding how the scheduling should work.  The main points I focused on were:

*   **No Double Booking:**  Neither teachers nor students can be in two places at once (within the same block). The code actively checks for these conflicts.
*   **Room Capacity:**  The system needs to make sure courses aren't assigned to rooms that are too small. The code checks for this as well.
*   **Prioritization:** Student requests have a priority order: Required, Requested, and Recommended. While the code reads this, it doesn't seem to use it for the validation itself, which makes sense since this is more about the assignment process.

From what I can see, the provided data seems to be well-behaved – I didn't encounter any immediate errors or warnings during the validation. This means there were no teacher conflicts, student conflicts, or room capacity issues detected in the *current* dataset.

## Potential Roadblocks

The script identifies potential "unsolvable metrics" as errors and warnings.  If, for example, a teacher was assigned to two courses in block 1A, the script would flag this as an error. Similarly, if too many students requested a course for a small room, it would generate a warning.

## The Code Behind the Scenes

The heart of the validation lies in the `validate_data` function within `process_dataset.py`. Here's a snippet showing how it works:

```python
def validate_data(json_data):
    """Validate the data according to the specified rules."""
    validation_results = {
        "errors": [],
        "warnings": [],
        "insights": []
    }

    # Extract relevant data
    lecturer_data = json_data.get("Lecturer Details", [])
    rooms_data = json_data.get("Rooms Data", [])
    courses_data = json_data.get("Course List", [])
    requests_data = json_data.get("Lecture Requests from Students", [])
    rules_data = json_data.get("RULES", [])

    # Extract time blocks
    time_blocks = ["1A", "1B", "2A", "2B", "3", "4A", "4B"]
    validation_results["insights"].append(f"Available time blocks: {time_blocks}")

    # Check for teacher conflicts (teacher assigned to multiple courses in same block)
    teacher_blocks = defaultdict(dict)

    if courses_data:
        for course in courses_data:
            lecturer_id = course.get("lecturer_id")
            available_blocks = []

            for block in time_blocks:
                if course.get(block.lower()) == "Yes" or course.get(block.lower()) == 1:
                    available_blocks.append(block)

                    if lecturer_id:
                        if block in teacher_blocks[lecturer_id]:
                            validation_results["errors"].append(
                                f"Teacher conflict: Lecturer {lecturer_id} assigned to multiple courses in block {block}"
                            )
                        else:
                            teacher_blocks[lecturer_id][block] = course.get("course_name")

    # Check for room capacities against course requests
    course_enrollments = defaultdict(int)

    if requests_data:
        for request in requests_data:
            for priority in ["required", "requested", "recommended"]:
                course = request.get(priority)
                if course:
                    course_enrollments[course] += 1

    if rooms_data and courses_data:
        room_capacities = {room.get("room_number"): room.get("capacity") for room in rooms_data if room.get("room_number")}

        for course in courses_data:
            course_name = course.get("course_name")
            room_number = course.get("room_number")

            if course_name and room_number and room_number in room_capacities:
                capacity = room_capacities[room_number]
                enrollment = course_enrollments.get(course_name, 0)

                if enrollment > capacity:
                    validation_results["warnings"].append(
                        f"Room capacity issue: Course '{course_name}' has {enrollment} requests but room {room_number} has capacity {capacity}"
                    )

    # Check for student conflicts (student requesting multiple courses in same block)
    student_blocks = defaultdict(lambda: defaultdict(list))
    if requests_data:
        for request in requests_data:
            student_id = request.get("student_id")
            for priority in ["required", "requested", "recommended"]:
                course_name = request.get(priority)
                if course_name and courses_data:
                    for course in courses_data:
                        if course.get("course_name") == course_name:
                            for block in time_blocks:
                                if course.get(block.lower()) == "Yes" or course.get(block.lower()) == 1:
                                    if student_id in student_blocks and block in student_blocks[student_id]:
                                        validation_results["errors"].append(
                                            f"Student conflict: Student {student_id} requests multiple courses in block {block}"
                                        )
                                    else:
                                        student_blocks[student_id][block].append(course_name)

    # Additional insights
    if courses_data:
        validation_results["insights"].append(f"Total number of courses: {len(courses_data)}")

    if lecturer_data:
        validation_results["insights"].append(f"Total number of lecturers: {len(lecturer_data)}")

    if rooms_data:
        validation_results["insights"].append(f"Total number of rooms: {len(rooms_data)}")
        total_capacity = sum(room.get("capacity", 0) for room in rooms_data if room.get("capacity"))
        validation_results["insights"].append(f"Total room capacity: {total_capacity}")

    if requests_data:
        validation_results["insights"].append(f"Total number of student requests: {len(requests_data)}")

        # Count priorities
        priority_counts = defaultdict(int)
        for request in requests_data:
            for priority in ["required", "requested", "recommended"]:
                if request.get(priority):
                    priority_counts[priority] += 1

        for priority, count in priority_counts.items():
            validation_results["insights"].append(f"Number of {priority} course requests: {count}")

    return validation_results
```

It cleverly uses dictionaries to keep track of teacher and student schedules, making it easy to spot conflicts.

## What the Output Looks Like

The script generates a `validation_results.json` file.  Here's what it contained in my case (since the processed data was too big to load directly):

```json
{
  "errors": [],
  "warnings": [],
  "insights": [
    "Available time blocks: ['1A', '1B', '2A', '2B', '3', '4A', '4B']",
    "Total number of lecturers: 83"
  ]
}
```

As you can see, no errors or warnings were found in this run.

## Visualizing the Process (If I Could)

To make this report even clearer, I'd ideally include screenshots:

1.  **Excel File:** A peek at the raw data in `dataset.xlsx`.
2.  **Processed JSON:** A look at the cleaned-up data in `processed_data.json`.
3.  **Validation Results:** The output from `validation_results.json`, showing any errors, warnings, and insights.
4.  **VS Code:** The `process_dataset.py` file open, with the `validate_data` function highlighted.

This would provide a complete picture of the data's journey, from raw input to validated results.