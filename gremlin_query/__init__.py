from gremlin_query.edge import Edge
from gremlin_query.vertex import Vertex


def addV(vertex: Vertex) -> str:
    """
    Generate a Gremlin query to add a vertex using the provided Vertex object.

    Args:
        vertex (Vertex): A Vertex object containing the label and properties.

    Returns:
        str: A Gremlin query to add the vertex.
    """
    query = f"g.addV('{vertex.label}')"

    for key, value in vertex.properties.items():
        query += f".property('{key}', '{value}')"

    return query


def addE(edge: Edge) -> str:
    """
    Generate a Gremlin query to add an edge between two vertices.

    Args:
        edge (Edge): The Edge object containing the label, source vertex,
            destination vertex, and properties.

    Returns:
        str: A Gremlin query to add the edge between the two vertices.
    """
    from_key, from_value = list(edge.from_vertex.properties.items())[0]
    to_key, to_value = list(edge.to_vertex.properties.items())[0]

    query = (
        f"g.V().has('{from_key}', '{from_value}').as('from').V()"
        f".has('{to_key}', '{to_value}').addE('{edge.label}').from('from')"
    )

    if edge.properties:
        for key, value in edge.properties.items():
            query += f".property('{key}', '{value}')"

    return query


def V(label: str, property_key: str, property_value: str) -> str:

    has_label = f"hasLabel('{label}')"
    has_property = f"has('{property_key}', '{property_value}')"

    _filter = f"{has_label}.{has_property}"

    return f"g.V().{_filter}"


def updateV(
    label: str,
    property_key: str,
    property_value: str,
    updates: dict
) -> str:

    has_label = f"hasLabel('{label}')"
    has_property = f"has('{property_key}', '{property_value}')"

    query = f"g.V().{has_label}.{has_property}"

    for key, value in updates.items():
        query += f".property('{key}', '{value}')"

    return query


def dropV(label: str, property_key: str, property_value: str) -> str:

    has_label = f"hasLabel('{label}')"

    has_property = f"has('{property_key}', '{property_value}')"

    return f"g.V().{has_label}.{has_property}.drop()"


def E(label: str, from_vertex: dict, to_vertex: dict) -> str:
    from_key, from_value = list(from_vertex.items())[0]
    to_key, to_value = list(to_vertex.items())[0]

    return (
        f"g.V().has('{from_key}', '{from_value}').outE('{label}').inV()"
        f".has('{to_key}', '{to_value}')"
    )


def updateE(
    label: str,
    from_vertex: dict,
    to_vertex: dict,
    updates: dict
) -> str:
    from_key, from_value = list(from_vertex.items())[0]
    to_key, to_value = list(to_vertex.items())[0]

    query = (
        f"g.V().has('{from_key}', '{from_value}').outE('{label}')"
        f".hasLabel('{label}').inV()"
        f".has('{to_key}', '{to_value}')"
    )

    for key, value in updates.items():
        query += f".property('{key}', '{value}')"

    return query


def dropE(label: str, from_vertex: dict, to_vertex: dict) -> str:
    from_key, from_value = list(from_vertex.items())[0]
    to_key, to_value = list(to_vertex.items())[0]

    return (
        f"g.V().has('{from_key}', '{from_value}').outE('{label}').hasLabel('{label}').inV()"
        f".has('{to_key}', '{to_value}').drop()"
    )


def dropAllV():
    return "g.V().drop().iterate()"


def countV():
    return "g.V().count()"
