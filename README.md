# FastAPI GDG OCAPU Workshop Project

This project is a FastAPI-based web application that demonstrates various API concepts and includes a budget management system. The project is structured into two main components: a basic API demonstration and a budget management system.

## Project Structure

```
.
├── src/
│   ├── basic/           # Basic API demonstration
│   │   └── main.py      # Core API endpoints
│   └── budget/          # Budget management system
│       ├── main.py      # Budget API endpoints
│       ├── schema.py    # Data models and schemas
│       ├── utils.py     # Utility functions
│       └── transactions.py # Transaction management
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Features

### Basic API (src/basic)
- Root endpoint with welcome message
- Path parameter examples
- Query parameter examples
- Request body handling with Pydantic models
- Header-based authentication
- Order management system with CRUD operations

### Budget Management System (src/budget)
- Transaction management (CRUD operations)
- Account balance tracking
- Multiple account types support
- Overall balance calculation
- Transaction history

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi-gdgocapu-workshop
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv gdgoc-env
source gdgoc-env/bin/activate  # On Windows: gdgoc-env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the basic API:
```bash
uvicorn src.basic.main:app --reload
```

To run the budget management system:
```bash
uvicorn src.budget.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## Dependencies

Key dependencies include:
- FastAPI: Modern web framework for building APIs
- Pydantic: Data validation and settings management
- Uvicorn: ASGI server implementation
- Python-dotenv: Environment variable management
- Other utility packages for enhanced functionality

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.