### CallLogs-Extraction-using-LLM

The Call Logs Extraction project is structured to process and display information based on user-submitted questions and documents. The flow and functions of the project can be outlined as follows:

1. **Web Interface (`index.html`)**:
  - The web interface provides a form where users can submit a question and a list of document URLs, one per line. There is also an "auto-approve suggestions" checkbox.
  - Upon form submission, a POST request is sent to the `/submit_documents` route with the question, document URLs, and the auto-approve status.
  - The interface also includes a section for displaying questions and answers, where the information is updated dynamically based on the processing status.

2. **Flask Application (`app.py`)**:
  - `index()`: This function serves the main page of the web application, rendering the `index.html` template.
  - `submit_documents()`: Handles form submissions from the web interface. It reads the question and document URLs from the form, initiates the processing of the documents, and updates a global `processing_status` dictionary that tracks the processing state, including any errors, extracted facts, and facts that have been removed since the last submission.
  - If "auto-approve suggestions" is checked, the function immediately processes the URLs using the `extract_facts()` function from `document_processor.py`, updates the `processing_status` with the extracted facts, and marks the processing status as "done".
  - If "auto-approve suggestions" is not checked, the processing status is set to "pending", indicating manual approval may be required.
  - `get_question_and_facts()`: This route provides a JSON response with the current processing status, including the question, processing state, facts extracted by day, any removed facts, and errors. This information is used to update the web interface dynamically.

3. **Document Processing (`document_processor.py`)**:
  - `get_vectorstore_from_url(url)`: Fetches and processes the content of the provided URL to create a vector store, which represents the document content used for further analysis and fact extraction.
  - `extract_facts(question, document_url)`: This function extracts facts relevant to the user's question from the document at the provided URL. It involves several steps:
    - Extracting the date from the document URL.
    - Creating a vector store for the document.
    - Using a series of Langchain components (like `WebBaseLoader`, `RecursiveCharacterTextSplitter`, `Chroma`, `ChatOpenAI`, etc.) to process the document content, generate queries based on the user's question, and retrieve relevant information.
    - Organizing the extracted information by date and returning it for display.

#### Overall Flow:
1.	The user accesses the web interface, inputs a question and document URLs, and submits the form.
2.	The Flask application receives the submission, starts processing the documents, and updates the processing status.
3.	As documents are processed, the Flask application extracts facts related to the question from each document.
4.	The web interface periodically fetches updates from the Flask application and displays the current question, extracted facts, and any processing errors or status messages.

This setup allows for interactive document processing with user input, providing a dynamic way to extract and display information based on submitted questions and documents.

