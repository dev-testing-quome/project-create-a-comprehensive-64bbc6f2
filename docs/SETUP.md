# Developer Setup Guide - project-create-a-comprehensive

This guide outlines the setup process for developers working on `project-create-a-comprehensive`, a HIPAA-compliant healthcare patient portal.  We'll use a combination of Python (backend), React (frontend), and PostgreSQL (database).  Docker is the recommended approach for local development.

## Prerequisites

* **Required Software Versions:**
    * Python 3.9+
    * Node.js 16+
    * PostgreSQL 14+
    * Docker Desktop
    * Docker Compose
* **Development Tools:**
    * Git
    * Text Editor/IDE (VS Code recommended)
* **IDE Recommendations and Configurations:**
    * **VS Code:** Install the following extensions:
        * Python
        * ESLint
        * Prettier
        * Docker


## Local Development Setup

### Option 1: Docker Development (Recommended)

1. **Clone Repository:**
   ```bash
   git clone <repository_url>
   cd project-create-a-comprehensive
   ```

2. **Docker Setup:** Ensure Docker and Docker Compose are installed and running.

3. **Development `docker-compose.yml` Configuration:**  This file (located in the project root) will define the services.  A sample structure:

   ```yaml
   version: "3.9"
   services:
     web:
       build: ./frontend
       ports:
         - "3000:3000"
       depends_on:
         - backend
         - db
     backend:
       build: ./backend
       ports:
         - "8000:8000"
       depends_on:
         - db
       environment:
         - DATABASE_URL=postgresql://postgres:password@db:5432/patient_portal
     db:
       image: postgres:14
       environment:
         - POSTGRES_USER=postgres
         - POSTGRES_PASSWORD=password
         - POSTGRES_DB=patient_portal
       ports:
         - "5432:5432"
   ```

4. **Hot Reload Setup:**  For the frontend (React), use a tool like `nodemon` within the `frontend` directory.  For the backend (Python), consider using a development server with automatic reloading (e.g., `uvicorn` with appropriate settings).

### Option 2: Native Development

1. **Backend Setup:**
   ```bash
   cd backend
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Frontend Setup:**
   ```bash
   cd frontend
   npm install
   ```

3. **Database Setup:** Install PostgreSQL locally. Create the `patient_portal` database and user. Configure the connection string (see Environment Configuration).


## Environment Configuration

* **Required Environment Variables:**
    * `DATABASE_URL`: PostgreSQL connection string (e.g., `postgresql://user:password@host:port/database`)
    * `SECRET_KEY`:  A strong, randomly generated secret key for session management (**crucial for security**)
    * `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USERNAME`, `EMAIL_PASSWORD`: Email configuration for automated reminders.
    * `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`: Twilio credentials for SMS reminders.
    * `STRIPE_SECRET_KEY`: Stripe secret key for billing integration (replace with your actual key).

* **Local Development `.env` File Setup:** Create a `.env` file in the project root and add your environment variables.  **Never commit `.env` to version control.**

* **Configuration for Different Environments:** Use environment variables to switch between development, staging, and production configurations.  Consider using a dedicated configuration management system for production.


## Running the Application

1. **Start Commands (Docker):**
   ```bash
   docker-compose up -d --build
   ```
2. **Start Commands (Native):**
    * Backend: `uvicorn main:app --reload` (assuming `main.py` contains the app)
    * Frontend: `npm start`
3. **Access Frontend and Backend:** The frontend will be accessible at `http://localhost:3000` and the backend API at `http://localhost:8000`.
4. **API Documentation Access:** Use a tool like Swagger or generate documentation from your API framework (e.g., OpenAPI specification).


## Development Workflow

* **Git Workflow and Branching Strategy:** Use Gitflow or a similar branching strategy (e.g., feature branches, pull requests).
* **Code Formatting and Linting Setup:** Use Prettier and ESLint for consistent code style. Configure your IDE to automatically format code on save.
* **Testing Procedures:**  Write unit and integration tests (see Testing section).
* **Debugging Setup:** Use your IDE's debugging tools and logging statements.


## Database Management

* **Running Migrations:** Use Alembic or a similar migration tool to manage database schema changes.
* **Seeding Development Data:** Create scripts to populate the database with sample data for development.
* **Database Reset Procedures:**  Create scripts to easily reset the database to a clean state.


## Testing

* **Running Unit Tests:**  `pytest` (Python) or `jest` (JavaScript).  Example (pytest):  `pytest` in the backend directory.
* **Running Integration Tests:**  Use a testing framework to test interactions between different components.
* **Test Coverage Reports:** Generate coverage reports using tools like `pytest-cov`.


## Common Development Tasks

* **Adding New API Endpoints:**  Follow the existing code style and add appropriate tests.
* **Adding New Frontend Components:**  Use React's component model and ensure proper styling and integration.
* **Database Schema Changes:**  Use migrations to manage schema changes.
* **Adding Dependencies:**  Use `pip` (backend) and `npm` (frontend) to manage dependencies.


## Troubleshooting

* **Common Setup Issues:**  Check Docker logs, ensure ports are not in use, and verify environment variables.
* **Port Conflicts Resolution:**  Change ports in `docker-compose.yml` or your local server configurations.
* **Dependency Issues:**  Use a virtual environment (Python) and carefully manage package versions (npm).
* **Environment Variable Problems:**  Double-check the `.env` file and ensure variables are properly set.


## Contributing

* **Code Style Guidelines:**  Follow the style guide (e.g., PEP 8 for Python, Airbnb style guide for JavaScript).
* **Pull Request Process:**  Create clear and concise pull requests with thorough testing.
* **Issue Reporting:**  Use the project's issue tracker to report bugs and feature requests.


Remember to replace placeholders like `<repository_url>` with your actual values.  This guide provides a solid foundation; adapt it as needed for your specific project requirements and technologies.  Always prioritize HIPAA compliance throughout the development process.
