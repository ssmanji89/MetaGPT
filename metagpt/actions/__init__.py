
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/11 17:44
@Author  : alexanderwu
@File    : __init__.py
"""
import enum
from metagpt.actions.action import Action as action_module
from metagpt.actions.action_output import ActionOutput as action_output_module

class ActionType(enum.Enum):
    """All types of Actions, used for indexing."""

import pkgutil
import sys

# Dynamically import all actions in the actions folder
__path__ = pkgutil.extend_path(__path__, __name__)
for importer, modname, ispkg in pkgutil.walk_packages(path=__path__, prefix=__name__+'.'):
    imported_module = __import__(modname)
    action_class = getattr(sys.modules[modname], modname.split('.')[-1])
    if issubclass(action_class, action_module.Action) and action_class is not action_module.Action:
        ActionType[modname.split('.')[-1].upper()] = action_class

__all__ = [
    "ActionType",
    "action_module as Action",
    "action_output_module as ActionOutput",
]
