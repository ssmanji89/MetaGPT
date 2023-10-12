
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
)
from metagpt.software_company import SoftwareCompany

async def startup(
    idea: str,
    investment: float = 3.0,
    n_round: int = 5,
    code_review: bool = False,
    run_tests: bool = False,
    implement: bool = True,
    run_data_analysis: bool = False,
    run_security_scan: bool = False,
    manage_community: bool = False,
):
    """Run a startup. Be a boss."""
    company = SoftwareCompany()
    
    # Initialize roles
    company.add_role(Architect())
    company.add_role(Engineer())
    company.add_role(ProductManager())
    company.add_role(ProjectManager())
    company.add_role(QaEngineer())
    company.add_role(DataAnalyst())
    company.add_role(QAAgent())
    company.add_role(SecurityAnalyst())
    company.add_role(UXDesigner())
    company.add_role(DevOpsEngineer())
    company.add_role(CommunityManager())

    # Your business logic here
    # ...

if __name__ == "__main__":
    fire.Fire(startup)
