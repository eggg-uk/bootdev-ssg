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

class LeafNode(HTMLNode):
    def __init__(self,tag,value,children=None,props=None):
        super().__init__(tag,value,None,props)
        
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,value=None,props=None):
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        if tag == None:
        pass