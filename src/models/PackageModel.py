
from typing import Union, Literal

from sdks.novavision.src.base.model import Inputs,Input, Package, Output, Config, Configs, Outputs, Response, Request

########################################################################

class OutputOnData(Output):
    name: Literal["outputOnData"] = "outputOnData"
    value: Union[list, dict]
    type: str = "object"

    class Config:
        title = "Data"


class InputOnData(Input):
    name: Literal["inputOnData"] = "inputOnData"
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

class SelectionExpressionOne(Config):
    name: Literal["One"] = "One"
    value: Literal["One"] = "One"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "One"


class SelectionExpressionAll(Config):
    name: Literal["All"] = "All"
    value: Literal["All"] = "All"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "All"


class SelectionExpression(Config):
    """
        Choose to select based on a single item's truth or all items' truth.
    """
    name: Literal["selectionExpression"] = "selectionExpression"
    value: Union[SelectionExpressionOne, SelectionExpressionAll]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Selection Expression"


class CheckExistsTrue(Config):
    name: Literal["True"] = "True"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "No Data"


class CheckExistsFalse(Config):
    dataExpression: DataExpression
    selectionExpression: SelectionExpression
    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Data Available"


class OnDataCheckExists(Config):
    """
        Controls behavior based on the presence or content of the input.

        - `No Data`: Acts if the value is missing.
        - `Data Available`: Acts based on a condition inside the input (e.g., confidence > 5).
    """
    name: Literal["onDataCheckExists"] = "onDataCheckExists"
    value: Union[CheckExistsTrue, CheckExistsFalse]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Check Exists"


class OnDataConfigs(Configs):
    onDataCheckExists: OnDataCheckExists
    stopStatementStatus: StopStatementStatus


class OnDataInputs(Inputs):
    inputOnData: InputOnData


class OnDataOutputs(Outputs):
    outputOnData: OutputOnData


class OnDataResponse(Response):
    outputs: OnDataOutputs


class OnDataRequest(Request):
    inputs: OnDataInputs
    configs: OnDataConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class OnDataExecutor(Config):
    name: Literal["OnData"] = "OnData"
    value: Union[OnDataRequest, OnDataResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "On Data"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }

########################################################################

class OutputOnExpression(Output):
    name: Literal["outputOnExpression"] = "outputOnExpression"
    value: Union[list, dict]
    type: str = "object"

    class Config:
        title = "Data"


class InputDataOnExpression(Input):
    name: Literal["inputDataOnExpression"] = "inputDataOnExpression"
    value: Union[list, dict]
    type: str = "object"

    class Config:
        title = "Data"

class InputExpressionOnExpression(Input):
    name: Literal["inputExpressionOnExpression"] = "inputExpressionOnExpression"
    value: Union[list, dict]
    type: str = "object"

    class Config:
        title = "Expression"


class OnExpressionCheckExists(Config):
    """
        Controls behavior based on the presence or content of the input.

        - `No Data`: Acts if the value is missing.
        - `Data Available`: Acts based on a condition inside the input (e.g., confidence > 5).
    """
    name: Literal["onExpressionCheckExists"] = "onExpressionCheckExists"
    value: Union[CheckExistsTrue, CheckExistsFalse]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Check Exists"


class OnExpressionConfigs(Configs):
    onExpressionCheckExists: OnExpressionCheckExists
    stopStatementStatus: StopStatementStatus


class OnExpressionInputs(Inputs):
    inputDataOnExpression: InputDataOnExpression
    inputExpressionOnExpression: InputExpressionOnExpression


class OnExpressionOutputs(Outputs):
    outputOnExpression: OutputOnExpression


class OnExpressionResponse(Response):
    outputs: OnExpressionOutputs


class OnExpressionRequest(Request):
    inputs: OnExpressionInputs
    configs: OnExpressionConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class OnExpressionExecutor(Config):
    name: Literal["OnExpression"] = "OnExpression"
    value: Union[OnExpressionRequest, OnExpressionResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "On Expression"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }

########################################################################

class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[OnDataExecutor, OnExpressionExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "On Operation"

class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["Stop"] = "Stop"
