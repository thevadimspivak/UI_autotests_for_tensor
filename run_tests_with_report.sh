#!/usr/bin/env bash
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
pytest ./tests --html=./reports/report_$DATE.html