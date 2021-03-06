import bpy
import numpy as np
from time import time




def ex4(me, n):

    me_vertices = []
    for v in me.vertices:
        me_vertices.append((v.co[0],v.co[1],v.co[2]))
    me_faces = []
    for f in me.polygons:
        me_faces.append(f.vertices[:])

    #initliaization
    vertices_sub = me_vertices
    faces_sub = me_faces
    vertices_cat = me_vertices
    faces_cat = me_faces

    for i in range(n):
        print(" iteration ", i)
        new_me_sub = bpy.data.meshes.new("new_me_sub")
        ob_sub = bpy.data.objects.new("new_me_sub",new_me_sub)
        new_me_sub.from_pydata(vertices_sub,[],faces_sub)

        vertices_sub, faces_sub = simpleSub(new_me_sub)

        new_me_cat = bpy.data.meshes.new("new_me_cat")
        ob_cat = bpy.data.objects.new("new_me_cat",new_me_cat)
        new_me_cat.from_pydata(vertices_cat,[],faces_cat)

        vertices_cat, faces_cat = catClarS(new_me_cat)

    return(vertices_sub,vertices_cat,faces_sub)

    # final_vertices = vertices_cat[:]

    # print("value t = ",t )
    # for v in range(len(vertices_sub)):
    #      final_vertices.append((t*vertices_sub[v][0]+(1-t)*vertices_cat[v][0],t*vertices_sub[v][1]+(1-t)*vertices_cat[v][1],t*vertices_sub[v][2]+(1-t)*vertices_cat[v][2]))




# def ex3(me, n, t):
#
#     me_vertices = []
#     for v in me.vertices:
#         me_vertices.append((v.co[0],v.co[1],v.co[2]))
#     me_faces = []
#     for f in me.polygons:
#         me_faces.append(f.vertices[:])
#
#     #initliaization
#     vertices_sub = me_vertices
#     faces_sub = me_faces
#     vertices_cat = me_vertices
#     faces_cat = me_faces
#
#     for i in range(n):
#         print(" iteration ", i)
#         new_me_sub = bpy.data.meshes.new("new_me_sub")
#         ob_sub = bpy.data.objects.new("new_me_sub",new_me_sub)
#         new_me_sub.from_pydata(vertices_sub,[],faces_sub)
#
#         vertices_sub, faces_sub = simpleSub(new_me_sub)
#
#         new_me_cat = bpy.data.meshes.new("new_me_cat")
#         ob_cat = bpy.data.objects.new("new_me_cat",new_me_cat)
#         new_me_cat.from_pydata(vertices_cat,[],faces_cat)
#
#         vertices_cat, faces_cat = catClarS(new_me_cat)
#
#
#     final_vertices = vertices_cat[:]
#
#     print("value t = ",t )
#     for v in range(len(vertices_sub)):
#          final_vertices.append((t*vertices_sub[v][0]+(1-t)*vertices_cat[v][0],t*vertices_sub[v][1]+(1-t)*vertices_cat[v][1],t*vertices_sub[v][2]+(1-t)*vertices_cat[v][2]))
#
#
#     me = bpy.data
#
#     bpy.ops.object.delete()
#
#
#     me = bpy.data.meshes.new("final_me")
#     ob = bpy.data.objects.new("final_me",me)
#     ob.location = bpy.context.scene.cursor_location
#     bpy.context.scene.objects.link(ob)
#     me.from_pydata(final_vertices,[],faces_sub)
#     me.update(calc_edges = True)
#     bpy.data.objects["final_me"].select = True
#     bpy.context.scene.objects.active = bpy.data.objects["final_me"]
#
#
#     #return(final_vertices, faces_sub)

