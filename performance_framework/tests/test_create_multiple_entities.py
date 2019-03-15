# Author: Himanshu Saikia
# Dated: 15/03/2019
# This module is used to create multiple entities:

import test_repo.performance_framework.core.Application.Authentication.authentication as auth
import test_repo.performance_framework.engine.create_entity.create_delimited_entity as create_delimited_entity
import test_repo.performance_framework.tests.test_controller as controller


session = auth.log_in()
no_of_entities = controller.NO_OF_ENTITIES
#Create multiple delimited entities:
create_delimited_entity.create_delimited_entity(session, no_of_entities)