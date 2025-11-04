print("file aviable")

import requests
import telebot
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
#--------------------------------------------------------------------------------------------------------
# Bot initialization
#--------------------------------------------------------------------------------------------------------
bot = telebot.TeleBot("Bot_API")

#--------------------------------------------------------------------------------------------------------
# Currencies
#--------------------------------------------------------------------------------------------------------
CURRENCIES = {
    "usd": "🇺🇸 USD",
    "eur": "🇪🇺 EUR",
    "rub": "🇷🇺 RUB",
    "inr": "🇮🇳 INR",
    "gbp": "🇬🇧 GBP",
    "jpy": "🇯🇵 JPY",
    "cny": "🇨🇳 CNY",
    "brl": "🇧🇷 BRL",
    "aed": "🇦🇪 AED",
    "chf": "🇨🇭 CHF",
    "try": "🇹🇷 TRY",
    "kzt": "🇰🇿 KZT",
}

#--------------------------------------------------------------------------------------------------------
# Localization
#--------------------------------------------------------------------------------------------------------
TEXTS = {
    "en": {
        "hint": "Choose a currency to see Monero (XMR) price:",
        "price": "Monero (XMR) price: {price:.2f} {curr}",
        "error": "Error getting data. Try again later.",
        "inline_hint": "Type: @moneroprice_bot usd / eur / rub ...",
        "start": "Hi! Send a currency code (e.g., usd, eur, rub) or tap a button to get Monero price.",
        "help": "Send a currency code or tap a button. Inline mode also works: @moneroprice_bot usd",
        "wrong": "I didn't get that. Send a currency code like 'usd' or use the buttons below.",
        "choose": "Choose a currency:",
    },
    
    "ru": {
        "hint": "Выберите валюту, чтобы узнать курс Monero (XMR):",
        "price": "Курс Monero (XMR): {price:.2f} {curr}",
        "error": "Ошибка при получении данных . Попробуй позже.",
        "inline_hint": "Введите: @moneroprice_bot usd / eur / rub ...",
        "start": "Привет! Я показываю курс Monero к выбранной валюте. Нажми кнопку или отправь код валюты (например: usd, eur, rub).",
        "help": "Отправь код валюты (usd, eur, rub, ...), или нажми кнопку ниже. Также можно использовать меня в инлайн-режиме: @moneroprice_bot usd",
        "wrong": "Не понял запрос. Отправь код валюты (например, usd) или воспользуйся кнопками ниже.",
        "choose": "Выбери валюту:",
    },

    "fr": {
      "hint": "Choisissez une devise pour voir le prix du Monero (XMR) :",
      "price": "Prix du Monero (XMR) : {price:.2f} {curr}",
      "error": "Erreur lors de la récupération des données. Réessayez plus tard.",
      "inline_hint": "Tapez : @moneroprice_bot usd / eur / rub ...",
      "start": "Salut ! Envoyez un code de devise (ex. usd, eur, rub) ou appuyez sur un bouton pour obtenir le prix du Monero.",
      "help": "Envoyez un code de devise ou utilisez un bouton. Le mode inline fonctionne aussi : @moneroprice_bot usd",
      "wrong": "Je n’ai pas compris. Envoyez un code comme 'usd' ou utilisez les boutons ci-dessous.",
      "choose": "Choisissez une devise :"
    },

    "hi": {
        "hint": "Monero (XMR) की कीमत देखने के लिए एक मुद्रा चुनें:",
        "price": "Monero (XMR) की कीमत: {price:.2f} {curr}",
        "error": "डेटा प्राप्त करने में समस्या हुई। बाद में पुनः प्रयास करें।",
        "inline_hint": "टाइप करें: @moneroprice_bot usd / eur / rub ...",
        "start": "नमस्ते! कोई मुद्रा कोड भेजें (जैसे usd, eur, rub) या बटन दबाएँ और Monero की कीमत प्राप्त करें।",
        "help": "कोई मुद्रा कोड भेजें या बटन का उपयोग करें। इनलाइन मोड भी काम करता है: @moneroprice_bot usd",
        "wrong": "मैं समझ नहीं पाया। कृपया 'usd' जैसे मुद्रा कोड भेजें या नीचे दिए गए बटनों का उपयोग करें।",
        "choose": "एक मुद्रा चुनें:"
    }, 

    "de": {
        "hint": "Wählen Sie eine Währung, um den Monero (XMR)-Preis anzuzeigen:",
        "price": "Monero (XMR) Preis: {price:.2f} {curr}",
        "error": "Fehler beim Abrufen der Daten. Bitte später erneut versuchen.",
        "inline_hint": "Geben Sie ein: @moneroprice_bot usd / eur / rub ...",
        "start": "Senden Sie einen Währungscode (z. B. usd, eur, rub) oder tippen Sie auf eine Taste.",
        "help": "Senden Sie einen Währungscode oder nutzen Sie Tasten. Inline: @moneroprice_bot usd",
        "wrong": "Unklar. Senden Sie einen Währungscode wie „usd“ oder nutzen Sie die Tasten.",
        "choose": "Währung wählen:",
    },

    "nl": {
        "hint": "Kies een valuta om de Monero (XMR) prijs te zien:",
        "price": "Monero (XMR) prijs: {price:.2f} {curr}",
        "error": "Fout bij het ophalen van gegevens. Probeer het later opnieuw.",
        "inline_hint": "Typ: @moneroprice_bot usd / eur / rub ...",
        "start": "Stuur een valutacode (bijv. usd, eur, rub) of tik op een knop.",
        "help": "Stuur een valutacode of gebruik knoppen. Inline: @moneroprice_bot usd",
        "wrong": "Onbekend verzoek. Stuur een valutacode zoals 'usd' of gebruik de knoppen.",
        "choose": "Kies een valuta:",
    },

    "es": {
        "hint": "Elige una moneda para ver el precio de Monero (XMR):",
        "price": "Precio de Monero (XMR): {price:.2f} {curr}",
        "error": "Error al obtener los datos Inténtalo más tarde.",
        "inline_hint": "Escribe: @moneroprice_bot usd / eur / rub ...",
        "start": "Envía un código de moneda (p. ej., usd, eur, rub) o usa un botón.",
        "help": "Envía un código o usa botones. Modo inline: @moneroprice_bot usd",
        "wrong": "No entendí. Envía un código como 'usd' o usa los botones.",
        "choose": "Elige moneda:",
    },

    "pt-br": {
        "hint": "Escolha uma moeda para ver o preço do Monero (XMR):",
        "price": "Preço do Monero (XMR): {price:.2f} {curr}",
        "error": "Erro ao obter dados. Tente novamente mais tarde.",
        "inline_hint": "Digite: @moneroprice_bot usd / eur / rub ...",
        "start": "Envie um código de moeda (ex.: usd, eur, rub) ou toque em um botão.",
        "help": "Envie um código ou use botões. Inline: @moneroprice_bot usd",
        "wrong": "Não entendi. Envie um código como 'usd' ou use os botões.",
        "choose": "Escolha a moeda:",
    },

    "ar": {
        "hint": "اختر العملة لعرض سعر مونيرو (XMR):",
        "price": "سعر مونيرو (XMR): {price:.2f} {curr}",
        "error": "حدث خطأ أثناء جلب البيانات . حاول مرة أخرى لاحقًا.",
        "inline_hint": "اكتب: @moneroprice_bot usd / eur / rub ...",
        "start": "أرسل رمز العملة (مثل usd أو eur أو rub) أو استخدم الأزرار.",
        "help": "أرسل رمزًا أو استخدم الأزرار. وضع inline: @moneroprice_bot usd",
        "wrong": "غير واضح. أرسل رمزًا مثل 'usd' أو استخدم الأزرار.",
        "choose": "اختر العملة:",
    },

    "zh": {
        "hint": "选择一种货币以查看门罗币 (XMR) 价格：",
        "price": " 门罗币 (XMR) 价格：{price:.2f} {curr}",
        "error": "获取数据时出错 。请稍后重试。",
        "inline_hint": "输入：@moneroprice_bot usd / eur / rub ...",
        "start": "发送货币代码（如 usd、eur、rub）或点击按钮。",
        "help": "发送代码或使用按钮。内联模式：@moneroprice_bot usd",
        "wrong": "未理解。发送类似“usd”的代码或使用下方按钮。",
        "choose": "选择货币：",
    },
}