def simpleSub (me) :
    new_vertices = []
    new_faces = []

    facePoint = []
    edgePoint = []
    baricenterPoint = []

    edgeN = computeEdgeNeighbour(me)


    #face points
    numFaces = len(me.polygons)
    for f in range(len(me.polygons)):
        facePoint.append (computeFacePoint(me,f))
        new_vertices.append((facePoint[f][0],facePoint[f][1],facePoint[f][2]))



    edgeMidPoint = []
    edgeMidPoint = computeEdgeMidPoint(me)

    #edge points with borders
    numEdges = len(me.edges)
    for e in range(len(me.edges)):
        vl = []
        epoint = []
        i = 0
        sumx = 0
        sumy = 0
        sumz = 0

        for f in range(len(edgeN[e])) :
            face = edgeN[e][f]
            vl.append(facePoint[face])

        verA = me.edges[e].vertices[0]
        verB = me.edges[e].vertices[1]
        A = me.vertices[verA].co
        B = me.vertices[verB].co
        vl.append((A[0],A[1],A[2]))
        vl.append((B[0],B[1],B[2]))
        for v in range(len(vl)):
            i = i + 1
            sumx = sumx + vl[v][0]
            sumy = sumy + vl[v][1]
            sumz = sumz + vl[v][2]
        epoint = (r(sumx/i), r(sumy/i), r(sumz/i))
        edgePoint.append(epoint)
        new_vertices.append((edgePoint[e][0], edgePoint[e][1], edgePoint[e][2]))


    #old vertices
    for v in range(len(me.vertices)) :
        new_vertices.append((me.vertices[v].co[0], me.vertices[v].co[1], me.vertices[v].co[2]))





    adjacentEdges = []
    adjacentEdges = edgesCloseToVertex(me)

    adjacentFaces = []
    adjacentFaces = facesCloseToVertex(me)

    #creating the face
    for f in range(len(me.polygons)):
        #face vertex
        f3 = f

        for v in range(len(me.polygons[f].vertices)):

            face = []

            f1 = 0
            f2 = 0
            f4 = 0

            a = me.polygons[f].vertices[v]


            #v of baricenter vertices
            f1 = numFaces + numEdges + a


            #first edge vertex
            if (v != (len(me.polygons[f].vertices) - 1)):
                b = me.polygons[f].vertices[v+1]
            else :
                b = me.polygons[f].vertices[0]

            for e in adjacentEdges[a]:
                edgeV1 = me.edges[e].vertices[0]
                edgeV2 = me.edges[e].vertices[1]
                if ((edgeV1 == a and edgeV2 == b) or (edgeV1 == b and edgeV2== a)) :
                    f2 = numFaces + e


            #second edge vertex
            if(v != 0):
                b = me.polygons[f].vertices[v-1]
            else:
                b = me.polygons[f].vertices[len(me.polygons[f].vertices)-1]
            for e in adjacentEdges[a]:
                edgeV1 = me.edges[e].vertices[0]
                edgeV2 = me.edges[e].vertices[1]
                if ((edgeV1 == a and edgeV2 == b) or (edgeV1 == b and edgeV2== a)) :
                    f4 = numFaces + e

            face = (f1,f2,f3,f4)
            new_faces.append(face)



    return new_vertices,new_faces



def ex2(me):

    coords, faces = catClarS(me)
    me = bpy.data

    bpy.ops.object.delete()


    me = bpy.data.meshes.new("new_me")
    ob = bpy.data.objects.new("new_me",me)
    ob.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(ob)
    me.from_pydata(coords,[],faces)
    me.update(calc_edges = True)
    bpy.data.objects["new_me"].select = True
    bpy.context.scene.objects.active = bpy.data.objects["new_me"]





