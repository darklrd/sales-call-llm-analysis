# Sales Call LLM Analysis Tool

## Overview

The Sales Call LLM Analysis Tool is designed to automate the processing and analysis of sales call data. It efficiently handles various aspects of sales call management including downloading audio, converting it to text, correcting transcripts, and analyzing the content for actionable insights. The tool is built with the integration of Large Language Models (LLMs) to aid in understanding and improving sales strategies through transcript analysis.

## Features

- Automated downloading and conversion of sales call audio to text
- Advanced correction algorithms for transcript refinement
- Translation of non-English transcripts into English
- Deep analysis of transcripts to identify performance metrics, key topics, and sentiment

## Installation

Before you begin the installation, ensure that you have Python 3.x installed on your system.

1. **Clone the repository**:

    ```bash
    git clone https://github.com/darklrd/sales-call-llm-analysis.git
    cd sales-call-llm-analysis
    ```

2. **Set up the environment**:

    It is recommended to set up a virtual environment for the project:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:

    With the virtual environment activated, install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. **Environment variables**:

    Copy the `.env.template` to a new file named `.env` and fill in the required API keys and project-specific settings.

## Usage

To run the Sales Call LLM Analysis Tool, execute the main script:

```bash
python3 main.py
```

The main.py script is the entry point of the application and orchestrates the complete process flow. 

## Configuration

The `prompts.json` file contains the templates for various operations like translation prompts, correction prompts, and analysis prompts. Modify this file to change the behavior of the LLM responses.