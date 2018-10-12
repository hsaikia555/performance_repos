import createEntity
import logInToZDP
import createWorkflow
import createLZDirectory
import fetchConnections
import createFilePattern
import createDQRule
import time
import SOAK_Test_502.remoteConnection
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
print("Create Connection.....")
connection_id=fetchConnections.fetch_connections(session)
print("Connection ID:  ",connection_id)
print("--------------------------------------")
print("Create Workflow....")
wfId=createWorkflow.createWorkflow(session,entityTypeId,version,entityName,connection_id)
print("Workflow created ID:  ",wfId)
print("-------------------------------------")
print("Fetch LZ server ID......")
serverId=createLZDirectory.fetchLZServers(session)
print("LZ Server ID:  ",serverId)
print("---------------------------------------")
print("Create LZ directory.....")
lzDirId,lzDirPath=createLZDirectory.createLZDir(session,serverId)
print("LZ directory ID:  ",lzDirId)
print("LZ direcotry created: ",lzDirPath)
print("--------------------------------------")
print("Create File Pattern......")
filePatternId=createFilePattern.createFilePattern(session,lzDirId,wfId,connection_id)
print("File pattern ID:  ",filePatternId)
print("---------------------------------------")
print("Sleeping for 10 seconds........")
time.sleep(10)
print("Trigger remote file droop script.....")
SOAK_Test_502.remoteConnection.remoteConnection(lzDirPath)
