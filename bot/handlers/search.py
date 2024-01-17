from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from serpapi import GoogleSearch
import random
from os import getenv


router = Router()

@router.inline_query()
async def google_search(query: InlineQuery):
    search_query = query.query
    if query.from_user.id != 5047574160:
        return
    results = []

    for i in range(min(50, len(search_query))):
        response = GoogleSearch(
            {
                "q": search_query,
                "location": "Russia",
                "api_key": getenv("SERP_TOKEN")
            }
        )
    
        data = response.get_json()
        for result in data.get('organic_results', []):
            title = result.get('title', 'No Title')
            description = result.get('snippet', 'No Description')
            url = result.get('link', 'No URL')

            article = InlineQueryResultArticle(
                id=str(random.randint(-100000,98012390123890123891)),
                title=title,
                description=description,
                input_message_content=InputTextMessageContent(
                    message_text=f'<b>{title}</b>\n{description}\n\n{url}'
                )
            )
            results.append(article)

    await query.answer(results, cache_time=1)

    