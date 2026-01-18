# Configuring Authorization Rules

Understanding how data access permissions and authorization work in Amplify Gen 2.

## What We Configured Earlier

In defining our [Data Schema]() earlier, we set up authorization rules for our Post model:

```typescript
// amplify/data/resource.ts

Post: a.model({
  caption: a.string(),
  email: a.string(),
  userId: a.string(),
  date: a.string(),
  imagePath: a.string()
})
.authorization(allow => [
  allow.authenticated().to(['read']),
  allow.ownerDefinedIn(userId).to(['create', 'update', 'delete'])
])
```
```typescript
export const data = defineData({
  schema,
  authorizationModes: {
    defaultAuthorizationMode: 'userPool',
  }
});
```

## Default Authorization Mode

Setting `defaultAuthorizationMode: 'userPool'` means:

- All API requests require a valid Cognito User Pool token
- Only authenticated users can interact with your data backend
- Amplify automatically handles token validation and user identification

## Model-Level Authorization Rules

The `.authorization()` method defines who can perform which operations:

```typescript
allow.authenticated().to(['read'])
```

This rule means:

- **Who**: Any authenticated user (`allow.authenticated()`)
- **What**: Can read posts (`.to(['read'])`)
- **Result**: All signed-in users can view all posts, but cannot create, update, or delete

## Owner-Defined Authorization

The second rule uses a custom ownership field:

```typescript
allow.ownerDefinedIn(userId).to(['create', 'update', 'delete'])
```

This means:

- **Who**: Users who own the record (determined by the `userId` field)
- **What**: Can create, update, and delete posts
- **How it works**: When a user creates a post, their user ID is stored in the `userId` field, making them the owner
- **Result**: Only the post creator can modify or delete their own posts

## Current Permission Behavior

**What Users CAN Do:**

- Read/view all posts once authenticated
- Create new posts (ownership automatically assigned)
- Update their own posts (owner-based access)
- Delete their own posts (owner-based access)
- Access real-time updates when posts change

**What Users CANNOT Do:**

- Update posts created by other users
- Delete posts created by other users
- Access posts without authentication

## Authorization Rules Reference

Here's a comprehensive table of all available authorization rules in Amplify Gen 2:

| Rule | Description | Use Case | Auth Mode |
|------|-------------|----------|-----------|
| `allow.publicApiKey()` | Grants everyone access | Public content via API key | `apiKey` |
| `allow.authenticated()` | Any signed-in user | Public content for logged-in users | `userPool` / `oidc` / `identityPool` |
| `allow.guest()` | Unauthenticated users | Public content, no login required (via Cognito Identity Pool) | `identityPool` |
| `allow.owner()` | Record owner (uses default `owner` field) | User-specific data with default ownership | `userPool` / `oidc` |
| `allow.ownerDefinedIn(field)` | Custom ownership field | Custom ownership tracking | `userPool` / `oidc` |
| `allow.group('groupName')` | Users in specific Cognito group | Role-based access control | `userPool` / `oidc` |
| `allow.groups(['group1', 'group2'])` | Users in any of the specified groups | Multiple role access | `userPool` / `oidc` |
| `allow.groupsDefinedIn(field)` | Groups defined in a field | Dynamic group membership | `userPool` / `oidc` |
| `allow.custom()` | Custom authorization provider | External auth systems | `lambda` |

## Operations Reference

Available operations for `.to()`:

| Operation | Description |
|-----------|-------------|
| `'create'` | Create new records |
| `'read'` | Read/query existing records |
| `'update'` | Modify existing records |
| `'delete'` | Remove records |

## Learn More

For comprehensive authorization documentation, visit the [AWS Amplify Gen 2 Authorization Guide](https://docs.amplify.aws/gen2/build-a-backend/data/customize-authz/).
