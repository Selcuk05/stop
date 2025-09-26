
from sdks.novavision.src.helper.package import PackageHelper
from components.Stop.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, StopExecutor, StopResponse, StopOutputs, OutputStop


def build_response_stop(context):
    if context.branchstop:
        outputStop = OutputStop(value=context.input, branch="stop")
    else:
        outputStop = OutputStop(value=context.input)
    stopOutputs = StopOutputs(outputStop=outputStop)
    stopResponse = StopResponse(outputs=stopOutputs)
    stopExecutor = StopExecutor(value=stopResponse)
    executor = ConfigExecutor(value=stopExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel
