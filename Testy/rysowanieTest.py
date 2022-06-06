import graphviz

# Z tego nie bedziemy korzystac

dot = graphviz.Digraph(comment='The Round Table', format='png')
dot.node('A', 'A')
dot.node('B', 'B')
dot.node('C', 'C')
dot.edges(['AB', 'AC'])
dot.edge('B', 'C', constraint='false')
dot.edge('A', 'B', label='10', len='1.00', color="red")
dot.body.remove(dot.body[2])

print(dot.body[3])
print(dot.source)

dot.render("graf", view=True)