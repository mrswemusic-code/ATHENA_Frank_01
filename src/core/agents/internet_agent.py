from src.core.agents.base_agent import BaseAgent


class InternetAgent(BaseAgent):

    def __init__(self, kernel=None):

        super().__init__(
            name="internet",
            kernel=kernel
        )

    def capabilities(self):

        return [

            "internet",
            "search",
            "search_web",
            "research",
            "news"

        ]

    def execute(self, task):

        payload = getattr(
            task,
            "payload",
            {}
        )

        query = payload.get(
            "query",
            ""
        )

        return {

            "agent": self.name,

            "status": "not_implemented",

            "message": "Internet module not implemented yet.",

            "query": query

        }
