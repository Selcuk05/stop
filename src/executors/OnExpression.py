
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.helper.executor import Executor
from sdks.novavision.src.base.component import Component
from components.Stop.src.models.PackageModel import PackageModel
from components.Stop.src.utils.response import build_response_on_expression


class OnExpression(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.input = self.request.get_param("inputDataOnExpression")
        self.inputExpression = self.request.get_params("inputExpressionOnExpression")
        self.statement_status = self.request.get_param("stopStatementStatus")
        self.check_exists = self.request.get_param("onExpressionCheckExists")
        self.expression = self.request.get_param("dataExpression")  # aranacak expression
        self.selection = self.request.get_param("selectionExpression") # "One" or "All"
        self.branchstop = False

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def apply_filter(self):
        if self.check_exists:
            return not self.input

        if self.selection == "All":
            # True if at least one item is NOT equal -> stop
            return any(
                exp != self.expression
                for exp in (self.inputExpression or [])
            )

        elif self.selection == "One":
            # True if no items match -> stop
            return not any(
                exp == self.expression
                for exp in (self.inputExpression or [])
            )

        return True

    def run(self):
        if self.apply_filter():
            if self.statement_status == "stop":
                self.flow.stop(package_uID=self.uID)
            elif self.statement_status == "end":
                self.flow.end(package_uID=self.uID)
            elif self.statement_status == "branchstop":
                self.branchstop = True

        return build_response_on_expression(context=self)


if __name__ == "__main__":
    Executor(sys.argv[1]).run()
