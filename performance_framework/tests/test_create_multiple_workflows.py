# Author: Himanshu Saikia
# Dated: 15/03/2019
# This module is used to create multiple workflow:

import test_repo.performance_framework.core.Application.Authentication.authentication as auth
import test_repo.performance_framework.engine.create_workflow.create_UTF_workflow as create_utf_workflow
import test_repo.performance_framework.tests.test_controller as controller

#  Create multiple UTF workflow:
session = auth.log_in()
no_of_utf_workflow = controller.NO_OF_UTF_WORKFLOW
wf_base_path = controller.WORKFLOW_BASE_PATH
utf_input_path = controller.UTF_INPUT_PATH
create_utf_workflow.create_utf_workflow(session,no_of_utf_workflow,utf_input_path,wf_base_path)