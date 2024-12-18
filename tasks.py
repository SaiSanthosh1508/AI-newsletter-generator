from crewai import Task
from agents import news_retriever_agent,news_analyzer_agent,news_formatter_agent

news_retrieve_task = Task(
    name = "content retrieval task",
    description = "retrieve latest advancements and trends in the field of AI in this week"\
        "Make sure to include any latest groundbreaking researches, latest models released"\
        "top web conferences or any other important news related to AI from AI tech giants",
    agent=news_retriever_agent,
    output_file="news_retrieved.txt",
    expected_output = """A list of top AI news story titles, URLs, and a brief summary for each story from the past week. 
                Example Output: 
                [
                    {  'title': 'AI takes spotlight in Super Bowl commercials', 
                    'url': 'https://example.com/story1', 
                    'summary': 'AI made a splash in this year\'s Super Bowl commercials...'
                    }, 
                    {{...}}
                ]
            """
)

news_analyzer_task = Task(
    name = "news analysis task",
    description = "analyze the retrieved news and make sure you utilise only those related to AI latest trends and advancements"\
        "Do not include the example given in the expected output",
    agent=news_analyzer_agent,
    context = [news_retrieve_task],
    output_file="news_analyzed.txt",
    expected_output = """A list of top AI news story titles, URLs, and a brief summary for each story from the past week. 
                Example Output: 
                [
                    {  'title': 'AI takes spotlight in Super Bowl commercials', 
                    'url': 'https://example.com/story1', 
                    'summary': 'AI made a splash in this year\'s Super Bowl commercials...'
                    }, 
                    {{...}}
                ]
            """
)

news_formatting_task = Task(
    name = "news formatting task",
    description= "Format the information in a visually appealing format with icons, images, and neat alignment. Utilize the right font properties to design a newsletter."\
        "Make sure to include the title, URL, and a brief summary for each story."\
         "You can use any tools or software you are comfortable with to design the newsletter.Write atleast 10 top and latest news articles", 
    agent=news_formatter_agent, 
    context=[news_analyzer_task],
    output_file="news_formatted.md",
    expected_output='''
                    expected_output_format = """
## 📰 AI Daily Digest - [Date]

### 1. **[Title of News Article 1]**
   - 📅 **Date**: DD/MM/YYYY
   - 📝 **Summary**: A concise 6-7 sentence summary explaining the article.
   - 🔗 **Source**: [Link to original article]
   - 🏷️ **Category**: AI Models
   - 📝 **Key Insights**: This article highlights new advancements in AI-based natural language processing models. Researchers have achieved a 30% reduction in model size while improving accuracy by 15%.
   
---

### 2. **[Title of News Article 2]**
   - 📅 **Date**: MM/DD/YYYY
   - 📝 **Summary**: A concise 4-5 sentence summary explaining the article.
   - 🔗 **Source**: [Link to original article]
   - 🏷️ **Category**: AI Research
   - 📝 **Key Insights**: This article discusses the challenges and breakthroughs in AI ethics and how transparency in AI systems is becoming a priority for leading tech companies.
   
---

### 3. **[Title of News Article 3]**
   - 📅 **Date**: MM/DD/YYYY
   - 📝 **Summary**: A concise 4-5 sentence summary explaining the article.
   - 🔗 **Source**: [Link to original article]
   - 🏷️ **Category**: AI Ethics
   - 📝 **Key Insights**: This article addresses the growing concerns about bias in AI models and calls for more diversity in AI development teams to mitigate inherent biases.
   
---

                    ''' 
)