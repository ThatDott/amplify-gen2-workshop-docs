# Workshop Elements

## Core Concepts

### AWS Amplify Gen 2
AWS Amplify Gen 2 is Amazon's latest full-stack development platform that uses a code-first approach. Unlike Gen 1's CLI-driven configuration, Gen 2 lets you define your entire backend using TypeScript, providing better type safety, version control, and developer experience.

### React
React is a JavaScript library for building user interfaces, developed by Facebook. It uses a component-based architecture where you build encapsulated components that manage their own state, then compose them to make complex UIs. React uses a virtual DOM for efficient updates and supports modern JavaScript features.

### TypeScript
TypeScript is a programming language developed by Microsoft that builds on JavaScript by adding static type definitions. It helps catch errors during development, provides better IDE support with autocomplete and refactoring, and makes code more maintainable in large applications.

### Authentication & Authorization
- **Amazon Cognito User Pools**: Managed user directory service that handles user registration, authentication, and account recovery
- **Multi-Factor Authentication (MFA)**: Additional security layer requiring users to provide two or more verification factors
- **Role-based access control**: Security approach that restricts system access based on user roles

### GraphQL
GraphQL is a query language and runtime for APIs that allows clients to request exactly the data they need. Unlike REST APIs that return fixed data structures, GraphQL lets you specify which fields you want, reducing over-fetching and under-fetching of data. It also supports real-time subscriptions for live updates.

### AWS AppSync
AWS AppSync is Amazon's managed GraphQL service that automatically scales your API and provides real-time subscriptions, offline support, and conflict resolution. It connects to various data sources like DynamoDB, Lambda, and HTTP endpoints.

### Amazon DynamoDB
DynamoDB is Amazon's fully managed NoSQL database service designed for applications that need consistent, single-digit millisecond latency at any scale. It automatically scales up and down based on demand and handles all database administration tasks.

### Amazon S3
Amazon Simple Storage Service (S3) is object storage built to store and retrieve any amount of data from anywhere. It's designed for durability and provides industry-leading scalability, data availability, security, and performance.

### Amazon Cognito
Amazon Cognito provides authentication, authorization, and user management for web and mobile apps. It supports user sign-up, sign-in, and access control, and can scale to millions of users while integrating with social identity providers.

### Data Management
- **CRUD operations**: Create, Read, Update, Delete => the four basic operations for persistent storage
- **Data relationships and modeling**: How data entities relate to each other in your application

### File Storage
- **Secure file upload/download**: Protected file operations that respect user permissions
- **Access control and permissions**: Rules that determine who can access which files

### Deployment & CI/CD
- **GitHub integration**: Connecting your code repository to deployment services
- **Automatic deployments**: Code changes automatically trigger new deployments
- **Environment management**: Separate configurations for development, staging, and production
- **Build and deployment pipelines**: Automated processes that test, build, and deploy your code

## Technical Stack

- **Frontend**: React 18 + TypeScript
- **State Management**: React hooks and context
- **Styling**: Modern CSS and responsive design
- **Backend**: AWS Amplify Gen 2
- **Database**: Amazon DynamoDB
- **Authentication**: Amazon Cognito
- **Storage**: Amazon S3
- **API**: AWS AppSync (GraphQL)
- **Hosting**: AWS Amplify Hosting
