import config
import createEntity
import logInToZDP
import createWorkflow
import createLZDirectory
import fetchConnections
import createFilePattern
import createDQRule

print("Log into ZDP...")
session=logInToZDP.logIn()
print("Create DQ Rule....")
ruleId,ruleName=createDQRule.createDQRule(session)
print("DQ Rule ID:  ",ruleId,"DQ Rule Name:  ",ruleName)
print(".................................")
print("Create Entity.....")
entityTypeId,version,entityName=createEntity.createEntity(session,ruleId,ruleName)
print("Entity type ID:  ",entityTypeId,"Entity version:  ",version,"Entity Name:  ",entityName)
print("-------------------------------------")
print("Create Workflow....")
wfId=createWorkflow.createWorkflow(session,entityTypeId,version,entityName)
print("Workflow created ID:  ",wfId)
print("-------------------------------------")
print("Create Connection.....")
connection_id=fetchConnections.fetch_connections(session)
print("Connection ID:  ",connection_id)
print("--------------------------------------")
print("Fetch LZ server ID......")
serverId=createLZDirectory.fetchLZServers(session)
print("LZ Server ID:  ",serverId)
print("---------------------------------------")
print("Create LZ directory.....")
lzDirId=createLZDirectory.createLZDir(session,serverId)
print("LZ directory ID:  ",lzDirId)
print("--------------------------------------")
print("Create File Pattern......")
filePatternId=createFilePattern.createFilePattern(session,lzDirId,wfId,connection_id)
print("File pattern ID:  ",filePatternId)
print("---------------------------------------")
