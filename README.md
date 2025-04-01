# Todo API

This is a simple Todo API built with Python and FastAPI. Inspired from Roadmap.sh [project](https://roadmap.sh/projects/todo-list-api)

## Features

- Create, read, update, and delete todos.
- Simple and easy-to-use API.

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:itsukuna/todo_api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd todo_api
   ```

3. Install the required packages:

   ```bash
   pipenv install
   ```

## Usage

1. Run the API:

   ```bash
   fastapi dev app
   ```

2. Access the API documentation at:

   ```
   http://127.0.0.1:8000/docs
   ```

## Endpoints

- `POST /todos/`: Create a new todo.
- `GET /todos/`: Get all todos.
- `GET /todos/{todo_id}`: Get a specific todo by ID.
- `PUT /todos/{todo_id}`: Update a todo.
- `DELETE /todos/{todo_id}`: Delete a todo.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License.
