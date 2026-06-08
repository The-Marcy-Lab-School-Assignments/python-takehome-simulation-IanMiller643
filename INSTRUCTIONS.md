# Python Interview Simulation: NYC 311 Service Requests
**Dataset:** NYC 311 Service Requests  
**Part 1 Due:** Monday of Week 2 at 9:00am  
**Part 2 Due:** Monday of Week 3 at 9:00am  

---

## Overview

This is an individual take-home assessment completed in two parts. You will write a single Python script — `analysis.py` — that you will build on across two weeks. Each week you will submit the same folder with your latest version of the script.

Part 1 focuses on basic filtering, counting, and string formatting. Part 2 builds on Part 1 by adding aggregation, sorting, computed values, and formatted tabular output.


This assessment mirrors what you might receive as a take-home technical screen for a software engineering job. You will be evaluated on whether your output matches the expected answers and on whether your code demonstrates clean, readable Python.

**Feeling intimidated?** Rest assured, while the syntax may be new to you, the algorithms and logic needed to complete these tasks are similar to many of the problems that you have already solved using JavaScript: 
- creating frequency counters
- sorting with comparison functions
- string formatting
- finding maximums
- etc...

---

## The Dataset

You have been provided with `nyc_311_requests.csv` — a sample of NYC 311 service requests from January through April 2024.

Here are the first 4 rows in the file:

```csv
request_id,date,borough,complaint_type,agency,resolution_status
1001,2024-01-03,Brooklyn,Noise - Residential,NYPD,Closed
1002,2024-01-04,Manhattan,HEAT/HOT WATER,HPD,Closed
1003,2024-01-04,Queens,Rodent,DOHMH,Closed
```

A `.csv` file is a **comma-separated values file** which is a way to format data in a plaintext table with rows and columns. The very first row is the **header row** which lists the titles of each column. Each subsequent row is an entry in the table with comma-separated values.

As you can see, the file has the following columns:

| Column              | Description                                                   |
| ------------------- | ------------------------------------------------------------- |
| `request_id`        | Unique identifier for each request                            |
| `date`              | Date the request was submitted (YYYY-MM-DD)                   |
| `borough`           | NYC borough where the request originated                      |
| `complaint_type`    | Type of complaint (e.g., Noise - Residential, HEAT/HOT WATER) |
| `agency`            | City agency responsible for handling the request              |
| `resolution_status` | Whether the request is `Open` or `Closed`                     |

Your task will be to parse this CSV file and generate a report about its contents.

---

## What to Submit
 
Submit a folder named `nyc-311-simulation-your-name` containing:
 
1. `nyc_311_requests.csv` — the original dataset
2. `analysis.py` — your Python script
3. `output.txt` — the saved output from running your script
4. `README.md` — completed using the template below
You will submit the same folder twice — once at the end of Week 1 with Part 1 complete, and again at the end of Week 2 with Part 2 added to the same script.

A file called `expected_output.txt` is provided for you and your final `output.txt` file should match it exactly after completing Part 2 to earn full credit.

---
 
## README Template
 
You have been given a `README.md` file with instructions on how to use the script. This is a common convention for take-home assignments like this. The `README.md` file should also include a description and implementation notes which have been left blank. Fill those sections out before submitting. Replace everything in brackets.
 
```markdown
# NYC 311 Service Requests Analysis
 
## How to Run
 
1. Make sure you have Python 3 installed.
2. Navigate to this folder in your terminal.
3. Run the script:
 
python3 analysis.py
 
Output will be saved to `output.txt`. The console will confirm when the file has been written.
 
## What This Script Does
 
[Write 2-3 sentences describing what your script does in plain English.]
 
## Dependencies
 
This script uses only Python's built-in libraries: `csv`.
 
## Notes
 
[Optional: anything you want to flag about your approach or assumptions.]
```
 
---

## Getting Started

In Python, reading and writing to files is a fairly standard process.Copy the following code snippets into your `analysis.py` file to get started. Read each explanation carefully before using them.

### Reading the CSV

To read a CSV file we use the `open` function to load the file contents and then the `csv` package to read the file line by line.

```python
# Import the csv package to access DictReader
import csv

rows = []

with open('filename') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)
```

Each row is a dictionary where the keys are the column headers (`csv.DictReader` knows that the first row is the header row and pulls column headers from it). 

```python
# example of what the first data row looks like
row = {
  'request_id': 1001,
  'date': '2024-01-03',
  'borough': 'Brooklyn',
  'complaint_type': 'Noise - Residential',
  'agency': 'NYPD',
  'resolution_status': 'Closed'
}
```

You can access values like `row['borough']` or `row['complaint_type']`. After this block runs, `rows` is a list of dictionaries — one per row in the CSV.

### Writing to a file

```python
meaning_of_life = 42

with open('output.txt', 'w') as f:
    f.write(f"Meaning of life: {meaning_of_life}\n")

print("Output saved to output.txt")
```

`with open()` ensures the file is closed safely after writing, even if something goes wrong. The `'w'` mode creates the file if it doesn't exist and overwrites it if it does. The `print` statement confirms to you that the script ran successfully.

### Running the Script

To run a python script, use the `python3 <filename>` terminal command:

```sh
python3 analysis.py
```

---
 
## Part 1 Questions
*Due: Monday of Week 2 at 9:00am*
 
Your script must answer all three questions below and write the results to `output.txt`.
 
**Question 1: How many requests are currently open?**
 
Write the result in this exact format:
```
Open requests: 17
```
 
**Question 2: What is the most common complaint type?**
 
Write the result in this exact format:
```
Most common complaint type: Noise - Residential (30 requests)
```
 
