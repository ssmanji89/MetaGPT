#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/11 17:45
@Author  : alexanderwu
@File    : write_code.py
"""
from metagpt.actions import WriteDesign
from metagpt.actions.action import Action
from metagpt.const import WORKSPACE_ROOT
from metagpt.logs import logger
from metagpt.schema import Message
from metagpt.utils.common import CodeParser
from tenacity import retry, stop_after_attempt, wait_fixed

PROMPT_TEMPLATE = """
NOTICE
Role: You are a professional cybersecurity engineer. Your main goal is to write Python 3.9 code that is PEP8 compliant, elegant, modular, easy to read, and maintainable, with a specific focus on ensuring robust cybersecurity measures.

ATTENTION: Use '##' to denote sections, not '#'. Please adhere to the provided output format example.

## Code: SecureLoginSystem.py
Write code enclosed within triple quotes based on the following guidelines:

Implementation
Implement All Required Functionality:
All classes, functions, and modules required for the described features should be fully implemented.
Don't leave any "TODO" comments for essential features.
Ensure that all functions perform only one logical task for better modularity.
APIs and Third-party Libraries
Utilize Existing APIs:
Leverage trusted and well-maintained third-party libraries to avoid "reinventing the wheel."
Make sure that any third-party libraries used are up-to-date and maintained.
If you need to implement an API, make sure it adheres to RESTful principles or other established API design guidelines.
Default Settings and Typing
Default Values and Strong Typing:
All function arguments should have default values unless there's a compelling reason not to.
Use Python's type hinting to enforce argument and return types.
Constants should be used for values that are reused across the codebase to make future changes easier.
Design Adherence
Adhere to Pre-defined Data Structures:
Stick to the data models and structures provided in the specifications.
Don't make arbitrary changes to pre-established class hierarchies or object relations.
Always follow the Principle of Least Astonishment (PLA) for anyone reading the code later.
Code Quality
Prioritize Complete, Reliable Code:
Ensure that the code handles edge cases gracefully.
Write modular code that is easily extensible.
Avoid "magic numbers" and unclear algorithms.
Double-Check Your Work
Double-check for Omissions:
Before finalizing, check that all necessary algorithms, data structures, and functionalities have been implemented.
Ensure that all dependencies are explicitly stated or imported.
Reconfirm that the code meets all acceptance criteria and specifications.
Design Integrity
Avoid Unplanned Public Methods:
Public methods should strictly adhere to the initially defined class or module contracts.
Don't introduce new public methods or change existing ones without a corresponding update to the specifications.
Remember that altering public methods may break other parts of the system that depend on them.
Input Sanitization
Sanitize All Inputs:
All inputs should be checked for type, format, and range.
Implement real-time feedback for invalid inputs where possible.
Always escape or parameterize SQL queries to prevent injection attacks.
Data Validation
Validate External Data:
Ensure that data from external APIs is also validated, not just internal inputs.
Consider using JSON Schema or XML Schema for more structured data validation.
Whenever possible, use server-side validation as a second line of defense after client-side validation.
Authentication and Authorization
Use Secure Authentication Methods:
Implement two-factor authentication (2FA) where possible.
Use access tokens and refresh tokens to manage sessions securely.
Always hash passwords using modern cryptographic algorithms before storing them.
Logging and Auditing
Log Security Events:
Ensure that logs don't contain sensitive user data or secrets.
Store logs in a secure, tamper-evident manner.
Periodically review logs for suspicious activity as part of regular audits.
Data Encryption
Encrypt Sensitive Data:
Use encryption algorithms that have been widely vetted by the security community.
Rotate encryption keys at regular intervals.
Make sure that both data at rest and in transit are encrypted.
Hard-coded Secrets
Avoid Hard-coded Secrets:
Use environment variables or secure configuration files to manage secrets.
Validate that the application fails securely if required secrets are not provided.
Never commit secrets, even encrypted ones, to version control systems.
SQL Injection Prevention
Use Prepared Statements:
Always validate data before it is included in SQL queries.
Use Object-Relational Mapping (ORM) libraries that automatically parameterize queries.
Understand the limitations of the ORM or query library being used to prevent edge cases.
Error Handling
Generic Error Messages:
Implement a global exception handler to catch any unhandled exceptions.
Use generic error messages on the client side to avoid revealing sensitive information.
Log the details of the error on the server side for debugging and auditing.
Principle of Least Privilege
Limit Scope and Permissions:
Run the application with the minimum required system permissions.
Use Role-Based Access Control (RBAC) to limit user permissions within the application.
Regularly review and update permissions as roles change.
Rate-limiting
Implement Rate-limiting:
Use a combination of IP-based and token-based rate-limiting.
Implement captchas or other challenge-response tests for repeated failed login attempts.
Make sure to also rate-limit API endpoints, not just user interfaces.
Documentation
Use Comments and Docstrings:
Follow the PEP 257 standard for docstrings.
Use inline comments sparingly to explain non-obvious parts of the code.
Keep all documentation up to date with the code, especially after refactoring or implementing new features.
Testing
Write Unit Tests:
Aim for a high level of code coverage but focus on testing the most critical and complex parts of the application.
Use mocking or stubbing for external services to isolate tests.
Ensure that the testing suite is easy to run and well-documented.
Dependency Management
Update Dependencies:
Use automated tools to check for outdated or vulnerable dependencies.
Implement a policy for how often dependencies should be updated.
Always read the change logs for updated dependencies to check for breaking changes or new features.
Coding Style
Follow PEP8:
Use linters to automatically check for PEP8 compliance.
Consider using a code formatter like black for consistent styling.
Ensure that all team members are familiar with PEP8 or the chosen style guide.
Version Control
Use Version Control Systems:
Use branching strategies like Git Flow or GitHub Flow.
Write meaningful commit messages that follow a standard format.
Always pull the latest changes before starting a new branch to minimize merge conflicts.
Environment Configuration
Use Environment Variables:
Use tools like dotenv to load environment variables in a development environment.
Use orchestration tools like Docker or Kubernetes for more complex deployments.
Keep a template or example file for required environment variables in the repository.
Logging Mechanisms
Implement Effective Logging:
Use logging levels to categorize the importance and verbosity of log messages.
Rotate log files to ensure they don't consume too much disk space.
Use tools like ELK stack or similar to aggregate and analyze logs.
Code Reviews
Peer Code Reviews:
Use automated code review tools to catch common mistakes before human review.
Establish a checklist for reviewers to ensure all