#--------------------------------------------------------------------------------------------------------
# some functions
#--------------------------------------------------------------------------------------------------------
def tr(lang, key, **kwargs):
    base = (lang or "en").split("-")[0].lower()
    text = TEXTS.get(base, TEXTS["en"]).get(key, key)
    return text.format(**kwargs)

def get_xmr_price(currency: str) -> float:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies={currency}"
    data = requests.get(url, timeout=5).json()
    return data["monero"][currency]

def build_reply_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    rows = list(CURRENCIES.items())
    chunk = 4
    for i in range(0, len(rows), chunk):
        kb.add(*(KeyboardButton(code.upper()) for code, _ in rows[i:i+chunk]))
    return kb

def send_price_message(chat_id: int, currency_code: str, lang: str):
    code = currency_code.lower()
    if code in CURRENCIES:
        try:
            price = get_xmr_price(code)
            msg = tr(lang, "price", price=price, curr=CURRENCIES[code])
        except Exception:
            msg = tr(lang, "error")
    else:
        msg = tr(lang, "wrong")
    bot.send_message(chat_id, msg, reply_markup=build_reply_keyboard())

#--------------------------------------------------------------------------------------------------------
# Inline
#--------------------------------------------------------------------------------------------------------
@bot.inline_handler(lambda query: True)
def inline_query(query):
    lang = getattr(query.from_user, "language_code", None) or "en"
    text = (query.query or "").strip().lower()
    results = []

    if not text:
        markup = InlineKeyboardMarkup(row_width=3)
        for code, label in CURRENCIES.items():
            markup.add(
                InlineKeyboardButton(
                    label,
                    switch_inline_query_current_chat=code
                )
            )
        result = InlineQueryResultArticle(
            id="0",
            title="Monero (XMR)",
            description=tr(lang, "hint"),
            input_message_content=InputTextMessageContent(tr(lang, "inline_hint")),
            reply_markup=markup,
        )
        results.append(result)
    elif text in CURRENCIES:
        try:
            price = get_xmr_price(text)
            msg = tr(lang, "price", price=price, curr=CURRENCIES[text])
        except Exception:
            msg = tr(lang, "error")
        results.append(
            InlineQueryResultArticle(
                id="1",
                title=msg,
                input_message_content=InputTextMessageContent(msg),
            )
        )
    else:
        results.append(
            InlineQueryResultArticle(
                id="2",
                title=tr(lang, "inline_hint"),
                input_message_content=InputTextMessageContent(tr(lang, "inline_hint")),
            )
        )
    bot.answer_inline_query(query.id, results, cache_time=5)