**Question 3: How many requests were submitted per borough?**
 
Write each borough and its count, one per line, in alphabetical order by borough name:
```
Requests per borough:
- Bronx: 20
- Brooklyn: 21
- Manhattan: 21
- Queens: 20
- Staten Island: 18
```

**Part 1 Final Output**

The final output should match this exactly (note spacing between answers to each question):

```
Open requests: 17

Most common complaint type: Noise - Residential (30 requests)

Requests per borough:
- Bronx: 20
- Brooklyn: 21
- Manhattan: 21
- Queens: 20
- Staten Island: 18
```

*Notice the blank line between questions*

**Part 1 Requirements**
 
Your script must:
 
- Read the CSV using Python's built-in `csv` module and `with open()`
- Use a `for` loop to iterate over the rows
- Use a dictionary to count values
- Use f-strings for all formatted output
- Use `with open()` to write all output to `output.txt`
- Print `Output saved to output.txt` to the console when the script finishes
- Produce output that matches the format above exactly, including spacing and capitalization
---

### Grading Checklist — Part 1
*Used for the Week 2 grading pass*
 
**Output (6 points):**

- [ ] Q1 output matches expected answer exactly
- [ ] Q2 output matches expected answer exactly, including complaint type name and count
- [ ] Q3 output lists all five boroughs
- [ ] Q3 boroughs are in alphabetical order
- [ ] Q3 counts are correct for all boroughs
- [ ] All output is saved to `output.txt`

**Code Quality (6 points):**

- [ ] Uses `csv` module to read the file (not `open()` + manual string splitting)
- [ ] Uses a `for` loop to iterate over rows
- [ ] Uses a dictionary to store and count values where appropriates
- [ ] Uses f-strings for formatted output
- [ ] Uses `with open()` for file writing and prints `Output saved to output.txt` on completion
- [ ] README is complete and describes what the script does in plain English

**Part 1 Total: 12 points**
 
---

 
## Part 2 Questions
*Due: Monday of Week 3 at 9:00am*
 
Add the following four questions to your existing script. Your final `output.txt` should contain the answers to all seven questions — Part 1 and Part 2 together.
 
**Question 4: How many requests were submitted for each complaint type?**
 
Write the results sorted by count from highest to lowest:
```
Requests by complaint type:
- Noise - Residential: 30
- HEAT/HOT WATER: 29
- Rodent: 23
- Illegal Parking: 18
```
 
**Question 5: Which borough has the most open requests?**
 
Write the result in this exact format:
```
Borough with most open requests: Brooklyn (5 open)
```
 
**Question 6: What is the closure rate for each borough?**
 
The closure rate is the percentage of a borough's requests that are closed. For example, Brooklyn has 21 total requests, 16 of which are closed. This means that Brooklyn's closure rate is 76.2% (16/21).

Write each borough's closure rate as a percentage, sorted alphabetically. Percentages must be rounded to one decimal place:

```
Closure rate by borough:
- Bronx: 80.0%
- Brooklyn: 76.2%
- Manhattan: 85.7%
- Queens: 90.0%
- Staten Island: 83.3%
```
 
**Question 7: What are the top 3 boroughs by total number of requests?**
 
Write the result as a numbered list. When boroughs are tied, list them alphabetically:
```
Top 3 boroughs by total requests:
1. Brooklyn (21 requests)
2. Manhattan (21 requests)
3. Bronx (20 requests)
```

**Part 2 Final Output**

The final output should match this exactly (note spacing between answers to each question):

```
Open requests: 17

Most common complaint type: Noise - Residential (30 requests)

Requests per borough:
- Bronx: 20
- Brooklyn: 21
- Manhattan: 21
- Queens: 20
- Staten Island: 18

Requests by complaint type:
- Noise - Residential: 30
- HEAT/HOT WATER: 29
- Rodent: 23
- Illegal Parking: 18

Borough with most open requests: Brooklyn (5 open)

Closure rate by borough:
- Bronx: 80.0%
- Brooklyn: 76.2%
- Manhattan: 85.7%
- Queens: 90.0%
- Staten Island: 83.3%

Top 3 boroughs by total requests:
1. Brooklyn (21 requests)
2. Manhattan (21 requests)
3. Bronx (20 requests)
```
 
**Part 2 Requirements**
 
In addition to the Part 1 requirements, your script must:
 
- Use dictionaries to aggregate values by group
- Compute a derived value (closure rate as a percentage)
- Sort results programmatically (do not hardcode the order)
---
 
### Grading Checklist — Part 2
*Used for the Week 3 grading pass*
 
**Output (9 points):**

- [ ] Q4 lists all four complaint types with correct counts
- [ ] Q4 results are sorted highest to lowest
- [ ] Q5 identifies Brooklyn as the correct borough with the correct count
- [ ] Q6 lists all five boroughs with correct closure rates
- [ ] Q6 boroughs are in alphabetical order
- [ ] Q6 percentages are rounded to one decimal place
- [ ] Q7 lists the correct top 3 boroughs with correct counts
- [ ] Q7 tied boroughs (Brooklyn and Manhattan) are listed alphabetically
- [ ] All output from both Part 1 and Part 2 is saved to `output.txt`

**Code Quality (6 points):**

- [ ] Uses dictionaries to aggregate values by group
- [ ] Computes closure rate as a derived value (not hardcoded)
- [ ] Uses `sorted()` programmatically rather than hardcoding order
- [ ] Uses f-strings for formatted output
- [ ] Part 1 code quality requirements are still met in the final submission
- [ ] README is updated to reflect the full script

**Part 2 Total: 15 points**