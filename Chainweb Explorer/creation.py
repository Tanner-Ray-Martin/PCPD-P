import os

def create_kadena_explorer_structure(base_path):
    # Define the folder structure
    structure = {
        "src": {
            "backend": {
                "api": {
                    "__init__.py": "",
                    "routes": {
                        "__init__.py": "",
                        "transactions.py": "",
                        "blocks.py": "",
                        "accounts.py": ""
                    },
                    "schemas": {
                        "__init__.py": "",
                        "transaction_schema.py": "",
                        "block_schema.py": "",
                        "account_schema.py": ""
                    },
                    "main.py": ""
                },
                "db": {
                    "__init__.py": "",
                    "models.py": "",
                    "database.py": "",
                    "crud.py": ""
                },
                "core": {
                    "__init__.py": "",
                    "config.py": "",
                    "dependencies.py": ""
                },
                "tests": {
                    "__init__.py": "",
                    "test_transactions.py": "",
                    "test_blocks.py": "",
                    "test_accounts.py": ""
                }
            },
            "frontend": {
                "pyside": {
                    "__init__.py": "",
                    "main.py": "",
                    "widgets.py": ""
                },
                "streamlit": {
                    "main.py": ""
                },
                "html": {
                    "index.html": ""
                }
            }
        },
        "README.md": ""
    }

    # Function to create files and directories
    def create_files_and_dirs(base_path, structure):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_files_and_dirs(path, content)
            else:
                with open(path, 'w') as f:
                    f.write(content)

    # Create the base path if it doesn't exist
    os.makedirs(base_path, exist_ok=True)
    create_files_and_dirs(base_path, structure)

# Base path for the project
base_path = r'C:\Users\tanner.martin\Desktop\Personal\PCPD-P\Chainweb Explorer'
create_kadena_explorer_structure(base_path)
print(f"Folder structure for Kadena Chainweb Explorer project created in '{base_path}'")
