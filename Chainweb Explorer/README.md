# Kadena Chainweb Explorer Project

This project is a Kadena Chainweb Explorer built using SQLAlchemy, Pydantic, FastAPI, PySide6, Streamlit, and HTML. The folder structure is organized to separate the backend and frontend components effectively.

## Folder Structure

### src/backend

1. **api**
   - `__init__.py`: Initialization file for the API package.
   - **routes**
     - `__init__.py`: Initialization file for the routes package.
     - `transactions.py`: API routes related to transactions.
     - `blocks.py`: API routes related to blocks.
     - `accounts.py`: API routes related to accounts.
   - **schemas**
     - `__init__.py`: Initialization file for the schemas package.
     - `transaction_schema.py`: Pydantic schema for transaction data.
     - `block_schema.py`: Pydantic schema for block data.
     - `account_schema.py`: Pydantic schema for account data.
   - `main.py`: Entry point for the FastAPI application.

2. **db**
   - `__init__.py`: Initialization file for the database package.
   - `models.py`: SQLAlchemy models definitions.
   - `database.py`: Database connection setup.
   - `crud.py`: CRUD operations for the models.

3. **core**
   - `__init__.py`: Initialization file for the core package.
   - `config.py`: Configuration settings for the project.
   - `dependencies.py`: Dependency injection for the FastAPI application.

4. **tests**
   - `__init__.py`: Initialization file for the tests package.
   - `test_transactions.py`: Test cases for transactions.
   - `test_blocks.py`: Test cases for blocks.
   - `test_accounts.py`: Test cases for accounts.

### src/frontend

1. **pyside**
   - `__init__.py`: Initialization file for the PySide6 package.
   - `main.py`: Entry point for the PySide6 application.
   - `widgets.py`: Custom widgets for the PySide6 application.

2. **streamlit**
   - `main.py`: Entry point for the Streamlit application.

3. **html**
   - `index.html`: HTML file for the web interface.

## Description

### Backend

- **FastAPI**: The backend API is built using FastAPI. It serves as the main interface for interacting with the Kadena blockchain and retrieving data about transactions, blocks, and accounts.
- **SQLAlchemy**: Used for ORM (Object-Relational Mapping) to manage database models and interactions.
- **Pydantic**: Utilized for data validation and serialization within the FastAPI application.

### Frontend

- **PySide6**: Provides a desktop GUI for interacting with the Kadena Chainweb Explorer.
- **Streamlit**: Offers a web-based interface for the same purpose.
- **HTML**: Basic web page for additional frontend needs.

### Tests

- Contains test cases to ensure the functionality and reliability of the backend components.

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
    git clone https://github.com/yourusername/KadenaChainwebExplorer.git
    ```

2. Navigate to the project directory:
    ```sh
    cd KadenaChainwebExplorer
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

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