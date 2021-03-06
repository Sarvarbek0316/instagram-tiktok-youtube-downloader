from aiogram import types
from loader import dp
from main import instag, tiktok, youtube

@dp.message_handler(content_types='text')
async def test(ms:types.Message):
    link=ms.text
    
    try:
        result = youtube(link)
        for i in result:
            if i['hasAudio']:
                await ms.answer_video(i['url'])
    except:
        pass
    
    try:
        result = tiktok(link)
        await ms.answer_video(result['video'][0])
        
    except:
        pass
    
    try:
        result=instag(link)
        if result['Type']=='Post-Image':
            await ms.answer_photo(result["media"], caption=result["Title"])
        if result['Type']=='Post-Video':
            await ms.answer_video(result["media"], caption=result["Title"])
    except:
        pass
    
