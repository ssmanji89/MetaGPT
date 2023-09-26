# Step 1: Ensure that NPM is installed on your system. Then install mermaid-js. (If you don't have npm in your computer, please go to the Node.js offical website to install Node.js https://nodejs.org/ and then you will have npm tool in your computer.)
npm --version
sudo npm install -g @mermaid-js/mermaid-cli

# Step 2: Ensure that Python 3.9+ is installed on your system. You can check this by using:
python --version

# Step 3: Clone the repository to your local machine, and install it.
git clone https://github.com/geekan/metagpt
cd metagpt
pip install -e.

export PYPPETEER_EXECUTABLE_PATH="/root/.local/share/pyppeteer/local-chromium/588429"
unset PYPPETEER_EXECUTABLE_PATH

python3 startup.py "Develop an application that aims to simplify the lives of IT Systems Administrators by enabling them to define Windows Configuration Profiles loaded Powershell Scripts as well as the ability to load custom ADMX Templates for Local Policy Management and Administration. These profiles can then be used to generate Webstart MSI or One-touch PPKG Windows Provisioning Packages for use with Windows Workstation Deployment Operations and Efforts. Your insights on these aspects would be highly valuable. Thank you!" --code_review true --investment=999 --run_tests true --n_round=7

python3 startup.py "Develop a stock trading bot using the robin_stocks and yfinance Python modules. The bot should allow users to execute trading algorithms on their Robinhood account. The application should be deployable via Docker and allow customization through a YAML configuration file." --code_review true --investment=999 --run_tests true --n_round=7

python3 startup.py "Design, develop, and implement an Inventory Management System utilizing specified Microsoft technologies including SharePoint for document management, OneDrive for file storage, PowerShell for scripting, and Azure services such as Azure SQL Database and Azure Functions. The system will integrate with Salesforce for external sales data via a RESTful API. Inventory tracking will be facilitated through Zebra Barcode Scanners for both inbound and outbound goods. The analytics module will offer real-time insights into inventory turnover and sales performance metrics. Customer service features will be AI-driven, incorporating chatbots and automated email responses. Security measures will include SSL encryption, multi-factor authentication, and role-based authorization to ensure secure multi-user collaboration. The system will be accessible via web browsers (Chrome, Firefox, Safari) and mobile interfaces (iOS and Android). Include in the documentation Standard Operating Procedures, both as part of the system's User Guide and as separate documents detailing procedural steps for end-users. Data backups and recovery mechanisms must be outlined, and a timeline for user training, development, testing, and rollout must be provided. Compliance with industry-specific laws and regulations, such as GDPR, should also be specified."  --code_review true --investment=999 --run_tests true --n_round=7