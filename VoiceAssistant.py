import asyncio
import json
import websockets
import pyttsx3
import enchant
import logging
import ssl

from AssistantService import assistantModel_Vi, assistantModel_En

voiceAssistant = pyttsx3.init("dummy")
voices = voiceAssistant.getProperty("voices")

checkEn = enchant.Dict("en_US")

def checkEnService(content, language: str) -> str:
    temp = content.split()
    count_vi = 0
    count_en = 0
    for i in temp:
        if checkEn.check(i):
            count_en += 1
        else:
            count_vi += 1
    
    if count_vi > count_en:
        language = "vi"
    elif  count_vi < count_en:
        language = "en"
    
    return language


def assistantSpeak(audio, language: str):
    language = checkEnService(audio, language)

    if language == "vi":
        voiceAssistant.setProperty("voice", voices[1].id)
    elif language == "en":
        voiceAssistant.setProperty("voice", voices[0].id)

    voiceAssistant.say(audio)
    voiceAssistant.runAndWait()


def assistant(userContent, language: str):
    language = checkEnService(userContent, language)
    
    if language == "vi":
        userContent = userContent.lower()
        answer = assistantModel_Vi(userContent)
        assistantSpeak(answer, "vi")
        return answer
        
    elif language == "en":
        userContent = userContent.lower()
        answer = assistantModel_En(userContent)
        assistantSpeak(answer, "en")
        return answer


# async def webSocketService(websocket, path):
#     async for message in websocket:
#         data = json.loads(message)
#         transcript = data["transcript"]
#         language = data["lng"]
        
#         answerMessage = assistant(transcript, language)

#         response_data = {"status": "success", "message": answerMessage}
#         await websocket.send(json.dumps(response_data))



# asyncio.get_event_loop().run_until_complete(
#     websockets.serve(webSocketService, "localhost", 8080, ssl = CERT)
# )


# asyncio.get_event_loop().run_forever()

logging.basicConfig()
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain("./ssl/cert.pem", "./ssl/key.pem")

async def webSocketService(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        transcript = data["transcript"]
        language = data["lng"]
        
        answerMessage = assistant(transcript, language)

        response_data = {"status": "success", "message": answerMessage}
        await websocket.send(json.dumps(response_data))



asyncio.get_event_loop().run_until_complete(
    websockets.serve(webSocketService, "localhost", 8080, ssl = ssl_context)
)


asyncio.get_event_loop().run_forever()