def catClarS (me) :
    new_vertices = []
    new_faces = []

    facePoint = []
    edgePoint = []
    baricenterPoint = []

    edgeN = computeEdgeNeighbour(me)


    #face points
    numFaces = len(me.polygons)
    for f in range(len(me.polygons)):
        facePoint.append (computeFacePoint(me,f))
        new_vertices.append((facePoint[f][0],facePoint[f][1],facePoint[f][2]))


    #edge points with borders
    numEdges = len(me.edges)
    for e in range(len(me.edges)):
        vl = []
        epoint = []
        i = 0
        sumx = 0
        sumy = 0
        sumz = 0

        for f in range(len(edgeN[e])) :
            face = edgeN[e][f]
            vl.append(facePoint[face])

        verA = me.edges[e].vertices[0]
        verB = me.edges[e].vertices[1]
        A = me.vertices[verA].co
        B = me.vertices[verB].co
        vl.append((A[0],A[1],A[2]))
        vl.append((B[0],B[1],B[2]))
        for v in range(len(vl)):
            i = i + 1
            sumx = sumx + vl[v][0]
            sumy = sumy + vl[v][1]
            sumz = sumz + vl[v][2]
        epoint = (r(sumx/i), r(sumy/i), r(sumz/i))
        edgePoint.append(epoint)
        new_vertices.append((edgePoint[e][0], edgePoint[e][1], edgePoint[e][2]))







    adjacentEdges = []
    adjacentEdges = edgesCloseToVertex(me)

    adjacentFaces = []
    adjacentFaces = facesCloseToVertex(me)

    edgeMidPoint = []
    edgeMidPoint = computeEdgeMidPoint(me)


    #compute baricenter
    numVert = len (me.vertices)
    for v in range( len (me.vertices)):

        P = me.vertices[v].co

        n = 0
        Fx = 0
        Fy = 0
        Fz = 0



        for f in adjacentFaces[v] :
            n = n + 1
            Fx = Fx + facePoint[f][0]
            Fy = Fy + facePoint[f][1]
            Fz = Fz + facePoint[f][2]
        F = (Fx/n, Fy/n, Fz/n)

        n = 0
        Rx = 0
        Ry = 0
        Rz = 0
        for e in  adjacentEdges[v] :
            n = n + 1
            Rx = Rx + edgeMidPoint[e][0]
            Ry = Ry + edgeMidPoint[e][1]
            Rz = Rz + edgeMidPoint[e][2]
        R = (Rx/n, Ry/n, Rz/n)

        Bx = (F[0] + 2*R[0] + (n - 3)*P[0])/n
        By = (F[1] + 2*R[1] + (n - 3)*P[1])/n
        Bz = (F[2] + 2*R[2] + (n - 3)*P[2])/n

        baricenterPoint.append ((Bx,By,Bz))
        new_vertices.append((baricenterPoint[v][0], baricenterPoint[v][1], baricenterPoint[v][2]))



    #creating the face
    for f in range(len(me.polygons)):
        #face vertex
        f3 = f

        for v in range(len(me.polygons[f].vertices)):

            face = []

            f1 = 0
            f2 = 0
            f4 = 0


            a = me.polygons[f].vertices[v]


            #v of baricenter vertices
            f1 = numFaces + numEdges + a


            #first edge vertex
            if (v != (len(me.polygons[f].vertices) - 1)):
                b = me.polygons[f].vertices[v+1]
            else :
                b = me.polygons[f].vertices[0]

            for e in adjacentEdges[a]:
                edgeV1 = me.edges[e].vertices[0]
                edgeV2 = me.edges[e].vertices[1]
                if ((edgeV1 == a and edgeV2 == b) or (edgeV1 == b and edgeV2== a)) :
                    f2 = numFaces + e



            #second edge vertex
            if(v != 0):
                b = me.polygons[f].vertices[v-1]
            else:
                b = me.polygons[f].vertices[len(me.polygons[f].vertices)-1]
            for e in adjacentEdges[a]:
                edgeV1 = me.edges[e].vertices[0]
                edgeV2 = me.edges[e].vertices[1]
                if ((edgeV1 == a and edgeV2 == b) or (edgeV1 == b and edgeV2== a)) :
                    f4 = numFaces + e

            face = (f1,f2,f3,f4)
            new_faces.append(face)


    return new_vertices,new_faces





def computeEdgeMidPoint(me):
    sumx = 0
    sumy = 0
    sumz = 0
    edgeMidPoint = []
    for e in me.edges:
        a = me.vertices[e.vertices[0]].co
        b = me.vertices[e.vertices[1]].co
        sumx = (a[0] + b[0])
        sumy = (a[1] + b[1])
        sumz = (a[2] + b[2])
        edgeMidPoint.append((r(sumx/2), r(sumy/2), r(sumz/2)))
    return edgeMidPoint

def edgesCloseToVertex(me):
    adjacentEdges = []
    for v in range (len (me.vertices)):
        closeEdges = []
        for e in range(len(me.edges)):
             if (me.edges[e].vertices[0] == v or me.edges[e].vertices[1] == v ) :
                 closeEdges.append(e)
        adjacentEdges.append(closeEdges)
    return adjacentEdges

def facesCloseToVertex(me):
    adjacentFaces = []
    for v in range (len (me.vertices)):
        closeFaces = []
        for f in range(len(me.polygons)):
            for vi in range(len(me.polygons[f].vertices)):
                if (me.polygons[f].vertices[vi] == v):
                    closeFaces.append(f)
        adjacentFaces.append(closeFaces)
    return adjacentFaces


def computeFacePoint (me, f):
    i = 0
    sumx = 0
    sumy = 0
    sumz = 0
    for v in me.polygons[f].vertices:
        sumx = sumx + me.vertices[v].co[0]
        sumy = sumy + me.vertices[v].co[1]
        sumz = sumz + me.vertices[v].co[2]
        i = i + 1
    facePointCo = (r(sumx/i), r(sumy/i), r(sumz/i))
    return facePointCo

# def computeEdgePoint (me, e, facePoint1, facePoint2):
#     edgePoint = []
#     i = 4
#     sumx = 0
#     sumy = 0
#     sumz = 0
#     verA = me.edges[e].vertices[0]
#     verB = me.edges[e].vertices[1]
#     A = me.vertices[verA].co
#     B = me.vertices[verB].co
#     C = facePoint1
#     D = facePoint2
#     sumx = A[0] + B[0] + C[0] + D[0]
#     sumy = A[1] + B[1] + C[1] + D[1]
#     sumz = A[2] + B[2] + C[2] + D[2]
#     edgePoint = (r(sumx/i), r(sumy/i), r(sumz/i))
#     return edgePoint




