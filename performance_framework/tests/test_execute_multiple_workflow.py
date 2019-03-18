# Author: Himanshu Saikia
# Dated: 15/03/2019
# This module is used to create multiple entities:

import test_repo.performance_framework.core.Application.Authentication.authentication as auth
import test_repo.performance_framework.engine.execute_workflow.execute_workflow as execute_workflow
import test_repo.performance_framework.tests.test_controller as controller

#  execute multiple UTF workflow:
session = auth.log_in()
workflow_execution_frequency = controller.WORKFLOW_EXECUTION_FREQUENCY
workflow_id = controller.WORKFLOW_ID
workflow_name = controller.WORKFLOW_NAME
execute_workflow.execute_workflow(session, workflow_execution_frequency, workflow_name, workflow_id)
