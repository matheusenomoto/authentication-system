# Authentication System using Facade, Strategy, and Singleton Patterns

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)

This project is a Python implementation of a flexible authentication system. It uses the **Facade**, **Strategy**, and **Singleton** design patterns to provide a clean, scalable, and easy-to-use authentication module.

This system is designed to showcase best practices in software architecture and object-oriented design, making it a great portfolio piece for roles like Solutions Architect or software developer.

## Features

- **Multiple Authentication Methods:** Easily supports different authentication providers.
  - Username & Password (Local)
  - Google Sign-In (Mocked OAuth2)
  - GitHub Sign-In (Mocked OAuth2)
- **Simplified Interface:** The **Facade** pattern hides the complexity of the underlying authentication logic.
- **Extensible:** The **Strategy** pattern makes it simple to add new authentication methods without changing the existing code.
- **Single Point of Control:** The **Singleton** pattern ensures a single, globally accessible instance of the authentication manager.

## Design Patterns Used

- **Strategy:** Defines a family of algorithms (authentication methods) and makes them interchangeable. Each authentication method (`local`, `google`, `github`) is a separate strategy.
- **Facade:** Provides a single, simplified interface (`AuthenticationFacade`) to the more complex subsystem of different authentication strategies.
- **Singleton:** Ensures that the `AuthenticationFacade` has only one instance throughout the application, providing a global point of access.

## Project Structure

```
authentication-system/
├── src/
│   ├── strategies/      # Contains all authentication strategies
│   │   ├── base_strategy.py
│   │   └── ...
│   ├── auth_facade.py   # The Facade and Singleton implementation
│   └── mock_user_db.py  # A mock user database
├── main.py              # Example client code demonstrating usage
└── README.md
```

## How to Run

1.  **Clone the repository:**
    ```sh
    git clone git@github.com:matheusenomoto/authentication-system.git
    cd authentication-system
    ```

2.  **Run the application:**
    This project uses only standard Python libraries, so no installation is required.
    ```sh
    python main.py
    ```

3.  **Expected Output:**
    The script will run through several authentication scenarios (successful and failed) for each strategy and print the results to the console.
    
    ![image](https://github.com/user-attachments/assets/95344b14-e377-4c42-b91a-ee7d2fce5381)


## Potential AWS Integration & Next Steps

This project serves as a strong foundation. For a **Solutions Architect** role, you can discuss how to evolve this into a cloud-native solution on AWS:

- **Amazon Cognito:** Replace the entire mock system. Cognito provides user pools for local users and supports identity federation with Google, GitHub, and other social providers out-of-the-box.
- **AWS Lambda & API Gateway:** The `AuthenticationFacade` logic could be deployed as a serverless AWS Lambda function. An Amazon API Gateway endpoint (`POST /auth`) would trigger the function, making it a scalable microservice.
- **AWS Secrets Manager:** Instead of hardcoding tokens or secrets, store third-party credentials (like Google Client ID/Secret) securely in AWS Secrets Manager.
- **IAM Roles:** Upon successful authentication (especially via Cognito), the system could grant the user temporary, limited-privilege IAM credentials to access other AWS resources (like S3 or DynamoDB) securely.

---

#### **Matheus Enomoto**
- [Blog](https://matheusenomoto.com/)
- [LinkedIn](https://www.linkedin.com/in/matheus-lopes-enomoto/)
