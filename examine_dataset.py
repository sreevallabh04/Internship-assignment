import pandas as pd
import json

# Read the Excel file
print("Reading dataset.xlsx...")
excel_file = pd.ExcelFile("dataset.xlsx")
sheet_names = excel_file.sheet_names
print(f"Found sheets: {sheet_names}")

# Examine Room data
print("\n=== EXAMINING ROOM DATA ===")
rooms_df = pd.read_excel(excel_file, sheet_name="Rooms data")
rooms_df = rooms_df.dropna(how='all').dropna(axis=1, how='all').reset_index(drop=True)
print(f"Rooms dataframe shape: {rooms_df.shape}")
print(f"Rooms columns: {rooms_df.columns.tolist()}")
print("\nFirst 5 rooms:")
print(rooms_df.head())

# Check for capacity column and calculate total capacity
if 'Capacity' in rooms_df.columns:
    total_capacity = rooms_df['Capacity'].sum()
    print(f"\nTotal room capacity: {total_capacity}")
else:
    capacity_cols = [col for col in rooms_df.columns if 'capacity' in str(col).lower()]
    if capacity_cols:
        print(f"\nPossible capacity column(s): {capacity_cols}")
        print(f"Sum of {capacity_cols[0]}: {rooms_df[capacity_cols[0]].sum()}")
    else:
        print("\nNo capacity column found in room data")

# Check for progress on Milestone 2
print("\n=== CHECKING FOR MILESTONE 2 PROGRESS ===")
try:
    with open("processed_data.json", "r") as f:
        print("processed_data.json exists (Milestone 1 completed)")
except FileNotFoundError:
    print("processed_data.json not found (Milestone 1 incomplete)")

# Look for scheduling-related files
scheduling_files = ['schedule.py', 'scheduler.py', 'scheduling.py']
found_files = []
for file in scheduling_files:
    try:
        with open(file, "r") as f:
            found_files.append(file)
    except FileNotFoundError:
        pass

if found_files:
    print(f"Found scheduling-related files: {found_files}")
else:
    print("No scheduling-related files found (Milestone 2 appears incomplete)")

print("\nScript completed.")