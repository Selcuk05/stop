
from typing import Union, Literal
from sdks.novavision.src.base.model import Inputs,Input, Package, Output, Config, Configs, Outputs, Response, Request


class OutputStop(Output):
    name: Literal["outputStop"] = "outputStop"
    value: Union[list, dict]
    type: str = "object"

    class Config:
        title = "Data"


class InputStop(Input):
    name: Literal["inputStop"] = "inputStop"
    value: Union[list, dict]
    type: str = "object"

    class Config:
        title = "Data"


class EndStatement(Config):
    name: Literal["EndStatement"] = "EndStatement"
    value: Literal["end"] = "end"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Stop App (End)"


class StopStatement(Config):
    name: Literal["stop"] = "stop"
    value: Literal["stop"] = "stop"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Stop App (Now)"


class BranchStopStatement(Config):
    name: Literal["branchstop"] = "branchstop"
    value: Literal["branchstop"] = "branchstop"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Stop Branch (Now)"


class StopStatementStatus(Config):
    """
        Statement Flag represents the result of a conditional check.
        Use this to determine if the corresponding condition has been satisfied.
    """
    name: Literal["stopStatementStatus"] = "stopStatementStatus"
    value: Union[StopStatement, EndStatement, BranchStopStatement]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Stop Operator"


class DataExpressionTrue(Config):
 name: Literal["True"] = "True"
 value: Literal[True] = True
 type: Literal["bool"] = "bool"
 field: Literal["option"] = "option"

 class Config:
     title = "True"


class DataExpressionFalse(Config):
    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "False"


class DataExpression(Config):
    """
        If you are using the Data executor within a Flow,
        you must first configure and run the Expression package
        before applying DataExpression.
    """
    name: Literal["dataExpression"] = "dataExpression"
    value: Union[DataExpressionTrue, DataExpressionFalse]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Expression Status"


class CheckExistsTrue(Config):
    name: Literal["True"] = "True"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Enable"


class CheckExistsFalse(Config):
    dataExpression: DataExpression
    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disable"


class StopCheckExists(Config):
    """
        Controls behavior based on the presence or content of the input.

        - `Enable`: Acts if the value is missing.
        - `Disable`: Acts based on a condition inside the input (e.g., confidence > 5).
    """
    name: Literal["stopCheckExists"] = "stopCheckExists"
    value: Union[CheckExistsTrue, CheckExistsFalse]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Check Exists"


class StopConfigs(Configs):
    stopCheckExists: StopCheckExists
    stopStatementStatus: StopStatementStatus


class StopInputs(Inputs):
    inputStop: InputStop


class StopOutputs(Outputs):
    outputStop: OutputStop


class StopResponse(Response):
    outputs: StopOutputs


class StopRequest(Request):
    inputs: StopInputs
    configs: StopConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class StopExecutor(Config):
    name: Literal["Stop"] = "Stop"
    value: Union[StopRequest, StopResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Stop"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[StopExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"
        json_schema_extra = {
            "target": "value"
        }


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["Stop"] = "Stop"
