# Setting Up AWS Amplify for Your App

Now lets start connecting your React app to AWS services. AWS Amplify makes this surprisingly straightforward, but we're going to build it step-by-step so you understand what's happening under the hood.

**Amplify Gen 2** is Amazon's latest approach to full-stack development. Unlike the previous version that used configuration files, Gen 2 uses TypeScript code to define your backend resources. This gives you better type safety, more flexibility, and easier integration with your frontend code.

You could use the quickstart command `npm create amplify@latest` to generate everything automatically, but we're taking the manual approach. This way, you'll understand each piece and have a solid foundation for building more complex applications later.

## Manual Installation of Amplify Gen 2

Let's start by adding Amplify to your existing React project. Make sure you're in your project root directory, then install the necessary packages:

```bash
npm init -y
npm add --save-dev @aws-amplify/backend@latest @aws-amplify/backend-cli@latest typescript
```

**What these packages do:**

- `@aws-amplify/backend` - The core library for defining backend resources
- `@aws-amplify/backend-cli` - Command-line tools for deploying and managing your backend
- `typescript` - Provides type checking and better development experience

## Creating the Backend Structure

Now we'll create the folder structure that Amplify expects. In your root directory, create an `amplify` folder:

```bash
mkdir amplify
cd amplify
```

Inside the `amplify/` folder, we need to create two key files:

**1. `backend.ts` - Your main backend configuration**

```typescript
// amplify/backend.ts
import { defineBackend } from '@aws-amplify/backend';

defineBackend({});
```

This file is where you'll register all your backend resources. Right now it's empty, but we'll add authentication, data, and storage as we build them.

**2. `tsconfig.json` - TypeScript configuration**

```json
{
    "extends": "@aws-amplify/backend/tsconfig"
}
```

This tells TypeScript how to compile your Amplify backend code.

## Understanding Your Project Structure

After these steps, your project should look like this:

```
├── amplify/
│   ├── backend.ts              # Main backend entry point
│   ├── tsconfig.json           # TypeScript config for backend
│   └── package.json            # Backend dependencies
├── src/                        # Your React app code
├── node_modules/               # Installed packages
├── .gitignore
├── package-lock.json
├── package.json                # Frontend dependencies
└── tsconfig.json               # TypeScript config for frontend
```

Amplify Gen 2 separates your frontend and backend code clearly. Your React app lives in `src/`, while your AWS resource definitions live in `amplify/`. This separation makes it easier to manage applications.

The `backend.ts` file acts as the entry point where you'll import and register all your backend resources. As we add authentication, data models, and storage, you'll see how this central configuration makes everything work together.

---

You're now ready to start adding backend functionality. In the next section, we'll add user authentication using AWS Cognito.
