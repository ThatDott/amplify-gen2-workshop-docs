# Key Differences Between Amplify Gen 1 and Gen 2

AWS Amplify Gen 2 introduces a **code-first** approach to building full-stack applications, improving speed, developer experience (DX), and workflow efficiency compared to Amplify Gen 1.

---

## Core Comparison

| Feature                          | Amplify Gen 1                                         | Amplify Gen 2                                                   |
|----------------------------------|--------------------------------------------------------|------------------------------------------------------------------|
| **Infrastructure Setup**        | CLI or Amplify Studio                                  | TypeScript files (e.g., `resource.ts`)                          |
| **Developer Experience**        | Manual provisioning                                    | IDE-friendly with IntelliSense and type safety                 |
| **Local Development**           | Shared environments                                    | Isolated sandboxes per developer (faster, safer iterations)     |
| **Environment Management**      | Manual CLI/console setup                               | Git branch = environment (zero-config setup)                   |
| **Frontend Type Integration**   | Requires codegen for types                             | Auto-generated types for real-time data binding                 |
| **Workflow Integration**        | Backend-focused                                        | Fullstack-first: backend, hosting, auth, UI all unified         |
| **API & DB Definition**         | JSON-based GraphQL schema                              | TypeScript-based schema with live code integration              |
| **Authentication**             | AWS Cognito with CLI setup                             | Cognito via TS config with extendable user flows                |
| **Custom AWS Services**         | Limited/extensible via CLI                             | Built on AWS CDK — fully modular and extensible                 |
| **Management Console**          | Basic deployment and hosting                           | Unified view of builds, hosting, env vars, users, data          |

---

## Key Amplify Gen 2 Features

- **Code-first** full-stack development
- **Real-time API & NoSQL DB** auto-generated from data schema
- **Git-based environments** (e.g., `main`, `dev`, `feature/*`)
- **Instant preview deploys** from pull requests
- **Cognito Auth** with simple custom user flows
- **AWS CDK foundation** for modular extension (e.g., S3, Lambda, Location)

---

We can now proceed with the **actual workshop using Amplify Gen 2**, where we’ll walk through creating a real-time API, setting up authentication, and deploying your fullstack app from scratch.

