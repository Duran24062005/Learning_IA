from app.controllers.auth_controller import AuthController
from app.controllers.category_controller import CategoryController
from app.controllers.loan_controller import LoanAdminController, LoanResidentController
from app.controllers.menu_controller import MenuController
from app.controllers.report_controller import ReportController
from app.controllers.tool_controller import ToolController
from app.controllers.user_controller import UserController
from app.persistence.context import AppContext
from app.services.auth_service import AuthService
from app.services.category_service import CategoryService
from app.services.loan_service import LoanService
from app.services.report_service import ReportService
from app.services.tool_service import ToolService
from app.services.trace_service import TraceService
from app.services.user_service import UserService


def build_menu_controller() -> MenuController:
    context = AppContext.build()
    trace_service = TraceService(context.log_repository)

    category_service = CategoryService(context.category_repository)
    tool_service = ToolService(context.tool_repository, category_service)
    user_service = UserService(context.user_repository)
    loan_service = LoanService(
        context.loan_repository,
        tool_service,
        user_service,
        trace_service,
    )
    report_service = ReportService(
        context.tool_repository,
        context.loan_repository,
        context.user_repository,
    )
    auth_service = AuthService()

    category_controller = CategoryController(category_service, trace_service)
    tool_controller = ToolController(tool_service, trace_service)
    user_controller = UserController(user_service, trace_service)
    loan_admin_controller = LoanAdminController(loan_service, trace_service)
    loan_resident_controller = LoanResidentController(loan_service)
    report_controller = ReportController(report_service)
    auth_controller = AuthController(auth_service)

    return MenuController(
        auth_controller=auth_controller,
        category_controller=category_controller,
        tool_controller=tool_controller,
        user_controller=user_controller,
        loan_admin_controller=loan_admin_controller,
        loan_resident_controller=loan_resident_controller,
        report_controller=report_controller,
        category_service=category_service,
        tool_service=tool_service,
        user_service=user_service,
        loan_service=loan_service,
        trace_service=trace_service,
    )


def run_app() -> None:
    build_menu_controller().run()
