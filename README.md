# AWS Amplify Gen 2 Workshop

A comprehensive hands-on workshop for building full-stack applications with AWS Amplify Gen 2, covering authentication, data management, file storage, and deployment.

## 🎯 What You'll Build

By the end of this workshop, you'll have created a complete blog application featuring:

- **User Authentication** - Secure registration and login with AWS Cognito
- **Real-time Data** - GraphQL API with live updates across all users
- **File Storage** - Image uploads with user-specific access controls
- **Production Deployment** - Live application accessible via public URL

## 📚 Workshop Structure

### Introduction (20-30 min)
- Why AWS is the Solution
- Overview of AWS Amplify
- Gen 1 vs Gen 2 Differences

### Getting Started (45-60 min)
- Prerequisites and Setup
- Create React Application
- GitHub Integration and Deployment

### Core Implementation (3-4 hours)
- **Authentication** - User management with Cognito and MFA
- **Data & API** - GraphQL schema, CRUD operations, and permissions
- **Storage** - File uploads, image display, and downloads
- **Deployment** - Production hosting and custom domains

### Wrap-up (15-30 min)
- Application Review
- Resource Cleanup
- Next Steps

## ⏱️ Time Requirements

- **Total Duration:** 4-6 hours
- **Beginner Developers:** 5-6 hours
- **Experienced Developers:** 3.5-4.5 hours
- **Self-Paced Learning:** 2-3 sessions of 2 hours each

## 🛠️ Prerequisites

### Required Software
- **Node.js v18+** - JavaScript runtime for development tools
- **Git** - Version control for code management
- **Code Editor** - VS Code recommended with AWS extensions

### Required Accounts
- **AWS Account** - Free tier eligible for workshop resources
- **GitHub Account** - For code repository and deployment integration

### Recommended Knowledge
- Basic JavaScript/TypeScript familiarity
- React fundamentals (components, hooks, state)
- Command line interface basics

## 🚀 Quick Start

1. **Clone the workshop materials:**
   ```bash
   git clone https://github.com/your-username/amplify-gen2-workshop-docs.git
   cd amplify-gen2-workshop-docs
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the documentation server:**
   ```bash
   mkdocs serve
   ```

4. **Open your browser:**
   Navigate to `http://localhost:8000` to begin the workshop

## 📖 Documentation

The workshop documentation is built with MkDocs and includes:

- Step-by-step instructions with code examples
- Architecture diagrams and explanations
- Troubleshooting guides and best practices
- Links to additional AWS resources

### Local Development

To run the documentation locally:

```bash
# Install MkDocs
pip install mkdocs mkdocs-material

# Serve documentation
mkdocs serve

# Build static site
mkdocs build
```

## 🏗️ Workshop Architecture

The application you'll build uses modern serverless architecture:

```
Frontend (React + TypeScript)
    ↓
AWS Amplify Hosting (CloudFront CDN)
    ↓
AWS AppSync (GraphQL API)
    ↓
┌─────────────────┬─────────────────┬─────────────────┐
│   Amazon        │    Amazon       │    Amazon       │
│   Cognito       │    DynamoDB     │    S3           │
│ (Authentication)│   (Database)    │ (File Storage)  │
└─────────────────┴─────────────────┴─────────────────┘
```

## 🎓 Learning Outcomes

After completing this workshop, you'll understand:

- **Modern Cloud Development** - Serverless architecture patterns and benefits
- **AWS Amplify Gen 2** - Code-first approach to full-stack development
- **Authentication Systems** - User management with multi-factor authentication
- **GraphQL APIs** - Real-time data synchronization and type-safe operations
- **File Storage** - Secure upload/download with user permissions
- **Production Deployment** - CI/CD pipelines and global content delivery

## 💰 Cost Considerations

This workshop uses AWS Free Tier eligible services:

- **AWS Amplify Hosting** - 1,000 build minutes/month free
- **Amazon Cognito** - 50,000 MAUs free
- **AWS AppSync** - 250,000 queries/month free
- **Amazon DynamoDB** - 25GB storage free
- **Amazon S3** - 5GB storage free

**Estimated workshop cost:** $0-5 USD (depending on usage)

## 🧹 Cleanup

**Important:** Follow the cleanup instructions in the final workshop section to avoid ongoing charges. The workshop includes automated cleanup scripts for easy resource removal.

## 🤝 Contributing

We welcome contributions to improve the workshop:

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

### Areas for Contribution
- Additional exercises and challenges
- Improved explanations and diagrams
- Bug fixes and typo corrections
- Translation to other languages

## 📞 Support

- **Workshop Issues** - Open an issue in this repository
- **AWS Amplify Documentation** - [docs.amplify.aws](https://docs.amplify.aws)
- **AWS Support** - Use your AWS support plan for account-specific issues

## 📄 License

This workshop is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 🏷️ Tags

`aws` `amplify` `serverless` `react` `typescript` `graphql` `workshop` `tutorial` `full-stack` `cloud-computing`

---

**Ready to build modern cloud applications?** Start with the [Prerequisites](docs/2-start/prereq.md) section and begin your AWS Amplify journey!
