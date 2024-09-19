from gremlin_query import addE, addV, dropAllV
from server import execute_batch

from gremlin_query.edge import Edge
from gremlin_query.vertex import Vertex

# =================================================


if __name__ == "__main__":

    # Vetex
    marcio = Vertex(label="Marcio", properties={"Name": "Marcio"})
    lucas = Vertex(label="Lucas", properties={"Name": "Lucas"})
    rafael = Vertex(label="Rafael", properties={"Name": "Rafael"})
    felipe = Vertex(label="Felipe", properties={"Name": "Felipe"})
    giovana = Vertex(label="Giovana", properties={"Name": "Giovana"})
    vw_polo = Vertex(label="VW Polo", properties={"Model": "VW Polo"})
    civic = Vertex(label="Civic", properties={"Model": "Civic"})

    # Marcio Edges
    marcio_lucas = Edge(
        label="Friend",
        from_vertex=marcio,
        to_vertex=lucas,
        properties={
            "Since": "2017"
        }
    )

    marcio_rafael = Edge(
        label="Friend",
        from_vertex=marcio,
        to_vertex=rafael,
        properties={
            "Since": "2016"
        }
    )

    marcio_felipe = Edge(
        label="Friend",
        from_vertex=marcio,
        to_vertex=felipe,
        properties={
            "Since": "2016"
        }
    )

    marcio_giovana = Edge(
        label="Friend",
        from_vertex=marcio,
        to_vertex=giovana,
        properties={
            "Since": "2024"
        }
    )

    # Lucas Edges
    lucas_marcio = Edge(
        label="Friend",
        from_vertex=lucas,
        to_vertex=marcio,
        properties={
            "Since": "2017"
        }
    )

    lucas_rafael = Edge(
        label="Friend",
        from_vertex=lucas,
        to_vertex=rafael,
        properties={
            "Since": "2006"
        }
    )

    lucas_felipe = Edge(
        label="Friend",
        from_vertex=lucas,
        to_vertex=felipe,
        properties={
            "Since": "2017"
        }
    )

    lucas_giovana = Edge(
        label="Friend",
        from_vertex=lucas,
        to_vertex=giovana,
        properties={
            "Since": "2024"
        }
    )

    lucas_vw_polo = Edge(
        label="Has",
        from_vertex=lucas,
        to_vertex=vw_polo,
        properties={
            "Since": "2024"
        }
    )

    # Rafael Edges
    rafael_marcio = Edge(
        label="Friend",
        from_vertex=rafael,
        to_vertex=marcio,
        properties={
            "Since": "2016"
        }
    )

    rafael_lucas = Edge(
        label="Friend",
        from_vertex=rafael,
        to_vertex=lucas,
        properties={
            "Since": "2006"
        }
    )

    rafael_felipe = Edge(
        label="Friend",
        from_vertex=rafael,
        to_vertex=felipe,
        properties={
            "Since": "2016"
        }
    )

    rafael_giovana = Edge(
        label="Boyfriend",
        from_vertex=rafael,
        to_vertex=giovana,
        properties={
            "Since": "2024"
        }
    )

    rafael_civic = Edge(
        label="Has",
        from_vertex=rafael,
        to_vertex=civic,
        properties={
            "Since": "2024"
        }
    )

    # Felipe Edges
    felipe_marcio = Edge(
        label="Friend",
        from_vertex=felipe,
        to_vertex=marcio,
        properties={
            "Since": "2016"
        }
    )

    felipe_lucas = Edge(
        label="Friend",
        from_vertex=felipe,
        to_vertex=lucas,
        properties={
            "Since": "2017"
        }
    )

    felipe_rafael = Edge(
        label="Friend",
        from_vertex=felipe,
        to_vertex=rafael,
        properties={
            "Since": "2016"
        }
    )

    felipe_giovana = Edge(
        label="Friend",
        from_vertex=felipe,
        to_vertex=giovana,
        properties={
            "Since": "2024"
        }
    )

    # Giovana Edges
    giovana_marcio = Edge(
        label="Friend",
        from_vertex=giovana,
        to_vertex=marcio,
        properties={
            "Since": "2024"
        }
    )

    giovana_lucas = Edge(
        label="Friend",
        from_vertex=giovana,
        to_vertex=lucas,
        properties={
            "Since": "2024"
        }
    )

    giovana_rafael = Edge(
        label="Girlfriend",
        from_vertex=giovana,
        to_vertex=rafael,
        properties={
            "Since": "2024"
        }
    )

    giovana_felipe = Edge(
        label="Friend",
        from_vertex=giovana,
        to_vertex=felipe,
        properties={
            "Since": "2024"
        }
    )

    queries = [
        # cleanning database
        dropAllV(),

        # adding vertexes
        addV(marcio),
        addV(lucas),
        addV(rafael),
        addV(felipe),
        addV(giovana),
        addV(vw_polo),
        addV(civic),

        # adding marcio edges
        addE(marcio_lucas),
        addE(marcio_rafael),
        addE(marcio_felipe),
        addE(marcio_giovana),

        # adding lucas edges
        addE(lucas_marcio),
        addE(lucas_rafael),
        addE(lucas_felipe),
        addE(lucas_giovana),
        addE(lucas_vw_polo),

        # adding rafael edges
        addE(rafael_marcio),
        addE(rafael_lucas),
        addE(rafael_felipe),
        addE(rafael_giovana),
        addE(rafael_civic),

        # adding felipe edges
        addE(felipe_marcio),
        addE(felipe_lucas),
        addE(felipe_rafael),
        addE(felipe_giovana),

        # adding giovana edges
        addE(giovana_marcio),
        addE(giovana_lucas),
        addE(giovana_rafael),
        addE(giovana_felipe),
    ]

    for result in execute_batch(queries):
        print(result)
