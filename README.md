# PCPD-P Certification Projects Repository

This repository contains three projects aimed at demonstrating proficiency in various aspects of Python development and related technologies. The projects include:

1. **PCPD-P Certification Course Folder Structure**
2. **Dynamic Database Generator**
3. **Kadena Chainweb Explorer**

## Project Overviews

### 1. PCPD-P Certification Course Folder Structure

This project is a structured folder and file setup for the PCPD-P Certification course. It includes all the necessary segments and subsections as per the assessment criteria. Each segment is organized into a separate folder with placeholder Python files.

#### Key Components:
- **Core Concepts**: Fundamental Python concepts and terminologies.
- **Developer Toolkit Proficiency**: Tools and practices for efficient development.
- **Programming Essentials**: Basic programming constructs and operations.
- **Working With Functions and Classes**: Creating and using functions and classes.
- **Debugging and Code Quality**: Techniques for debugging and writing maintainable code.
- **Integration and Deployment**: Managing dependencies and deploying applications.
- **Collaboration and Methodologies**: Agile methodologies and team collaboration skills.
- **Exception Handling**: Handling exceptions in Python.
- **Real-world Application**: Practical capstone projects.
- **Advanced Python Mastery**: Advanced Python techniques and best practices.
- **Software Development Best Practices**: Tools and methodologies for high-quality software development.
- **Deployment and Containerization**: Packaging and deploying applications.
- **Version Control, Collaboration, and Soft Skills**: Version control and collaboration skills.

### 2. Dynamic Database Generator

This project is a dynamic database generator built using SQLAlchemy, Pydantic, FastAPI, PySide6, Streamlit, and HTML. It demonstrates the integration of various technologies to create a flexible and interactive database management system.

#### Key Components:
- **Backend**:
  - **API**: FastAPI application with routes, schemas, and main entry point.
  - **DB**: SQLAlchemy models, database setup, and CRUD operations.
  - **Core**: Configuration and dependency management.
  - **Tests**: Unit tests for backend functionality.
- **Frontend**:
  - **PySide6**: Desktop GUI application.
  - **Streamlit**: Web-based interface.
  - **HTML**: Basic web page.

### 3. Kadena Chainweb Explorer

This project is a Kadena Chainweb Explorer, which interacts with the Kadena blockchain to retrieve and display data about transactions, blocks, and accounts. It uses SQLAlchemy, Pydantic, FastAPI, PySide6, Streamlit, and HTML.

#### Key Components:
- **Backend**:
  - **API**: FastAPI application with routes for transactions, blocks, and accounts, along with corresponding schemas.
  - **DB**: SQLAlchemy models, database setup, and CRUD operations.
  - **Core**: Configuration and dependency management.
  - **Tests**: Unit tests for backend functionality.
- **Frontend**:
  - **PySide6**: Desktop GUI application.
  - **Streamlit**: Web-based interface.
  - **HTML**: Basic web page.

## Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic
- PySide6
- Streamlit

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/PCPD-P-Certification-Projects.git
    ```

2. Navigate to the project directory:
    ```sh
    cd PCPD-P-Certification-Projects
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Projects

### PCPD-P Certification Course Folder Structure
This project primarily serves as a reference and template. Explore the folder structure to understand the organization and contents.

### Dynamic Database Generator

1. Start the FastAPI server:
    ```sh
    uvicorn src.backend.api.main:app --reload
    ```

2. Run the PySide6 application:
    ```sh
    python src/frontend/pyside/main.py
    ```

3. Launch the Streamlit application:
    ```sh
    streamlit run src/frontend/streamlit/main.py
    ```

4. Open `index.html` in a web browser to view the HTML interface.

### Kadena Chainweb Explorer

1. Start the FastAPI server:
    ```sh
    uvicorn src.backend.api.main:app --reload
    ```

2. Run the PySide6 application:
    ```sh
    python src/frontend/pyside/main.py
    ```

3. Launch the Streamlit application:
    ```sh
    streamlit run src/frontend/streamlit/main.py
    ```

4. Open `index.html` in a web browser to view the HTML interface.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

