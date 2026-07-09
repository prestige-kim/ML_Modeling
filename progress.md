# Progress Tracking

## Current Phase

Phase 1 - Data Analysis Foundations

## Completed

* Week 1 Exercise 1 - Basic dataset inspection using `week1_macro_practice.csv`
  * Checked shape, columns, dtypes, missing values, duplicate rows, date column, and row meaning.
  * Reviewed in `answers/text/week1_1.txt` and `answers/code/week1_1.ipynb`.
* Week 1 Exercise 2 - Date conversion and chronological sorting using `week1_macro_practice.csv`
  * Converted `date` from string to datetime.
  * Sorted by date in ascending order and checked chronological order.
  * Reviewed in `answers/text/week1_2.txt` and `answers/code/week1_2.ipynb`.

## In Progress

* Pandas
* Data Exploration

## Weak Areas

* Pandas method interpretation
* Duplicate row concept
* Translating code output into precise written analysis
* Date range interpretation

## Strong Areas

* Economic Data Understanding
* Data Collection
* Data Source Validation

## Notes

Starting point: Modeling beginner.

Start Date: 2026-07-09

Current Week: 1
Week Status: In Progress

# Diagnostic Scores

Pandas: 3/10
EDA: 1/10
Visualization: 0/10
Missing Value Handling: 1/10
Feature Engineering: 0/10
Model Evaluation: 0/10
Leakage Awareness: 0/10
Time-Series Intuition: 2/10

# Weakness Log

## Duplicate Row Concept

Mistake: Initially treated repeated values or columns as possible duplicates.
Root Cause: Did not distinguish repeated values from duplicated rows.
Correction: A duplicated row means one row's full set of column values is identical to another row's full set of column values.
Follow-up Exercise: Continue checking duplicate rows in future datasets and explain whether repeated economic values are normal or true duplicate observations.

## Pandas Output Interpretation

Mistake: Code output was initially not fully translated into precise written findings.
Root Cause: Focused on running methods before interpreting their outputs.
Correction: For every inspection method, write what the output means in plain language.
Follow-up Exercise: Next exercise must include a short written interpretation for `shape`, `dtypes`, missing values, and date handling.

## Date Range Interpretation

Mistake: Initially reversed the earliest and latest dates, and described a 2021-01 to 2024-12 range as about 3 years.
Root Cause: Calendar range and time-axis language were interpreted loosely.
Correction: Earliest date means the oldest point in time; latest date means the most recent point in time. 2021-01 through 2024-12 is about 4 years of monthly data.
Follow-up Exercise: Future time-series exercises must state earliest date, latest date, frequency, and approximate coverage period.
