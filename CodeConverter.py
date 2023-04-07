from Mesh import Mesh


def CPP(Mesh):
    vertexs = Mesh.getVertexs()
    output = []
    output.append('void ' + formatName(Mesh.getName())+'(){\n')
    output.append(' \n')
    for vertex in vertexs:
        x, y, z = vertex
        output.append('{0, 0, 0xff7f0000,({},{},{})},\n'.format(x, y, z))
    output.append('\n')
    output.append('}\n')
    return output


def formatName(name):
    return name.replace('.', '_')