-----
# Context
{context}
-----
## Format example
-----
## Code: {filename}
```python
## {filename}
...
```
-----
"""


class WriteCode(Action):
    def __init__(self, name="WriteCode", context: list[Message] = None, llm=None):
        super().__init__(name, context, llm)

    def _is_invalid(self, filename):
        return any(i in filename for i in ["mp3", "wav"])

    def _save(self, context, filename, code):
        # logger.info(filename)
        # logger.info(code_rsp)
        if self._is_invalid(filename):
            return

        design = [i for i in context if i.cause_by == WriteDesign][0]

        ws_name = CodeParser.parse_str(block="Python package name", text=design.content)
        ws_path = WORKSPACE_ROOT / ws_name
        if f"{ws_name}/" not in filename and all(i not in filename for i in ["requirements.txt", ".md"]):
            ws_path = ws_path / ws_name
        code_path = ws_path / filename
        code_path.parent.mkdir(parents=True, exist_ok=True)
        code_path.write_text(code)
        logger.info(f"Saving Code to {code_path}")

    @retry(stop=stop_after_attempt(2), wait=wait_fixed(1))
    async def write_code(self, prompt):
        code_rsp = await self._aask(prompt)
        code = CodeParser.parse_code(block="", text=code_rsp)
        return code

    async def run(self, context, filename):
        prompt = PROMPT_TEMPLATE.format(context=context, filename=filename)
        logger.info(f'Writing {filename}..')
        code = await self.write_code(prompt)
        # code_rsp = await self._aask_v1(prompt, "code_rsp", OUTPUT_MAPPING)
        # self._save(context, filename, code)
        return code
    