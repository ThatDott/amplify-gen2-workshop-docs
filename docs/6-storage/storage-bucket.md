# Adding File Storage with Amplify

Now let's add file storage to your application so users can upload images with their posts. We'll use [Amazon S3](../workshop-elements.md#amazon-s3) through [Amplify Storage](../workshop-elements.md#file-storage), which handles all the complexity of secure file uploads and downloads.

**Amazon S3 (Simple Storage Service)** is an object storage for the internet. Think of it as a massive, secure file system in the cloud where you can store any type of file: images, documents, videos, or any other data. It handles durability, availability, and can scale to store unlimited amounts of data.

**Amplify Storage** is a service that makes it easy to add file storage to your applications using S3. It handles authentication, authorization, and provides simple APIs for uploading and downloading files. You don't need to worry about S3 bucket policies, IAM roles, or security configurations as Amplify handles all of that.

## Creating Your Storage Resource

Let's set up file storage for your application. 

Navigate to `amplify/` and create a new directory:

```bash
mkdir storage
cd storage
```

Create a `resource.ts` for storage:

```typescript
// amplify/storage/resource.ts

import { defineStorage } from '@aws-amplify/backend';

export const storage = defineStorage({
  name: 'myBucket'
});
```

Now register the storage resource in your backend. Update `backend.ts`:

```typescript
// amplify/backend.ts

import { defineBackend } from '@aws-amplify/backend';
import { auth } from './auth/resource';
import { data } from './data/resource';
import { storage } from './storage/resource';

defineBackend({
  auth,
  data,
  storage,
});
```

## Configuring Storage Access Rules

Now let's define who can access what files. Update your `amplify/storage/resource.ts`:

```typescript
// amplify/storage/resource.ts

import { defineStorage } from '@aws-amplify/backend';

export const storage = defineStorage({
  name: 'myBucket',
  access: (allow) => ({
    'post-pictures/{entity_id}/*': [
      allow.authenticated.to(['read']),
      allow.entity('identity').to(['write', 'delete']),
    ]
  })
});
```

**File path structure:** `'post-pictures/{entity_id}/*'`

- `post-pictures/` - Base directory for all post images
- `{entity_id}` - Dynamic placeholder that becomes each user's unique Cognito Identity ID
- `/*` - Matches any file in that user's directory

**Authorization rule:** 

`allow.authenticated.to(['read'])`
`allow.entity('identity').to(['write', 'delete'])`

- `authenticated` - All authenticated users
- `entity('identity')` - Only the identity owner (the user who uploaded the file)
- `read` - Download and view files
- `write` - Upload new files and overwrite existing ones
- `delete` - Remove files from storage

So this means everyone can access any files in `post-pictures/` but only owners can create or delete files in their folders.

**How user isolation works:**

When a user uploads a file, `{entity_id}` automatically becomes their unique Cognito Identity ID. This means each user gets their own private folder:

```
myBucket/
├── post-pictures/
│   ├── us-east-1:12345678-1234-1234-1234-123456789012/  # User 1's files
│   │   ├── 1640995200000-photo1.jpg
│   │   └── 1640995300000-photo2.png
│   └── us-east-1:87654321-4321-4321-4321-210987654321/  # User 2's files
│       ├── 1640995400000-image1.gif
│       └── 1640995500000-image2.jpg
```

## Deploying Your Storage Backend

Your sandbox should automatically detect the new storage resource and deploy it. If you need to restart it:

```bash
npx ampx sandbox
```

**What gets created in AWS:**

- A secure S3 bucket with your specified name
- IAM policies that enforce your access rules
- Integration with Cognito Identity Pool for user authentication
- Automatic path resolution that maps user sessions to storage directories

## Security Features Built-In

Amplify Storage automatically provides several security features:

**User Isolation:** Each user can only access files in their own directory. Even if they know another user's file path, they can't access it without proper authentication.

**Automatic Authentication:** All storage operations require valid Cognito tokens. Unauthenticated users can't access any files.

**Path-Based Security:** S3 bucket policies automatically enforce directory restrictions based on the user's identity.

**Identity Mapping:** Amplify automatically maps user login sessions to their storage paths, so you don't need to manage user directories manually.

Your file storage backend is now ready! In the next section, we'll add the frontend code to let users upload images with their posts and display them in the application.

