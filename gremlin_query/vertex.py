from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class Vertex(BaseModel):
    """
    A class representing a vertex in a graph database.

    Attributes:
        id (Optional[int]): The unique identifier for the vertex,
            usually assigned by the database.

        label (str): The label representing the type of the vertex
            (e.g., 'person', 'city').

        properties (Dict[str, Any]): A dictionary of key-value pairs
            representing the properties of the vertex.
    """

    id: Optional[str] = Field(None, description="Optional ID of the vertex")

    label: str = Field(..., description="The label of the vertex")

    properties: Dict[str, Any] = Field(
        default_factory=dict,
        description="Key-value properties of the vertex"
    )
