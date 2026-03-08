# container-sec-tool
Container Security Automation Tool
Overview

This tool helps developers scan Dockerfiles or Docker images for common security issues and automatically apply safe remediations where possible. It provides a clear, developer-friendly interface and produces readable reports of findings and fixes.


### Usage Examples

# Scan Dockerfile
python3 cli.py --dockerfile ./sample_dockerfile/origin/Dockerfile

# Scan and remediate
python3 cli.py --dockerfile ./sample_dockerfile/origin/Dockerfile --remediate

# Dry-run (show fixes without applying)
python3 cli.py --dockerfile ./sample_dockerfile/origin/Dockerfile --remediate --dry-run

# Save report as JSON
python3 cli.py --dockerfile ./sample_dockerfile/origin/Dockerfile --json-report report.json

Features

Scan Dockerfiles or Docker images for security issues

Detect running as root user

Detect use of ADD instead of COPY

Detect exposed privileged ports in images

Automatically remediate common issues

Replace ADD with COPY

Change USER root to a non-root user

Command-line interface (CLI) for easy usage

Generates readable reports with issues, severity, and suggested fixes

Installation
git clone <repository_url>
cd container-sec-tool
pip install -r requirements.txt
Usage
Scan a Dockerfile
python cli.py --dockerfile Dockerfile
Scan and remediate a Dockerfile
python cli.py --dockerfile Dockerfile --remediate
Scan a Docker image
python cli.py --image nginx:latest
Output

Displays a table of detected security issues, severity, and suggested fixes

Saves a remediated Dockerfile (if --remediate is used)

Example Report
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Issue                  ┃ Severity ┃ Fix                        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Running as root user    │ High     │ Specify a non-root USER    │
│ Using ADD instead of COPY │ Low   │ Replace ADD with COPY      │
└────────────────────────┴──────────┴────────────────────────────┘
Notes

This tool is intended as a demonstration for container security automation workflows.

It covers basic, common issues; extending to CVE scanning or CI/CD integration is possible.
