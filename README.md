# Resume Analyzer

A simple web application that analyzes resumes and identifies missing skills based on a selected target role.

## Overview

This project allows users to upload a resume and evaluate how well it matches a specific job role such as Data Science or Web Development. It highlights existing skills, missing skills, and provides a match score.

## Features

* Upload resume (.txt format)
* Select target role
* Identify relevant and missing skills
* Compute a match score
* Clean and interactive interface using Streamlit

## Tech Stack

* Python
* Streamlit

## Project Structure

resume-analyzer/

* app.py
* skills.py
* requirements.txt
* README.md

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   python -m streamlit run app.py

## Future Improvements

* Support PDF resume uploads
* Improve skill extraction using NLP
* Add more job roles
* Deploy as a web application

## Purpose

This project demonstrates basic text analysis, user interaction, and application design using Python.
