# ZDP API list
# log into ZDP:
# /bedrock-app/services/rest/login
log_into_zdp = "/bedrock-app/services/rest/login"
#  ----------------------------------------------------------------------
#  API related to Entity:
#  create entity:
# /bedrock-app/services/rest/projects/{project_Id}/entities
create_entity = "/bedrock-app/services/rest/projects/{}/entities"
# delete entity:
# /bedrock-app/services/rest/entities/{entity_Id}?projectIds={project_Id}
delete_entity = "/bedrock-app/services/rest/entities/{}?projectIds={}"


#  ---------------------------------------------------------------------------
#  API related to workflow:
#  create workflow:
# /bedrock-app/services/rest/projects/{project_Id}/workflows
create_workflow = "/bedrock-app/services/rest/projects/{}/workflows"
# execute workflow:
# /bedrock-app/services/rest/workflows/{workflow_Id}/execute?projectIds={project_Id}
execute_workflow = "/bedrock-app/services/rest/workflows/{}/execute?projectIds={}"



#  ----------------------------------------------------------------------------