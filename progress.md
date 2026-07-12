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
* Week 1 Exercise 3 - Missing value analysis using `week1_macro_practice.csv`
  * Identified columns and dates with missing values.
  * Used `loc` with `isna().any(axis=1)` to inspect rows containing missing values.
  * Explained why missing values should not be deleted or filled before understanding column meaning and analysis purpose.
  * Reviewed in `answers/text/week1/week1_3.txt` and `answers/code/week1/week1_3.ipynb`.
* Week 1 Exercise 4 - Summary statistics interpretation using `week1_macro_practice.csv`
  * Used `describe()`, `mean()`, `min()`, and `max()` to inspect numeric summaries.
  * Interpreted `count`, `mean`, `min`, `max`, and `std` as modeling-preparation checks.
  * Noted that `describe()` count excludes `NaN` values.
  * Reviewed in `answers/text/week1/week1_4.txt` and `answers/code/week1/week1_4.ipynb`.

## In Progress

* Pandas
* Data Exploration

## Weak Areas

* Pandas method interpretation
* Duplicate row concept
* Translating code output into precise written analysis
* Date range interpretation
* Explaining missing value treatment decisions precisely
* Distinguishing summary statistics from causal/economic explanations

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

Pandas: 5/10
EDA: 3/10
Visualization: 0/10
Missing Value Handling: 3/10
Feature Engineering: 0/10
Model Evaluation: 0/10
Leakage Awareness: 1/10
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

## Missing Value Treatment Reasoning

Mistake: Initially explained missing values as something to handle later all at once, rather than as a decision based on column meaning and analysis purpose.
Root Cause: Treated missing value handling as a mechanical cleaning step.
Correction: Missing value treatment depends on whether the missing column is a target candidate, explanatory variable candidate, or reference indicator. In time-series data, filling missing values with future information can create data leakage.
Follow-up Exercise: Future missing value exercises must explain why each missing value should be inspected before using `dropna()` or `fillna()`.

## Summary Statistics Scope

Mistake: Initially treated summary statistics as requiring deeper economic interpretation than needed for the current bootcamp phase.
Root Cause: The exercise scope was too broad and risked turning basic EDA into domain-heavy macro interpretation.
Correction: At this stage, summary statistics are used to inspect ranges, counts, missingness effects, and rough variability before modeling. They do not need to explain economic causes yet.
Follow-up Exercise: Future summary-statistics exercises should separate "what the summary shows" from "why the economy behaved that way."
