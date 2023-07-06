import asyncio
from typing import Any, Dict, List

from langchain.chat_models import ChatOpenAI
from langchain.schema import LLMResult, HumanMessage
from langchain.callbacks.base import AsyncCallbackHandler, BaseCallbackHandler


class MyCustomSyncHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        print(f"同步回调被调用: token: {token}")


class MyCustomAsyncHandler(AsyncCallbackHandler):
    async def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Run when chain starts running."""
        print("LLM调用开始....")
        await asyncio.sleep(0.3)
        print("Hi! I just woke up. Your llm is starting")

    async def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Run when chain ends running."""
        print("LLM调用结束....")
        await asyncio.sleep(0.3)
        print("Hi! I just woke up. Your llm is ending")


if __name__ == "__main__":
    chat = ChatOpenAI(
        max_tokens=25,
        streaming=True,
        callbacks=[MyCustomSyncHandler(), MyCustomAsyncHandler()],
    )

    asyncio.run(chat.agenerate([[HumanMessage(content="讲个笑话")]]))