Project Writeup: Article CMS Deployment
1. Resource Justification

I have analyzed the hosting options for the Article CMS and selected Azure App Service as the optimal deployment solution.

Analysis of Hosting Options 

    Cost: Azure App Service provides a cost-effective PaaS model, reducing overhead by eliminating the need to manage a full OS for a single Python application.

    Scalability: App Service allows for seamless horizontal and vertical scaling through the Azure Portal, whereas a VM would require manual setup of Scale Sets.

    Availability: Azure provides built-in high availability and automated patching for App Service, ensuring the app remains online without manual intervention.

    Workflow: The deployment workflow is highly efficient using the Deployment Center with GitHub Actions integration, compared to the manual configuration required for a VM.

Final Choice & Justification 

I chose Azure App Service because it allows for a focus on application development rather than server maintenance. It specifically simplified the process of troubleshooting SQL connectivity and Blob storage integration through integrated features like the Log Stream.

Potential Changes to Decision 

I would change my decision to an Azure Virtual Machine (VM) if the application required full administrative access to the Operating System or the installation of custom third-party software not supported by the App Service Linux environment.
2. Deployment & Connectivity

The Python web application is successfully deployed to Azure and maintains connectivity with all required storage solutions.

    Azure SQL Database: The app is connected to the cms database on server cms-server-12. It successfully stores article data (title, author, body) and user credentials.

    Azure Blob Storage: The app is connected to the Storage Account cmsimages1. Images are successfully uploaded to a blob container and rendered in the application.

    Technical Implementation: Connectivity was ensured by implementing proper URL encoding for database credentials and setting the WEBSITES_CONTAINER_START_TIME_LIMIT to allow for driver initialization.

3. Security & Monitoring

The application meets all Udacity security and monitoring standards.

    Microsoft Authentication: A functioning "Sign in with Microsoft" option is implemented using the msal library. The Redirect URIs are configured to point to the /getAToken endpoint of the deployed app.

    Logging: The application uses the logging library in __init__.py to capture both successful and unsuccessful access attempts.

    Log Evidence: As seen in the provided screenshots, successful login attempts and database handshakes are logged as INFO, while incorrect password attempts are captured as WARNING or ERROR messages.

4. Final Evidence Checklist 

The following screenshots are included in the screenshots/ directory of this submission:

    Resource Group: Showing all services (Storage, SQL, App Service) in one list.

    SQL Tables: Query Editor view confirming the posts and users tables exist.

    Storage Properties: Showing the Blob service endpoint URL.

    App Registration: Showing configured Redirect URIs for Microsoft login.

    Running Application: Detail view of the "Hello World!" article by Jane Doe with image and URL visible.

    Operational Logs: Capture containing at least one successful and one unsuccessful access attempt.