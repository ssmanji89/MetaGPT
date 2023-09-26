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

