from sqlalchemy_schemadisplay import create_schema_graph
from app import create_app
from app.extensions import db

app = create_app()

with app.app_context():
    graph = create_schema_graph(
        metadata=db.metadata,
        show_datatypes=False,
        show_indexes=False,
        rankdir='TB',
        concentrate=False
    )
    graph.write_png('er_diagram.png')
    graph.write_svg('er_diagram.svg')