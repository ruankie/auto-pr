from langchain.prompts import PromptTemplate

mr_prompt = PromptTemplate(
        input_variables=["commits", "format"],
        template="""I have made code changes to my git repository for which I have created a pull request.
        These changes are summarised by a series of commit messages.
        The commit message titles are: {commits}.
        
        Give me a detailed summary of the changes for adding to the pull request description.
        Use Markdown syntax for the pull request message.
        Give the pull request message in this format: {format}"""
    )