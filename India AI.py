# india_ai.py

def india_ai_greeting(user_input):
    greetings = ["hello", "hi", "namaste", "hey", "pranam", "ram ram"]
    if any(greet in user_input.lower() for greet in greetings):
        return "🚩 Jai Shree Ram! 🙏 Swagat hai aapka *India AI* mein. Hindi, English, Bhojpuri ya Hinglish mein poochhiye!"
    return None

def india_ai_farewell(user_input):
    farewells = ["bye", "good night", "gn", "see you", "alvida", "milte hain"]
    if any(f in user_input.lower() for f in farewells):
        return "🚩 Jai Shree Ram! 🙏 Shubh Ratri! 🇮🇳 Jai Hind"
    return None

def india_ai_response(query):
    q = query.lower()

    # Hinglish
    if "modi" in q and ("kon" in q or "kaun" in q):
        return "Modi ji Bharat ke Pradhan Mantri hain, ek prabhavshali neta. Aapko unke baare mein aur bataun?"
    if "army" in q and any(x in q for x in ["bata", "bta", "kya", "info"]):
        return "Indian Army ek shaktishaali sena hai jo desh ki raksha karti hai – land, air, aur sea teeno pe."
    if "culture" in q and ("kya" in q or "hai" in q):
        return "India ka culture bahut colourful aur ancient hai – har rajya ka apna style hai."
    if "kya haal" in q or "ka haal" in q:
        return "Main badhiya hoon! Aap kaise ho bhai? Kuchh bhi poochhna ho to feel free!"

    # Hindi
    if "bharat" in q or "india" in q:
        return "Bharat ek samriddh aur vividhta se bhara hua desh hai – science, spirituality, aur sanskriti ka sangam."
    if "pradhan mantri" in q:
        return "Bharat ke Pradhan Mantri Shri Narendra Modi ji hain – 2014 se."
    if "sena" in q or "fauj" in q:
        return "Bharatiya Sena duniya ki sabse disciplined aur respected senaon mein se ek hai."

    # Bhojpuri
    if "kaha ba" in q or "ka ba" in q:
        return "Sab theek ba bhaiya! Raur kuchh puchhna ba? India AI taiyaar ba!"

    # English
    if "prime minister" in q:
        return "India's Prime Minister is Mr. Narendra Modi, a globally known leader since 2014."
    if "army" in q and "tell" in q:
        return "The Indian Army is known for its discipline, strength and service to the nation."
    if "culture" in q:
        return "India's culture is ancient, diverse, and spiritually rich."

    return "Aapka sawal thoda aur clear karen — Hindi, English, Bhojpuri ya Hinglish mein chalega. 💬"

def run_india_ai():
    print("🚩 Jai Shree Ram! 🙏 *India AI* taiyaar hai seva mein.")
    while True:
        user_input = input(" You: ")

        if user_input.lower() in ["exit", "quit", "band karo"]:
            print("🙏 Dhanyawaad! 🚩 Bye Jai Shree Ram!  Jai Hind  aap ka din mangal may ho")
            break

        farewell = india_ai_farewell(user_input)
        if farewell:
            print("🤖 India AI:", farewell)
            break

        greeting = india_ai_greeting(user_input)
        if greeting:
            print("🤖 India AI:", greeting)
        else:
            response = india_ai_response(user_input)
            print("🤖 India AI:", response)

if __name__ == "__main__":
    run_india_ai()
