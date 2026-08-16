"""Module for interaction with "cards/" endpoint of Trello API."""

from api_clients.base_client import BaseClient


class CardClient(BaseClient):
    """Class for interaction with "cards/" endpoint of Trello API."""

    def __init__(self):
        """Initialize CardsClient and set the endpoint to 'boards/'."""
        super().__init__()
        self.endpoint = "cards/"