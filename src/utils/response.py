
from sdks.novavision.src.helper.package import PackageHelper
from components.Stop.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, OnDataExecutor, \
    OnDataResponse, OnDataOutputs, OutputOnData, OutputOnExpression, OnExpressionOutputs, OnExpressionExecutor, \
    OnExpressionResponse


def build_response_on_data(context):
    if context.branchstop:
        outputOnData = OutputOnData(value=context.input, branch="stop")
    else:
        outputOnData = OutputOnData(value=context.input)
    onDataOutputs = OnDataOutputs(outputOnData=outputOnData)
    onDataResponse = OnDataResponse(outputs=onDataOutputs)
    onDataExecutor = OnDataExecutor(value=onDataResponse)
    executor = ConfigExecutor(value=onDataExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel

def build_response_on_expression(context):
    if context.branchstop:
        outputOnExpression = OutputOnExpression(value=context.input, branch="stop")
    else:
        outputOnExpression = OutputOnExpression(value=context.input)
    onExpressionOutputs = OnExpressionOutputs(outputOnExpression=outputOnExpression)
    onExpressionResponse = OnExpressionResponse(outputs=onExpressionOutputs)
    onExpressionExecutor = OnExpressionExecutor(value=onExpressionResponse)
    executor = ConfigExecutor(value=onExpressionExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel

