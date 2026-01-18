# Prerequisites

Before we start building, let's make sure you have everything set up. Don't worry if you're missing something, we'll walk through each installation step.

**What you'll need:**

- Node.js v18 or higher
- An AWS account
- A GitHub account
- A code editor (we recommend Visual Studio Code)
- A Multi-factor Authenticator app like Google Authenticator

## Installing Node.js v18+

Node.js is a JavaScript runtime that lets you run JavaScript outside of web browsers. We need it because modern web development tools (including Amplify) are built with JavaScript and run on Node.js.

The easiest way to install Node.js is through your operating system's package manager. You can find installation instructions for your specific OS at [nodejs.org/download/](https://nodejs.org/en/download/current).

Once installed, verify everything works by opening your terminal and running:

```bash
# Terminal
node -v
npm -v
```

You should see version numbers like `v18.x.x` and `9.x.x`. If you get "command not found" errors, the installation didn't complete properly.

## Setting Up Your AWS Account

Your AWS account is your gateway to all Amazon Web Services. It's where you'll manage your cloud resources, monitor usage, and handle billing. Think of it as your personal slice of Amazon's massive cloud infrastructure.

*[Image placeholder: AWS Console dashboard screenshot]*

If you don't have an AWS account yet, head to [AWS Account Creation Guide](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html) and follow the setup process. You'll need your billing information, but don't worry, we'll stay within the free tier limits during this workshop.

## Creating Your GitHub Account

GitHub is where we'll store our code and set up automatic deployments. When you push code changes to GitHub, Amplify can automatically rebuild and redeploy your application. This is called Continuous Integration/Continuous Deployment (CI/CD).

If you don't have a GitHub account:

1. Go to [github.com](https://github.com)
2. Click "Sign up"
3. Follow the registration process

## Setting Up Your Code Editor

We recommend Visual Studio because it has excellent support for TypeScript, React, and AWS development. Download it from [visualstudio.microsoft.com](https://visualstudio.microsoft.com/downloads/).

**Helpful VS Code Extensions:**

Once you have VS Code installed, consider adding these extensions for a better development experience:

- AWS Toolkit
- TypeScript and JavaScript Language Features
- ES7+ React/Redux/React-Native snippets

That's it for setup! With these tools installed, you're ready to start building with Amplify.
