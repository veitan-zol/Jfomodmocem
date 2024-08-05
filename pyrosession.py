import asyncio
from pyrogram import Client


async def main():
    print("- Py-MAX Session Pyrogram -")
    print("\n---------------------------\n")
    api_id = int(input("APP ID: "))
    api_hash = input("API HASH: ")
    print("\n---------------------------\n")
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        await app.send_message(
            "me",
            "**كود سيشن البايروجرام يازميلي**:\n\n"
            f"`{await app.export_session_string()}`"
        )
        print(
            "تم بنجاح استخراج كود السيشن يا زميلي البايروجرام"
            "هتلقي الكود في الرسائل المحفوظه بتاعت حسابك يازميلي"
        )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
