from IPython.display import Image, display
import json

# def print_graph(app):
#     """Utility func to print the ghraph structure"""
#     display(Image(app.get_graph().draw_mermaid_png()))


class Helper:
    """Helper class to use in the graph to process the data"""


    def view_graph(self, app):
        """Utility func to print the ghraph structure"""
        display(Image(app.get_graph().draw_mermaid_png()))


    def monitor(self, data):
        """Utility func to print the data"""
        print("~" * 100)
        print(json.dumps(data, indent=4, ensure_ascii=False))
        print("#" * 100)


