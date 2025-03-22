print("Script started")
import pandas as pd
import json
import os
from collections import defaultdict

def read_excel_data(file_path):
    print(f"Reading Excel file: {file_path}")
    try:
        excel_file = pd.ExcelFile(file_path)
        sheet_names = excel_file.sheet_names
        print(f"Found sheets: {sheet_names}")
        data = {}
        for sheet in sheet_names:
            df = pd.read_excel(excel_file, sheet_name=sheet)
            print(f"DataFrame for sheet '{sheet}':")
            print(f"  Shape: {df.shape}")
            print(f"  Head:\n{df.head()}")
            data[sheet] = df
        return data
    except Exception as e:
        print(f"Error reading Excel file: {str(e)}")
        return None

def clean_dataframe(df):
    df = df.dropna(how='all').dropna(axis=1, how='all').reset_index(drop=True)
    return df

def clean_column_names(df):
    df.columns = [str(col).strip().replace(' ', '_').replace('\n', '_').lower() for col in df.columns]
    return df

def clean_and_process_data(data):
    return {sheet: clean_column_names(clean_dataframe(df)) for sheet, df in data.items()}

def dataframe_to_dict(df):
    records = df.to_dict(orient='records')
    for record in records:
        for key, value in list(record.items()):
            if pd.isna(value):
                record[key] = None
    return records

def convert_to_json(processed_data):
    return {sheet: dataframe_to_dict(df) for sheet, df in processed_data.items()}

def validate_data(json_data):
    results = {"errors": [], "warnings": [], "insights": []}
    lecturer_data = json_data.get("Lecturer Details", [])
    rooms_data = json_data.get("Rooms data", [])
    courses_data = json_data.get("Course list", [])
    requests_data = json_data.get("Student requests", [])
    print(f"Length of lecturer_data: {len(lecturer_data)}")
    print(f"Length of rooms_data: {len(rooms_data)}")
    print(f"Length of courses_data: {len(courses_data)}")
    print(f"Length of requests_data: {len(requests_data)}")
    time_blocks = ["1A", "1B", "2A", "2B", "3", "4A", "4B"]
    results["insights"].append(f"Available time blocks: {time_blocks}")
    teacher_blocks = defaultdict(dict)
    course_enrollments = defaultdict(int)
    student_blocks = defaultdict(lambda: defaultdict(list))
    
    if courses_data:
        for course in courses_data:
            lecturer_id = course.get("lecturer_id")
            for block in time_blocks:
                if course.get(block.lower()) in ["Yes", 1]:
                    if lecturer_id and block in teacher_blocks[lecturer_id]:
                        results["errors"].append(f"Teacher conflict: Lecturer {lecturer_id} assigned to multiple courses in block {block}")
                    else:
                        teacher_blocks[lecturer_id][block] = course.get("course_name")
    
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
                capacity, enrollment = room_capacities[room_number], course_enrollments.get(course_name, 0)
                if enrollment > capacity:
                    results["warnings"].append(f"Room capacity issue: Course '{course_name}' has {enrollment} requests but room {room_number} has capacity {capacity}")
    
    if requests_data:
        for request in requests_data:
            student_id = request.get("student_id")
            for priority in ["required", "requested", "recommended"]:
                course_name = request.get(priority)
                if course_name and courses_data:
                    for course in courses_data:
                        if course.get("course_name") == course_name:
                            for block in time_blocks:
                                if course.get(block.lower()) in ["Yes", 1]:
                                    if student_id in student_blocks and block in student_blocks[student_id]:
                                        results["errors"].append(f"Student conflict: Student {student_id} requests multiple courses in block {block}")
                                    else:
                                        student_blocks[student_id][block].append(course_name)
    
    if courses_data:
        results["insights"].append(f"Total number of courses: {len(courses_data)}")
    if lecturer_data:
        results["insights"].append(f"Total number of lecturers: {len(lecturer_data)}")
    if rooms_data:
        results["insights"].append(f"Total number of rooms: {len(rooms_data)}")
        results["insights"].append(f"Total room capacity: {sum(room.get('capacity', 0) for room in rooms_data if room.get('capacity'))}")
    if requests_data:
        results["insights"].append(f"Total number of student requests: {len(requests_data)}")
        priority_counts = defaultdict(int)
        for request in requests_data:
            for priority in ["required", "requested", "recommended"]:
                if request.get(priority):
                    priority_counts[priority] += 1
        for priority, count in priority_counts.items():
            results["insights"].append(f"Number of {priority} course requests: {count}")
    
    return results

def main():
    file_path = "dataset.xlsx"
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
    data = read_excel_data(file_path)
    if not data:
        print("Failed to read Excel data.")
        return
    processed_data = clean_and_process_data(data)
    json_data = convert_to_json(processed_data)
    with open("processed_data.json", "w") as json_file:
        json.dump(json_data, json_file, indent=2)
    print("Processed data saved to 'processed_data.json'")
    validation_results = validate_data(json_data)
    with open("validation_results.json", "w") as json_file:
        json.dump(validation_results, json_file, indent=2)
    print("Validation results saved to 'validation_results.json'")
    print("\nValidation Results:")
    print("\nErrors:")
    for error in validation_results["errors"]:
        print(f"- {error}")
    print("\nWarnings:")
    for warning in validation_results["warnings"]:
        print(f"- {warning}")
    print("\nInsights:")
    for insight in validation_results["insights"]:
        print(f"- {insight}")

if __name__ == "__main__":
    main()