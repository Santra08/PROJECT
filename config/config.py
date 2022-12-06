# import necessary packages

# %%
#File paths
modelFilePath = "modelFiles/chatbot_model.h5"
XtraningFilePath = 'modelFiles/X_train.npy'
YtraningFilePath = 'modelFiles/Y_train.npy'
intentFile = 'dataset/intents.json'
pickleFileWords = 'modelFiles/words.pkl'
pickleFileTags = 'modelFiles/tags.pkl'

#%%
#Logger details and load log module to 'log' variable
loggerName = 'Chatbot'
logFileName = loggerName+'.log'           # Log File Name
logFilePath = 'Logs/'
Path(logFilePath).mkdir(parents=True, exist_ok=True)
logPath = logFilePath+logFileName
L1 = lm.Logger(logPath, loggerName)
log = L1.writeLog()

#%%
#base url details
googleBaseUrl = "https://www.google.com/search?q="
weatherApiKey = "cf4d5fa61170327c04588207c169dd94"
weatherBaseUrl = "http://api.openweathermap.org/data/2.5/weather?"