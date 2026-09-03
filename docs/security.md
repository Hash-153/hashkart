# Security Architecture and Audit Controls

## Security Principles

NovaMart implements defense-in-depth security mechanisms tailored for e-commerce transactions:

1. **Authentication**: Stateless JSON Web Tokens (JWT) using HMAC-SHA256. Access tokens expire in 60 minutes; refresh tokens expire in 7 days.
2. **Password Security**: Passwords hashed using Argon2 / Bcrypt with configurable cost factors. Plaintext passwords are never logged or stored.
3. **Role-Based Authorization (RBAC)**: Endpoint protection enforcing role scopes (`CUSTOMER`, `STAFF`, `ADMIN`).
4. **SQL Injection Prevention**: Exclusive usage of SQLAlchemy ORM parameterized queries. Raw unescaped SQL strings are prohibited.
5. **Cross-Site Scripting (XSS)**: React automatically escapes output variables. API responses set `X-XSS-Protection` and strict `Content-Security-Policy` headers.
6. **Cross-Origin Resource Sharing (CORS)**: Explicit whitelist configuration restricting origins in production environments.
7. **Rate Limiting**: API rate-limiting middleware to mitigate brute-force authentication and denial-of-service attempts.
8. **Sensitive Data Sanitization**: Credit card data is never processed or saved; mock payment simulator accepts synthetic card signatures only. Internal stack traces are suppressed in production mode.
