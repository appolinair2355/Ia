# Bot Telegram IA (Render Ready)

## 🔧 Configuration Render.com

1. Crée un nouveau Web Service sur https://dashboard.render.com
2. Upload ce projet (ou connecte-le à un repo GitHub avec les mêmes fichiers)
3. Ajoute les variables d’environnement :
   - `BOT_TOKEN` → Ton token Telegram
   - `OPENAI_API_KEY` → Ta clé API OpenAI
4. Render installe tout automatiquement avec `requirements.txt`
5. Le bot démarre automatiquement avec `python bot.py`

Tu peux le tester en envoyant /start puis une question.
