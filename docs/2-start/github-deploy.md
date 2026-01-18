# Deploying our Frontend with AWS Amplify Hosting

Now that we have created our React application, it’s time to make it accessible on the internet! Using AWS Amplify, we can connect our project to a GitHub repository and deploy it in just a few steps.

You don’t need to manually configure servers and hosting. Amplify handles all the cloud infrastructure for you. This means your app can be live globally with just minimal setup.

## Steps to Deploy

1. **Go to the AWS Amplify Console**  

      Open the [Amplify Console](https://console.aws.amazon.com/amplify/).
      ![Image 1](images/deploy_1.jpg)

2. **Click "Create App" or "Deploy an App"**  

      You'll find this option on the homepage of the Amplify dashboard.
      ![Image 2](images/deploy_2.jpg)

3. **Select GitHub as your Git provider**  

      Amplify supports GitHub, GitLab, Bitbucket, and CodeCommit.
      ![Image 3](images/deploy_3.jpg)

4. **Authorize Amplify to access your GitHub account**  

      This is a one-time GitHub App authorization.
      ![Image 4](images/deploy_4.jpg)

5. **Select your repository**  

      Pick the repo containing your React app from the list.

6. **Choose the branch to deploy**  

      Usually `main` or `master`, depending on your project.

7. **(Optional) Configure app settings**  
   
      You can customize build settings or just click **Next** to skip.

8. **Review settings and click "Save and Deploy"**  
   
      Amplify will start the deployment process.

9. **Wait for the build to complete**  
   
      After a few minutes, your app will be live on an Amplify-hosted URL

---

With just a few clicks, you have successfuly deployed your frontend app on the internet. From here, any future updates you push to your GitHub branch will automatically trigger a new deployment, keeping your app live and up-to-date!

This demonstrates the power and simplicity of Amplify, letting you focus on building features instead of worrying about servers, hosting, or CI/CD pipelines.
