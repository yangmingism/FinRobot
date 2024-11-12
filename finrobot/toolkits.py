from autogen import register_function, ConversableAgent
from .data_source import *
from .functional.coding import CodingUtils

from typing import List, Callable
from functools import wraps
from pandas import DataFrame

# stringify_output 装饰器：将工具函数的输出转换为字符串，方便在对话中显示。
def stringify_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, DataFrame):
            return result.to_string()
        else:
            return str(result)

    return wrapper


def register_toolkits(
    config: List[dict | Callable | type],
    caller: ConversableAgent,
    executor: ConversableAgent,
    **kwargs
):
    """Register tools from a configuration list. 函数：注册一系列工具函数，可以是函数对象、字典，或者类。"""

    for tool in config:

        if isinstance(tool, type):
            register_tookits_from_cls(caller, executor, tool, **kwargs)
            continue

        tool_dict = {"function": tool} if callable(tool) else tool
        if "function" not in tool_dict or not callable(tool_dict["function"]):
            raise ValueError(
                "Function not found in tool configuration or not callable."
            )

        tool_function = tool_dict["function"]
        name = tool_dict.get("name", tool_function.__name__)
        description = tool_dict.get("description", tool_function.__doc__)
        register_function(
            stringify_output(tool_function),
            caller=caller,
            executor=executor,
            name=name,
            description=description,
        )


def register_code_writing(caller: ConversableAgent, executor: ConversableAgent):
    """Register code writing tools. 函数：注册代码编写相关的工具函数。"""

    register_toolkits(
        [
            {
                "function": CodingUtils.list_dir,
                "name": "list_files",
                "description": "List files in a directory.",
            },
            {
                "function": CodingUtils.see_file,
                "name": "see_file",
                "description": "Check the contents of a chosen file.",
            },
            {
                "function": CodingUtils.modify_code,
                "name": "modify_code",
                "description": "Replace old piece of code with new one.",
            },
            {
                "function": CodingUtils.create_file_with_code,
                "name": "create_file_with_code",
                "description": "Create a new file with provided code.",
            },
        ],
        caller,
        executor,
    )


def register_tookits_from_cls(
    caller: ConversableAgent,
    executor: ConversableAgent,
    cls: type,
    include_private: bool = False,
):
    """Register all methods of a class as tools. 函数：将类的所有方法注册为工具函数。"""
    if include_private:
        funcs = [
            func
            for func in dir(cls)
            if callable(getattr(cls, func)) and not func.startswith("__")
        ]
    else:
        funcs = [
            func
            for func in dir(cls)
            if callable(getattr(cls, func))
            and not func.startswith("__")
            and not func.startswith("_")
        ]
    register_toolkits([getattr(cls, func) for func in funcs], caller, executor)

# ## 代码解读：`toolkits.py`

# 这段代码定义了一些用于注册和管理工具函数的工具，主要用于 ConversableAgent（可对话代理）。


# ### 主要功能：

# 1. **注册工具函数：**
#    - `register_tookits` 函数：注册一系列工具函数，可以是函数对象、字典，或者类。
#    - `register_tookits_from_cls` 函数：将类的所有方法注册为工具函数。
#    - `register_code_writing` 函数：注册代码编写相关的工具函数。


# 2. **工具函数的包装：**
#    - `stringify_output` 装饰器：将工具函数的输出转换为字符串，方便在对话中显示。


# ### 代码逻辑：

# 1. **`register_tookits` 函数：**
#    - 遍历传入的 `config` 列表，逐个处理工具函数。
#    - 如果是类，则调用 `register_tookits_from_cls` 函数注册类的方法。
#    - 如果是字典或函数，则从中提取函数对象、名称和描述信息。
#    - 使用 `register_function` 函数注册工具函数，将其包装为 `stringify_output` 装饰器，并将名称和描述信息传递给 `register_function` 函数。


# 2. **`register_tookits_from_cls` 函数：**
#    - 获取类 `cls` 的所有方法名，过滤掉私有方法和特殊方法。
#    - 将所有方法转换为函数对象，并调用 `register_tookits` 函数注册。


# 3. **`register_code_writing` 函数：**
#    - 注册一些代码编写相关的工具函数，例如 `list_files`、`see_file`、`modify_code` 和 `create_file_with_code`。


# ### 代码设计思路：

# - 模块化：将工具函数的注册和管理与 ConversableAgent 的实现分离。
# - 可扩展性：可以使用 `register_tookits` 函数注册任意类型的工具函数。
# - 可配置性：可以使用字典配置工具函数的名称和描述信息。


# ### 代码风格：

# - 使用类型注解：提高代码的可读性和可维护性。
# - 使用装饰器：简化代码逻辑。
# - 使用函数式编程：提高代码的可重用性。


# ### 总结：

# `toolkits.py` 模块提供了一套灵活、可扩展的工具函数注册和管理机制，方便 ConversableAgent 使用各种工具函数。