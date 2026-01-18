# Deleting Files from Storage

At this point, we can now view posts with images and also seemingly be able to remove them. But there is a problem, when users delete posts, the post data does gett removed from DynamoDB, but the uploaded images still remain in your S3 bucket. These files consume storage space and increase costs. Let's implement proper file deletion to clean up these resources.

## Using `remove`

Add the `remove` function from Amplify Storage to your existing imports:

```typescript
// src/components/Posts.tsx

import { remove } from 'aws-amplify/storage';
```

Replace your existing `deletePost` function with this enhanced version:

```typescript
// src/components/Posts.tsx

const deletePost = async (id: string, imagePath: string) => {
  try {
    // Delete the image file from S3 if it exists
    if (imagePath) {
      await remove({ 
        path: imagePath 
      });
      console.log("Image deleted from S3:", imagePath);
    }

    // Delete the post from DynamoDB
    const deletedPost = await client.models.Post.delete({
      id,
    });

    console.log("Post deleted:", deletedPost);
  } catch (error) {
    console.error("Error deleting post:", error);
  }
};
```

- Checks if image exists and deletes the file from S3 first
- Then removes the post record from DynamoDB

Modify your delete button to pass both the post ID and image path:

```typescript
// src/components/Posts.tsx

{isAuthor(userId!) &&
  <div className="post-buttons">
    <button onClick={() => editPost(id)}>Edit</button>
    <button onClick={() => imagePath && deletePost(id, imagePath)}>Remove</button>
  </div>
}
```

> We add a guard condition to ensure that the `imagePath` exists before running the function

## Confirm Deletion

Create a post with an image and click the Remove button. Check your console logs to confirm both the S3 file and DynamoDB record are deleted:

```
Image deleted from S3: public/images/user123/photo.jpg
Post deleted: { id: "post123", ... }
```

Or you could simply check the S3 and DynamoDB dashboards and confirm deletion.

---

Now when users delete posts, all associated resources are completely removed from your AWS infrastructure, keeping your storage clean and costs optimized.
