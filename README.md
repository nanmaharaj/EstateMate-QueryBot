# EstateMate-QueryBot

# Conversational Data Retrieval on Real Estate Database

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Conclusion](#conclusion)

## Introduction
This project is an end-to-end conversational real estate database retrieval system that leverages [Streamlit](https://streamlit.io/) for the user interface, [Google Palm LLM](https://ai.google/research/pubs/pub49564) for natural language understanding, and the [Langchain](https://github.com/hwchase17/langchain) framework for managing conversational flow. The system interacts with a MySQL database to provide dynamic Q&A, using few-shot learning and [Hugging Face embeddings](https://huggingface.co/sentence-transformers) stored in [ChromaDB](https://github.com/chroma-core/chroma) to enhance query accuracy and relevance.

## Installation
To set up this project, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/nanmaharaj/EstateMate-QueryBot.git
    cd conversational-real-estate-retrieval
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the database:**
    - Ensure you have a MySQL database set up with your real estate data.
    - You can import data using the [provided SQL file](https://github.com/nanmaharaj/EstateMate-QueryBot/blob/main/miniproject_db.sql).

## Usage
1. **Start the Streamlit UI:**
    ```bash
    streamlit run main.py
    ```

2. **Enter your query in English:** Use the Streamlit interface to enter your real estate-related queries.

## Results
The conversational system successfully retrieves and responds to queries about real estate data with high accuracy. Key features include:
- Natural language understanding powered by [Google Palm LLM](https://ai.google/research/pubs/pub49564).
- Conversational management using [Langchain](https://github.com/hwchase17/langchain).
- Enhanced query accuracy with few-shot learning and [Hugging Face embeddings](https://huggingface.co/sentence-transformers).

## Conclusion
This project demonstrates the integration of advanced AI technologies to create a dynamic and interactive real estate query system. The combination of [Google Palm LLM](https://ai.google/research/pubs/pub49564), [Langchain](https://github.com/hwchase17/langchain), and [Hugging Face embeddings](https://huggingface.co/sentence-transformers) offers a robust solution for conversational data retrieval.
