import FuckGrok
import LoveGemini

#models:Grok2 Grok3 Grok3-Thinking Gemini-Thinking Gemini-2Pro
def answer_question(question, model):
    if model == "Grok-2":
        return FuckGrok.ask_grok2(question)
    elif model == "Grok-3":
        return FuckGrok.ask_grok3(question)
    elif model == "Grok-3-Thinking":
        return FuckGrok.ask_grok3_thinking(question)
    elif model == "Gemini-Thinking":
        return LoveGemini.ask_gemini_thinking(question)
    elif model == "Gemini-2-Pro":
        return LoveGemini.ask_gemini_2pro(question)
    else:
        return "FUCK U"