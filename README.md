# DA_LLM_API

DA_LLM_API is a project that processes user queries on two datasets using SQL and integrates the Gemini LLM through an API key to enhance query handling capabilities.

## Description

This project involves:

- **Datasets**: Two datasets stored in SQLite.
- **Operations**: Perform operations based on user queries.
- **Integration**: Gemini LLM integrated via an API key for advanced query processing.

## Features

- Query processing using SQL on SQLite datasets.
- Integration with Gemini LLM for enhanced query handling.
- Simple and efficient API for user interaction.

## Getting Started

### Prerequisites

- Python above 3.x
- Gemini LLM API Key
- IDE

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Saksham-3175/DA_LLM_API.git
    cd DA_LLM_API
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Gemini LLM API Key:
    - Obtain an API key from Gemini LLM.
    - Set it as an environment variable:
      ```bash
      export GEMINI_API_KEY='your_api_key_here'
      ```

### Usage

1. Open the folder in an IDE.
2. Open a new terminal
3. Run the below code in the terminal:
    ```bash
    streamlit run src/app.py
    ```
4. Interact with the chatbot to perform queries on the datasets.
   
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Gemini LLM team for providing the API.
  
---
