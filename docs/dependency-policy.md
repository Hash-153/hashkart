# Dependency and Licensing Policy

## Policy Statement

NovaMart maintains a strict policy regarding third-party software dependencies:
1. **Zero GPL Dependencies**: No dependencies licensed under GPL v1/v2/v3, AGPL v3, or LGPL with incompatible linking provisions may be introduced into the backend, frontend, infrastructure, or utility codebases.
2. **Permissive Licensing**: All dependencies MUST use permissive open-source licenses such as MIT, Apache 2.0, BSD-2-Clause, BSD-3-Clause, ISC, or PSF (Python Software Foundation).
3. **No External Secrets**: All dependencies must function fully in local environments without requiring proprietary third-party API keys or remote cloud services.

---

## Approved Dependency Registry

### Backend Dependencies (Python)

| Package | Version Range | License | Description / Purpose |
| :--- | :--- | :--- | :--- |
| **FastAPI** | ^0.110.0 | MIT | Asynchronous web framework |
| **Uvicorn** | ^0.28.0 | BSD-3-Clause | ASGI server implementation |
| **SQLAlchemy** | ^2.0.28 | MIT | Relational database ORM |
| **Asyncpg** | ^0.29.0 | Apache-2.0 | Asynchronous PostgreSQL driver |
| **Pydantic** | ^2.6.4 | MIT | Data validation and settings management |
| **Pydantic-Settings** | ^2.2.1 | MIT | Application configuration provider |
| **Passlib** | ^1.7.4 | BSD-3-Clause | Password hashing abstraction (Argon2 / Bcrypt) |
| **Bcrypt** | ^4.1.2 | Apache-2.0 | Bcrypt hashing backend |
| **PyJWT** | ^2.8.0 | MIT | JSON Web Token encoding and decoding |
| **Python-Multipart** | ^0.0.9 | Apache-2.0 | Form data parsing middleware |
| **Pytest** | ^8.1.1 | MIT | Automated testing framework |
| **Pytest-Asyncio** | ^0.23.5 | Apache-2.0 | Asyncio support for pytest |
| **Httpx** | ^0.27.0 | BSD-3-Clause | Async HTTP client for backend integration testing |
| **Aiosqlite** | ^0.20.0 | MIT | Async SQLite driver for fast local testing |

### Frontend Dependencies (TypeScript / React)

| Package | Version Range | License | Description / Purpose |
| :--- | :--- | :--- | :--- |
| **React** | ^18.2.0 | MIT | User interface library |
| **React-DOM** | ^18.2.0 | MIT | React rendering engine for DOM |
| **React-Router-DOM** | ^6.22.3 | MIT | Client-side application router |
| **Lucide-React** | ^0.359.0 | MIT | Modern UI icons |
| **Vite** | ^5.1.6 | MIT | Frontend build tool and dev server |
| **TypeScript** | ^5.4.2 | Apache-2.0 | Typed JavaScript superset compiler |

---

## Verification & Audit Procedure

Before adding any new dependency:
1. Query package license metadata on PyPI / npm repository.
2. Confirm license type is MIT, Apache 2.0, BSD, ISC, or PSF.
3. Record the package name, version, license type, and purpose in this file.
