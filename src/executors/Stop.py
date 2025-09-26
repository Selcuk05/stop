
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.helper.executor import Executor
from sdks.novavision.src.base.component import Component
from components.Stop.src.models.PackageModel import PackageModel
from components.Stop.src.utils.response import build_response_stop


class Stop(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.input = self.request.get_param("inputStop")
        self.statement_status = self.request.get_param("stopStatementStatus")
        self.check_exists = self.request.get_param("stopCheckExists")
        self.expression = self.request.get_param("dataExpression")  # aranacak expression
        self.branchstop = False

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def apply_filter(self):
        if self.check_exists:
            return not self.input

        matched = [
            item for item in (self.input or [])
            if item.get("expression") == self.expression
        ]
        return not matched

    def run(self):
        if self.apply_filter():
            if self.statement_status == "stop":
                self.flow.stop(package_uID=self.uID)
            elif self.statement_status == "end":
                self.flow.end(package_uID=self.uID)
            elif self.statement_status == "branchstop":
                self.branchstop = True

        return build_response_stop(context=self)


if __name__ == "__main__":
    Executor(sys.argv[1]).run()
