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
* Week 1 Exercise 5 - Basic time-series visualization using `week1_macro_practice.csv`
  * Created line plots for `industrial_production_index` and `pmi` using `plot()`.
  * Interpreted broad upward/downward movements and visible gaps caused by missing values.
  * Compared what graphs show better than summary statistics and what summary statistics show better than graphs.
  * Clarified that exact missing months may require checking the underlying data, not only reading the plot axis.
  * Reviewed in `answers/text/week1/week1_5.txt` and `answers/code/week1/week1_5.ipynb`.
* Week 1 Exercise 6 - Scatter plot relationship check using `week1_macro_practice.csv`
  * Created a scatter plot with `pmi` on the x-axis and `industrial_production_index` on the y-axis.
  * Interpreted that no clear visual relationship was obvious from the scatter plot alone.
  * Corrected the modeling interpretation from "not useful" to "not enough evidence from this plot alone."
  * Noted that missing values can remove points from a scatter plot.
  * Reviewed in `answers/text/week1/week1_6.txt` and `answers/code/week1/week1_6.ipynb`.
* Week 1 Review Check - End-to-end EDA review using `week1_macro_practice.csv`
  * Re-ran the full Week 1 EDA workflow: load data, inspect structure, convert dates, sort chronologically, check missing values, inspect summary statistics, and create line/scatter plots.
  * Explained the difference between date conversion and chronological sorting.
  * Explained that `describe()` count excludes `NaN` values and that averages do not show time order.
  * Identified remaining confusion around choosing target variables and explanatory variables before modeling.
  * Reviewed in `answers/text/week1/week1_review.txt` and `answers/code/week1/week1_review.ipynb`.

## In Progress

* Phase 2 - Machine Learning Foundations
* Target variable and explanatory variable selection
* Baseline modeling concepts

## Weak Areas

* Pandas method interpretation
* Duplicate row concept
* Translating code output into precise written analysis
* Date range interpretation
* Explaining missing value treatment decisions precisely
* Distinguishing summary statistics from causal/economic explanations
* Distinguishing what can be read from a plot from what requires checking the raw data
* Avoiding overstatement when a graph does not show a clear relationship
* Choosing target variables and explanatory variables based on modeling purpose rather than only data cleanliness

## Strong Areas

* Economic Data Understanding
* Data Collection
* Data Source Validation

## Notes

Starting point: Modeling beginner.

Start Date: 2026-07-09

Current Week: 2
Week Status: In Progress

# Diagnostic Scores

Pandas: 7/10
EDA: 6/10
Visualization: 3/10
Missing Value Handling: 3/10
Feature Engineering: 0/10
Model Evaluation: 0/10
Leakage Awareness: 3/10
Time-Series Intuition: 4/10

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

## Plot Interpretation Scope

Mistake: The review initially demanded exact missing months from a graph where the x-axis did not show every month.
Root Cause: The evaluation standard mixed visual interpretation with raw-data verification.
Correction: For basic visualization exercises, distinguish between what is visible from the plot and what requires checking the underlying DataFrame.
Follow-up Exercise: Future graph exercises should ask for broad trend, visible gaps, and uncertainty from the graph first; exact dates should be required only when the task explicitly asks the student to inspect the raw data.

## Scatter Plot Overstatement

Mistake: Initially described PMI as not useful for prediction based mainly on one same-time scatter plot.
Root Cause: Treated a weak visual relationship as enough evidence to reject a variable for modeling.
Correction: A scatter plot can show whether a simple same-time relationship is visually obvious, but it cannot alone prove a variable has no predictive value. Time-series features may work through lags or in combination with other variables.
Follow-up Exercise: Future relationship checks must use cautious language such as "this plot alone does not show clear evidence" instead of "this variable is not useful."

## Target and Explanatory Variable Selection

Mistake: Initially chose a target variable partly because it had no missing values and looked stable.
Root Cause: Treated data cleanliness as the main reason to define a prediction target.
Correction: A target variable should be chosen because it answers the modeling question: "What future value do I want to predict?" Explanatory variables should be chosen because they may provide information available at prediction time.
Follow-up Exercise: Week 2 should begin by explicitly defining target variable, prediction timestamp, available information, and a simple baseline before fitting any model.