def computeEdgeNeighbour(me):
    neighbors = []
    for e in range(len(me.edges)):
        edgeNeigh = []
        a = me.edges[e].vertices[0]
        b = me.edges[e].vertices[1]
        for f in range(len(me.polygons)):
            hasA = False
            hasB = False
            for ver in range(len(me.polygons[f].vertices)):
                if ( me.polygons[f].vertices[ver] == a ):
                    hasA = True
                if( me.polygons[f].vertices[ver] == b):
                    hasB = True
            if (hasA & hasB ):
                edgeNeigh.append(f)
        neighbors.append(edgeNeigh)
    return neighbors


def r(a) :
    return int(a*1000 + 0.5)/1000.0

def processa_malla(me):
    print('Name of the mesh: %s' % (me.name))
    print(' V= %d' % (len(me.vertices)))
    print(' E= %d' % (len(me.edges)))
    print(' F= %d' % (len(me.polygons)))

    print('Vertex list:')
    for i in range(len(me.vertices)):
        coord=me.vertices[i].co
        print(i, ":", coord[0], coord[1], coord[2])

    print('Face list:')
    for i in range(len(me.polygons)):
        print(i, ":", me.polygons[i].vertices[:])
    print('Equiv________________')
    for poly in me.polygons:
        print("Polygon index: %d, length: %d" % (poly.index, poly.loop_total))
        for loop_index in poly.loop_indices:
#equivalent to
#       for loop_index in range(poly.loop_start, poly.loop_start + poly.loop_total):
            print("    Vertex: %d" % me.loops[loop_index].vertex_index)
#can also be obtained from poly.vertices[] directly:
#       for v in poly.vertices[:]:
#           print("    Vertex: %d" % v)
    print("Loops:")
    for i in me.loops:
        print(i.vertex_index)

    print("Edge list :")
    for i in range(len(me.edges)):
        print(i, ":", me.edges[i].vertices[:])
    print("\nEnd of Data for mesh "+me.name+"\n\n")


def r(a) :
    return int(a*1000 + 0.5)/1000.0

def main(n=2):

    # Retrieve the active object (the last one selected)
    ob = bpy.data.scenes['Scene'].objects.active

    # If we are in edit mode, return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Retrieve the mesh data
    mesh = ob.data

    # Get current time
    t = time()

    coord1,coord2,face=ex4(mesh,n)

    bpy.ops.object.delete()

    me=bpy.data.meshes.new("Result")
    ob2=bpy.data.objects.new("Result",me)
    ob2.location=bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(ob2)
    me.from_pydata(coord1,[],face)
    me.update(calc_edges=True)
    bpy.data.objects["Result"].select = True
    bpy.context.scene.objects.active = bpy.data.objects["Result"]

    def interpolation(t):

        COORD=coord1[:]

        for i in range(len(coord1)):
            COORD[i]=((1-t)*coord1[i][0]+t*coord2[i][0],(1-t)*coord1[i][1]+t*coord2[i][1],(1-t)*coord1[i][2]+t*coord2[i][2])

        return(COORD)

    def Callback(scene):
        #We get the start and stop frames of the animation
        strt=scene.frame_start
        end = scene.frame_end
        #We compute the step
        num=end-strt
        frame = scene.frame_current
        step = float(frame-strt)/num
        #step is between 0 & 1
        COORD=interpolation(step)

        # Retrieve the active object (the last one selected)
        ob = bpy.data.scenes['Scene'].objects.active

        # If we are in edit mode, return to object mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # Retrieve the mesh data
        mesh = ob.data
        bpy.data.meshes.remove(mesh)
        bpy.ops.object.delete()

        me=bpy.data.meshes.new("Result")
        ob2=bpy.data.objects.new("Result",me)
        ob2.location=bpy.context.scene.cursor_location
        bpy.context.scene.objects.link(ob2)
        me.from_pydata(COORD,[],face)
        me.update(calc_edges=True)
        bpy.data.objects["Result"].select = True
        bpy.context.scene.objects.active = bpy.data.objects["Result"]



    bpy.data.scenes['Scene'].frame_end=100
    bpy.data.scenes['Scene'].frame_current=0

    bpy.app.handlers.frame_change_pre.clear()
    bpy.app.handlers.frame_change_pre.append(Callback)


    print("Script took %6.2f secs.\n\n"%(time()-t))
