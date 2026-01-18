# Setting Up Your Data Backend

Time to add a database and API to your application. With [Amplify Data](../workshop-elements.md#aws-amplify-gen-2), you'll get a secure, real-time GraphQL API backed by DynamoDB which all generated automatically from your data model definition.

**Amplify Data** is a service that creates a complete backend data layer from a simple schema definition. When you define your data model, Amplify automatically creates:

- A [GraphQL](../workshop-elements.md#graphql) API with [AWS AppSync](../workshop-elements.md#aws-appsync)
- [DynamoDB](../workshop-elements.md#amazon-dynamodb) tables for data storage
- Real-time subscriptions for live updates
- Authentication and authorization rules
- Type-safe client code for your frontend

![Amplify Data architecture showing schema to infrastructure mapping](images/amplify-data-architecture.png)

## Creating Your Data Model

Let's define a data model for our posts. Create a new directory and file: `amplify/data/resource.ts`

```bash
mkdir amplify/data
cd amplify/data
```

Now create the data resource file:

```typescript
// amplify/data/resource.ts
import { a, defineData, type ClientSchema } from '@aws-amplify/backend';

// Define our data schema
const schema = a.schema({
  Post: a.model({
    caption: a.string(),
    email: a.string(),
    userId: a.string(),
    date: a.string(),
    imagePath: a.string()
  })
    .authorization(allow => [
      allow.authenticated().to(['read']),
    ])
});

// Create the data resource
export const data = defineData({
  schema,
  authorizationModes: {
    defaultAuthorizationMode: 'userPool',
  }
});

// Export types for frontend use
export type Schema = ClientSchema<typeof schema>;
```

## Understanding the Schema Definition

```typescript
// Define our data schema
const schema = a.schema({
  Post: a.model({
    caption: a.string(),
    email: a.string(),
    userId: a.string(),
    date: a.string(),
    imagePath: a.string()
  })
    .authorization(allow => [
      allow.authenticated().to(['read']),
    ])
});
```

**The Post Model**

We're defining a `Post` model with five fields:

- `caption` - The post caption
- `email` - The author's email address
- `userId` - The unique ID of the user who created the post
- `date` - When the post was created
- `imagePath` - S3 Path to its source image

**Authorization Rules**

The `.authorization()` method defines who can access this data:

```typescript
// Authorization example
.authorization(allow => [
  allow.authenticated().to(['read']),
])
```

The rule above means to allow `authenticated` (logged-in) users to read posts.

See [Amplify Data Auth Rules](https://docs.amplify.aws/react/build-a-backend/data/customize-authz/) for more authorization rules.

**Data Configuration**

```typescript
// Create the data resource
export const data = defineData({
  schema,
  authorizationModes: {
    defaultAuthorizationMode: 'userPool',
  }
});

```

The `defineData()` function creates your backend configuration:

- `schema` is the data model you defined earlier (`Post`)
- `defaultAuthorizationMode: 'userPool'` means Cognito User Pool tokens will be used for authorization

**TypeScript Types**

```typescript
// Export types for frontend use
export type Schema = ClientSchema<typeof schema>;
```


The `ClientSchema` generates TypeScript types for your frontend code. This gives you autocomplete and type checking when working with your data. Completely optional, but it will boost your development experience (DX).

## Registering Data with Your Backend

Now add the data resource to your backend configuration. Update `backend.ts`:

```typescript
// amplify/backend.ts
import { defineBackend } from '@aws-amplify/backend';
import { auth } from './auth/resource';
import { data } from './data/resource';

defineBackend({
  auth,
  data,
});
```

## Deploying Your Data Backend

Your sandbox should still be running from the previous section. If not, start it again:

```bash
npx ampx sandbox
```

Amplify will detect the new data resource and deploy it automatically. You'll see output indicating that AppSync and DynamoDB resources are being created.

**What gets created in AWS:**

- An AppSync GraphQL API with automatically generated queries, mutations, and subscriptions
- A DynamoDB table to store your Post data
- IAM roles and policies for secure access
- Real-time subscription endpoints for live updates

Once deployment completes, your `amplify_outputs.json` file will be updated with the new API configuration.

## Understanding What You Built

With just a few lines of code, you now have:

**A complete GraphQL API** with operations like 

- `read`
- `write` 
- `update`
- `delete`
- `subscribe`

**A scalable database** that automatically handles:

- Data storage and retrieval
- Indexing for fast queries
- Backup and recovery
- Scaling based on demand

**Security built-in** with:

- Authentication required for all operations
- User-based access controls
- Encrypted data in transit and at rest

In the next sections, we'll connect your React frontend to this API and build the user interface for creating, reading, updating, and deleting posts.

