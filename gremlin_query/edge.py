from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

from gremlin_query.vertex import Vertex


class Edge(BaseModel):
    """
    A class representing an edge in a graph database.

    Attributes:
        id (Optional[int]): The unique identifier for the edge,
            usually assigned by the database.

        label (str): The label representing the type of relationship
            between vertices (e.g., 'knows', 'works_with').

        from_vertex (Vertex): The source Vertex object.
        to_vertex (Vertex): The destination Vertex object.

        properties (Dict[str, Any]): A dictionary of key-value pairs
            representing the properties of the edge.
    """

    id: Optional[int] = Field(
        None,
        description="The ID of the edge, usually assigned by the database"
    )
    label: str = Field(..., description="The label of the edge")

    from_vertex: Vertex = Field(..., description="The source Vertex object")
    to_vertex: Vertex = Field(..., description="The destination Vertex object")

    properties: Dict[str, Any] = Field(
        default_factory=dict, description="Key-value properties of the edge"
    )
