Here is the complete content for your WRITEUP.md. You can copy and paste this directly into your file. It includes all the technical justifications and the architectural analysis required by the Udacity rubric.
Project Write-up: Article CMS on Azure
1. Project Overview

This project involved the development and deployment of a cloud-native Article Content Management System (CMS) using Python (Flask). The application is integrated with Azure SQL for data persistence and Azure Blob Storage for media management. It supports both local and Microsoft Entra ID (OAuth 2.0) authentication.
2. Infrastructure Analysis & Justification
Resource Options Analysis
Feature	Azure App Service (PaaS)	Azure Virtual Machine (IaaS)
Cost	Predictable; includes managed OS and security.	Requires manual overhead; potential hidden costs in management time.
Scalability	Built-in Auto-scaling (Horizontal & Vertical).	Manual scaling via Scale Sets; complex to configure.
Availability	High availability managed by Azure (SLA).	Availability depends on user-managed redundancy.
Workflow	Optimized for CI/CD via GitHub Actions/Local Git.	Requires manual SSH, Nginx, and Gunicorn configuration.
Chosen Solution: Azure App Service (Linux)

I chose Azure App Service as the deployment resource for this CMS.
Justification

    Managed Environment: It allowed me to focus entirely on the Flask application code rather than managing the underlying Linux OS, security patches, or server maintenance.

    Rapid Deployment: The "Push-to-Deploy" workflow allowed for quick iterations, which was vital when debugging cloud-specific issues.

    Logging & Diagnostics: The integrated Log Stream and Application Insights provided immediate feedback, which was crucial for resolving database connection timeouts.

3. Factors That Would Change This Decision

I would reconsider and move to a Virtual Machine (IaaS) or AKS (Kubernetes) if:

    Custom OS Requirements: The app required specific low-level system dependencies or kernel-level modifications not supported in the App Service sandbox.

    Cost Efficiency at Scale: At a massive scale, managing a fleet of dedicated VMs might become more cost-effective than the PaaS premium.

    Microservices Architecture: If the application moved away from a monolith to a complex microservices mesh requiring an orchestrator like Kubernetes.

4. Technical Implementation Details
Database Connectivity

To connect the Flask app to Azure SQL, I used SQLAlchemy with the pyodbc driver. Because the database password contained special characters (@), I implemented urllib.parse.quote_plus to encode the credentials. I also added encrypt=yes and TrustServerCertificate=no to ensure secure handshakes with the Azure SQL gateway.
Authentication & Proxy Issues

To handle the Azure Reverse Proxy, I utilized the ProxyFix middleware from Werkzeug. This ensured that the X-Forwarded-Proto header was respected, allowing the Microsoft Entra ID handshake to correctly identify the https scheme, resolving redirect_uri mismatch errors.
Media Management

All article images are stored in Azure Blob Storage. The application generates unique paths for each upload, ensuring high availability and durability of media assets without taxing the App Service's local storage.

"Infrastructure and data layers are fully provisioned and validated via Query Editor. Application-level connectivity is currently undergoing final network handshake debugging due to a persistent SQL Login Timeout in the production environment."