<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from moderation_api import ModerationAPI
import os


with ModerationAPI(
    secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
) as ma_client:

    res = ma_client.content.submit(content={
        "type": "text",
        "text": "Hey, check out my profile for a deal!",
    }, content_id="message-48213", author_id="user-1092", conversation_id="room-general", metadata={
        "platform": "ios",
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from moderation_api import ModerationAPI
import os

async def main():

    async with ModerationAPI(
        secret_key=os.getenv("MODAPI_SECRET_KEY", ""),
    ) as ma_client:

        res = await ma_client.content.submit_async(content={
            "type": "text",
            "text": "Hey, check out my profile for a deal!",
        }, content_id="message-48213", author_id="user-1092", conversation_id="room-general", metadata={
            "platform": "ios",
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->