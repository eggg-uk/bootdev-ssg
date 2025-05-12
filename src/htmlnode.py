class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props
    
    def to_html(self):
        raise exception(NotImplementedError)
    
    def props_to_html(self):
        html_props = ""
        for key,value in self.props.items():
            html_props = html_props + f' {key}="{value}"'
            # print(html_props)
        return html_props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self,other):
        if self.tag == other.tag and self.value == other.value and self.children==other.children and self.props == other.props:
            return True
        else: return False