#--------------------------------------------------------------------------------------------------------
# chat with bot
#--------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=["start"])
def cmd_start(message):
    lang = getattr(message.from_user, "language_code", None) or "en"
    bot.send_message(
        message.chat.id,
        tr(lang, "start"),
        reply_markup=build_reply_keyboard()
    )
    bot.send_message(message.chat.id, tr(lang, "choose"))

@bot.message_handler(commands=["help"])
def cmd_help(message):
    lang = getattr(message.from_user, "language_code", None) or "en"
    bot.send_message(
        message.chat.id,
        tr(lang, "help"),
        reply_markup=build_reply_keyboard()
    )

@bot.message_handler(commands=["currencies"])
def cmd_currencies(message):
    lang = getattr(message.from_user, "language_code", None) or "en"
    codes = ", ".join(code.upper() for code in CURRENCIES.keys())
    bot.send_message(
        message.chat.id,
        f"{tr(lang, 'choose')} {codes}",
        reply_markup=build_reply_keyboard()
    )

@bot.message_handler(func=lambda m: True)
def handle_text(message):
    lang = getattr(message.from_user, "language_code", None) or "en"
    text = (message.text or "").strip().lower()
    candidate = None

   
    if text in CURRENCIES:
        candidate = text
    else:
        parts = text.split()
        for p in parts:
            if p in CURRENCIES:
                candidate = p
                break
            if len(p) == 3 and p.lower() in CURRENCIES:
                candidate = p.lower()
                break

    if candidate:
        send_price_message(message.chat.id, candidate, lang)
    else:
        bot.send_message(message.chat.id, tr(lang, "wrong"), reply_markup=build_reply_keyboard())

#--------------------------------------------------------------------------------------------------------
# Start bot
#--------------------------------------------------------------------------------------------------------
print("bot started")
bot.infinity_polling()
