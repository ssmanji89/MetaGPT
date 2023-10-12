
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import fire
from metagpt.roles import (
    Architect,
    Engineer,
    ProductManager,
    ProjectManager,
    QaEngineer,
    DataAnalyst,
    QAAgent,
    SecurityAnalyst,
    UXDesigner,
    DevOpsEngineer,
    CommunityManager,
    LegalAdvisor,
    ComplianceOfficer
)
from metagpt.agents import (
    RegulatoryAgent,
    ContractManagementAgent
)
from metagpt.software_company import SoftwareCompany
from metagpt.schema import Message

async def startup(
    idea: str,
    investment: float = 3.0,
    n_round: int = 5,
    code_review: bool = False,
    run_tests: bool = False,
    implement: bool = True,
    run_data_analysis: bool = False,
    run_security_scan: bool = True,
    manage_community: bool = False,
    financial_planning: bool = False,
    marketing_and_sales: bool = True,
    human_resources: bool = False,
    legal_and_compliance: bool = True
):
    """Run a startup. Be a boss."""
    company = SoftwareCompany()
    
    # Initialize and hire roles
    roles = [
        Architect(),
        Engineer(),
        ProductManager(),
        ProjectManager(),
        QaEngineer(),
        DataAnalyst(),
        QAAgent(),
        SecurityAnalyst(),
        UXDesigner(),
        DevOpsEngineer(),
        CommunityManager(),
        LegalAdvisor(),
        ComplianceOfficer(),
        RegulatoryAgent(),
        ContractManagementAgent()
    ]
    company.hire(roles)
    # Start a project with an idea
    company.start_project(idea)

    # Legal and Compliance
    if legal_and_compliance:
        await company.environment.publish_message(Message(role="LegalAdvisor", content="Initial Legal Review"))
        await company.environment.publish_message(Message(role="ComplianceOfficer", content="Initial Compliance Check"))
        await company.environment.publish_message(Message(role="RegulatoryAgent", content="Update on Regulatory Changes"))
        await company.environment.publish_message(Message(role="ContractManagementAgent", content="Contract Management"))
        
    # Product Development Lifecycle
    if implement:
        await company.environment.publish_message(Message(role="Architect", content="Design Architecture"))
        await company.environment.publish_message(Message(role="Engineer", content="Implement Design"))
        await company.environment.publish_message(Message(role="UXDesigner", content="Design UI/UX"))
        await company.environment.publish_message(Message(role="DevOpsEngineer", content="Setup CI/CD"))
        await company.environment.publish_message(Message(role="QAAgent", content="Run Tests"))

    # Data-Driven Decision Making
    if run_data_analysis:
        await company.environment.publish_message(Message(role="DataAnalyst", content="Analyze Market Data"))
        await company.environment.publish_message(Message(role="ProductManager", content="Decide Features"))

    # Security and Compliance
    if run_security_scan:
        await company.environment.publish_message(Message(role="SecurityAnalyst", content="Run Security Scan"))
        await company.environment.publish_message(Message(role="DevOpsEngineer", content="Ensure Compliance"))

    # Community Management
    if manage_community:
        await company.environment.publish_message(Message(role="CommunityManager", content="Manage Community"))

    # Your additional business logic here
    # ...

if __name__ == "__main__":
    fire.Fire(startup)
