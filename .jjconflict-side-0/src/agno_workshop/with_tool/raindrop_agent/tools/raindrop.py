"""Raindrop API Toolkit for Agno.

This module provides an Agno-compatible toolkit for interacting with the Raindrop API,
focusing on retrieving raindrops created between specific dates with specific tags.
"""

from datetime import datetime
from typing import Any

import httpx
from agno.tools import Toolkit
from agno.utils.log import logger
from pydantic import BaseModel, Field


class RaindropItem(BaseModel):
    """A model representing a Raindrop item."""

    id: str = Field(..., description="Unique identifier for the raindrop")
    title: str = Field(..., description="Title of the raindrop")
    link: str = Field(..., description="URL of the raindrop")
    created: datetime = Field(..., description="Creation timestamp")
    tags: list[str] = Field(default_factory=list, description="Tags associated with the raindrop")
    excerpt: str | None = Field(None, description="Excerpt or description of the raindrop")
    cover: str | None = Field(None, description="Cover image URL")
    collection: dict[str, Any] = Field(..., description="Collection the raindrop belongs to")


class RaindropSearch(BaseModel):
    """Response model for raindrop search results."""

    items: list[RaindropItem] = Field(default_factory=list, description="List of raindrops")
    count: int = Field(..., description="Total count of matching raindrops")


class RaindropTools(Toolkit):
    """Toolkit for interacting with Raindrop API.

    This toolkit provides tools for retrieving raindrops from the Raindrop API
    based on date ranges and tags, as well as handling OAuth authentication.
    """

    def __init__(self, access_token: str | None = None, client_id: str | None = None, client_secret: str | None = None) -> None:
        """Initialize the Raindrop toolkit.

        Args:
            access_token: The Raindrop access token for direct authentication.
            client_id: The OAuth client ID for authentication flows.
            client_secret: The OAuth client secret for authentication flows.
        """
        super().__init__(name="raindrop_tools")
        self._access_token = access_token
        self._client_id = client_id
        self._client_secret = client_secret
        self._base_url = "https://api.raindrop.io/rest/v1"

        # Register the toolkit functions
        self.register(self.get_raindrops_by_date_and_tag)

    async def _make_request(
        self,
        method: str,
        endpoint: str,
        params: dict[str, Any] | None = None,
        json_data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Make an authenticated request to the Raindrop API.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint to call
            params: Query parameters
            json_data: JSON payload for POST/PUT requests

        Returns:
            API response as a dictionary

        Raises:
            httpx.HTTPError: If the request fails
        """
        url = f"{self._base_url}/{endpoint}"

        headers = {
            "Content-Type": "application/json",
        }

        # Add authorization header if we have an API token and not making OAuth request
        headers["Authorization"] = f"Bearer {self._access_token}"

        try:
            async with httpx.AsyncClient() as client:
                response = await client.request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    json=json_data,
                    timeout=30.0,
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPError as e:
            logger.error(f"Error making request to Raindrop API: {e}")
            raise

    async def get_raindrops_by_date_and_tag(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        tag: str | None = None,
        collection_id: int = 0,
        limit: int = 50,
    ) -> dict[str, Any]:
        """Retrieve raindrops created between specific dates with a specific tag.

        Args:
            start_date: Start date in ISO format (YYYY-MM-DD)
            end_date: End date in ISO format (YYYY-MM-DD)
            tag: Tag to filter raindrops by
            collection_id: Collection ID to search in (0 for all collections)
            limit: Maximum number of raindrops to return (max 50)

        Returns:
            RaindropSearch object containing matching raindrops

        Raises:
            ValueError: If date format is invalid
            httpx.HTTPError: If the API request fails
        """
        try:
            if not self._access_token:
                msg = "Access token is required"
                raise ValueError(msg)

            # Construct the search query
            search_query = f"#{tag}" if tag else ""

            if start_date:
                search_query += f" created:>{start_date}"

            if end_date:
                search_query += f" created:<{end_date}"

            params = {
                "search": search_query,
                "sort": "created",
                "perpage": min(limit, 50),  # API limit is 50
                "page": 0,
            }

            # Make the API request
            endpoint = f"raindrops/{collection_id}"
            response_data = await self._make_request("GET", endpoint, params=params)

            # Process the response
            items = []
            for item in response_data.get("items", []):
                raindrop_item = RaindropItem(
                    id=str(item.get("_id")),
                    title=item.get("title", ""),
                    link=item.get("link", ""),
                    created=item.get("created", 0),
                    tags=item.get("tags", []),
                    excerpt=item.get("excerpt"),
                    cover=item.get("cover"),
                    collection=item.get("collection", {}),
                )
                items.append(raindrop_item)

            return RaindropSearch(items=items, count=response_data.get("count", 0)).model_dump()

        except ValueError as e:
            logger.error(f"Invalid date format: {e}")
            msg = f"Invalid date format. Please use YYYY-MM-DD format: {e}"
            raise ValueError(msg) from e
        except httpx.HTTPError as e:
            logger.error(f"Error retrieving raindrops: {e}")
            raise


# Example usage
"""
import asyncio
from agno.agent import Agent

# Initialize the toolkit with API token
raindrop_toolkit = RaindropTools(api_token="your_raindrop_api_token")

# Or initialize with OAuth client credentials
# raindrop_toolkit = RaindropTools(
#     client_id="your_client_id",
#     client_secret="your_client_secret"
# )

# Create an agent with the toolkit
agent = Agent(
    tools=[raindrop_toolkit],
    show_tool_calls=True,
    markdown=True,
)

# Use the agent
async def main():
    # Example for OAuth flow
    # First, direct user to:
    # https://raindrop.io/oauth/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI

    # Then exchange code for token
    # token_response = await raindrop_toolkit.exchange_code_for_token(
    #     code="code_from_redirect",
    #     redirect_uri="your_redirect_uri"
    # )

    # Then use the agent to search raindrops
    await agent.aprint_response(
        "Find raindrops with tag 'python' created between January 1, 2023 and March 1, 2023"
    )

asyncio.run(main())
"""
