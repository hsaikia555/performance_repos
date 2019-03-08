import ELK_Performance.createEntity
import ELK_Performance.logInToZDP
import ELK_Performance.createWorkflow
import ELK_Performance.createLZDirectory
import ELK_Performance.fetchConnections
import ELK_Performance.createFilePattern
import ELK_Performance.createDQRule
import time
import ELK_Performance.remoteConnection

print("Log into ZDP...")
session=ELK_Performance.logInToZDP.logIn()
print("Create DQ Rule....")
ruleId,ruleName=ELK_Performance.createDQRule.createDQRule(session)
print("DQ Rule ID:  ",ruleId,"DQ Rule Name:  ",ruleName)
print(".................................")
print("Create Entity.....")
entityTypeId,version,entityName=ELK_Performance.createEntity.createEntity(session,ruleId,ruleName)
print("Entity type ID:  ",entityTypeId,"Entity version:  ",version,"Entity Name:  ",entityName)
print("-------------------------------------")
print("Create Connection.....")
connection_id=ELK_Performance.fetchConnections.fetch_connections(session)
print("Connection ID:  ",connection_id)
print("--------------------------------------")
print("Create Workflow....")
wfId=ELK_Performance.createWorkflow.createWorkflow(session,entityTypeId,version,entityName,connection_id)
print("Workflow created ID:  ",wfId)
print("-------------------------------------")
print("Fetch LZ server ID......")
serverId=ELK_Performance.createLZDirectory.fetchLZServers(session)
print("LZ Server ID:  ",serverId)
print("---------------------------------------")
print("Create LZ directory.....")
lzDirId,lzDirPath=ELK_Performance.createLZDirectory.createLZDir(session,serverId)
print("LZ directory ID:  ",lzDirId)
print("LZ direcotry created: ",lzDirPath)
print("--------------------------------------")
print("Create File Pattern......")
filePatternId=ELK_Performance.createFilePattern.createFilePattern(session,lzDirId,wfId,connection_id)
print("File pattern ID:  ",filePatternId)
print("---------------------------------------")
#print("Sleeping for 10 seconds........")
#time.sleep(10)
#print("Trigger remote file droop script.....")
#ELK_Performance.remoteConnection.remoteConnection(lzDirPath)
