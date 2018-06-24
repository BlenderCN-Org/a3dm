import bpy
import numpy as np
from enum import Enum
import math
from mathutils import Matrix


scopeCounter = 0
Scopes = []

def scopes():
    print(len(Scopes))

def createCube(sx, sy, sz):
    bpy.ops.mesh.primitive_cube_add()
    # Get the cube object and rename it.
    cube = bpy.context.object
    cube.name = 'cube'
    # Resize the cube.
    bpy.ops.transform.resize(value=(sx, sy, sz))
    # Change the location of the cube.
    cube.location = (0, 0, 0)

def createCylinder(sx,sy,sz):
    bpy.ops.mesh.primitive_cylinder_add()
    cyl = bpy.context.object
    cyl.name = 'cylinder'
    # Resize the cylinder.
    bpy.ops.transform.resize(value=(sx, sy, sz))
    # Change the location of the cylinder.
    cyl.location = (5, 3, 0)

class ShapeType(Enum):
    NONE = 0
    CUBE = 1
    CYL = 2

class Shape(object):
    id = ""
    Type = ShapeType.NONE
    Pos = []
    Size = []
    P = []
    meshObj = bpy.ops.object.add()

    def __init__(self, id, Type, Pos, Size, P ):
        self.id = id
        self.Type = Type
        self.Pos = Pos
        self.Size = Size

        if(self.Type == ShapeType.CUBE):
            #adding cube
            bpy.ops.mesh.primitive_cube_add()
            # Get the cube object and rename it.
            self.meshObj = bpy.context.object
            self.meshObj.name = 'cube'

        elif(self.Type == ShapeType.CYL):
            #adding cylinder
            bpy.ops.mesh.primitive_cylinder_add()
            # Get the cylinder object and rename it.
            self.meshObj = bpy.context.object
            self.meshObj.name = 'cyl'

        else:
            print("not identified shape ")
            return


        # Resize
        bpy.ops.transform.resize(value=(Size[0], Size[1], Size[2]))
        # Change the location
        self.meshObj.location = (Pos[0] + P[0], Pos[1] + P[1], Pos[2] + P[2])

        print("*****creata Shape ", self.Type)
        print("     con id : ", id)
        print("     posizione relativa : ", Pos[0], Pos[1], Pos[2], "  posizione assoluta: ", Pos[0] + P[0], Pos[1] + P[1], Pos[2] + P[2])
        print("     dimensione : ",Size[0], Size[1], Size[2])


class Scope(object):
    id = ""
    #position
    P = []
    #size
    S = []
    #axes
    x = []
    y = []
    z = []

    Shapes = []


    def __init__(self,id, P, S, x , y, z):
        self.id = id
        self.P = P
        self.S = S
        self.x = x
        self.y = y
        self.z = z
        self.Shapes = []


    def info(self):
        print("**** scope ", self.id )
        print("     posizione = ", self.P)
        print("     scaling = ", self.S)
        print("     x ax = ", self.x)
        print("     y ax = ", self.y)
        print("     z ax = ", self.z)
        print("     numero di shapes : ", len(self.Shapes))


    def addCube(self, Pos, Size):
        id = len(self.Shapes)
        cube = Shape(id, ShapeType.CUBE, Pos, Size, self.P)
        self.Shapes.append(cube)
        print("added cube to Shape, now the number of Shape of the ", self.id, " scope is ", len(self.Shapes) )

    def addCyl(self, Pos, Size):
        id = len(self.Shapes)
        cyl = Shape(id, ShapeType.CYL, Pos, Size, self.P)
        self.Shapes.append(cyl)
        print("added cylinder to Shape, now the number of Shape of the ", self.id, " scope is ", len(self.Shapes)  )

    def updatePosition(self):
        for s in self.Shapes:
            s.meshObj.location = (s.Pos[0] + self.P[0], s.Pos[1] + self.P[1], s.Pos[2] + self.P[2])

    def updateScale(self, sx, sy, sz):
        for s in self.Shapes:
            scale_matrix = Matrix.Scale(sx, 4, (1, 0, 0))
            s.meshObj.matrix_world *= scale_matrix
            scale_matrix = Matrix.Scale(sy, 4, (0, 1, 0))
            s.meshObj.matrix_world *= scale_matrix
            scale_matrix = Matrix.Scale(sz, 4, (0, 0, 1))
            s.meshObj.matrix_world *= scale_matrix

            s.meshObj.location = (s.Pos[0] + self.P[0], s.Pos[1] + self.P[1], s.Pos[2]*sz + self.P[2])


    def translateScope(self,tx,ty,tz):
        x = self.P[0] + tx
        y = self.P[1] + ty
        z = self.P[2] + tz
        newPosition = (x,y,z)
        self.P = newPosition
        self.updatePosition()
        print("scope ", self.id, " translated ")

    def scaleScope(self, sx, sy, sz):
        newS = (sx,sy,sz)
        self.S = newS
        self.updateScale(sx,sy,sz)
        print("scope ", self.id, " scaled ")


def scopeInfo(ScopeID):
    global Scopes
    if(ScopeID > (len(Scopes) - 1) ):
        print("scope ", ScopeID, " not created yet --> addScope(Position, Size)")
        return
    Scopes[ScopeID].info()

def addScope(px,py,pz, sx,sy,sz):
    global scopeCounter
    id = scopeCounter
    P = (px,py,pz)
    S = (sx,sy,sz)
    x = [1,0,0]
    y = [0,1,0]
    z = [0,0,1]
    scope = Scope(id,P,S,x,y,z)
    global Scopes
    Scopes.append(scope)
    scopeCounter = scopeCounter + 1;
    return scope

def translateScope(ScopeID, tx, ty, tz):
    global Scopes
    if(ScopeID > (len(Scopes) - 1) ):
        print("scope ", ScopeID, " not created yet --> addScope(Position, Size)")
        return
    Scopes[ScopeID].translateScope(tx,ty,tz)

def scaleScope(ScopeID, sx, sy, sz):
    global Scopes
    if(ScopeID > (len(Scopes) - 1) ):
        print("scope ", ScopeID, " not created yet --> addScope(Position, Size)")
        return
    Scopes[ScopeID].scaleScope(sx,sy,sz)

def addCube(ScopeID, px=0, py=0, pz=0, sx=1, sy=1, sz=1):
    global Scopes
    if(ScopeID > (len(Scopes) - 1) ):
        print("scope ", ScopeID, " not created yet --> addScope(Position, Size)")
        return
    pos = (px,py,pz)
    size = (sx,sy,sz)
    Scopes[ScopeID].addCube(pos,size)

def addCyl(ScopeID, px=0, py=0, pz=0, sx=1, sy=1, sz=1):
    global Scopes
    if(ScopeID > (len(Scopes) - 1) ):
        print("scope ", ScopeID, " not created yet --> addScope(Position, Size)")
        return
    pos = (px,py,pz)
    size = (sx,sy,sz)
    Scopes[ScopeID].addCyl(pos,size)


def main():

    clear()
    pos = [0,0.5,0]
    dimension = [5,5,5]
    scope = addScope(0,0,0, 5, 5,5)

    pos = [1,0,1]
    size = [1,1,1]
    scope.addCube(pos,size)
    pos = [3,3,5]
    size = [1,1,5]
    scope.addCube(pos,size)
    pos = [4,0,4]
    size = [0.5,0.5,4]
    scope.addCube(pos,size)
    pos = [4,4,4]
    size = [1,1,4]
    scope.addCyl(pos,size)

    scope2 = addScope(-6,-6,0, 5, 5,5)

    pos = [1,0,1]
    size = [1,1,1]
    scope2.addCube(pos,size)
    pos = [3,3,5]
    size = [1,1,5]
    scope2.addCube(pos,size)
    pos = [4,0,4]
    size = [0.5,0.5,4]
    scope2.addCube(pos,size)
    pos = [4,4,4]
    size = [1,1,4]
    scope2.addCyl(pos,size)



def clear():
    global scopeCounter
    scopeCounter = 0
    Scopes.clear()
    #remove existing objects
        # select objects by type
    for o in bpy.data.objects:
        if o.type == 'MESH':
            o.select = True
        else:
            o.select = False

    # call the operator once
    bpy.ops.object.delete()





    # # Create a simple cube.
    # bpy.ops.mesh.primitive_cube_add()
    #
    # # Resize the cube.
    # bpy.ops.transform.resize(value=(5, 3, 0.5))
    #
    # # Get the cube object and rename it.
    # cube = bpy.context.object
    # cube.name = 'cube'
    #
    # # Create a simple cylinder.
    # bpy.ops.mesh.primitive_cylinder_add(radius = 1)
    #
    # # Get the cylinder object and rename it.
    # cyl = bpy.context.object
    # cyl.name = 'cylinder'
    #
    # # Change the location of the cylinder.
    # cyl.location = (5, 3, 0)
    #
    # # Create a boolean modifier named 'my_bool_mod' for the cube.
    # mod_bool = cube.modifiers.new('my_bool_mod', 'BOOLEAN')
    # # Set the mode of the modifier to DIFFERENCE.
    # mod_bool.operation = 'DIFFERENCE'
    # # Set the object to be used by the modifier.
    # mod_bool.object = cyl
    #
    #
    # # The modifier_apply function only works on the active object.
    # # Set the cube as the active object.
    # bpy.context.scene.objects.active = cube
    #
    # # Apply the modifier.
    # res = bpy.ops.object.modifier_apply(modifier = 'my_bool_mod')
    #
    # # Delete the cylinder.
    # cyl.select = True
    # bpy.ops.object.delete()


def help():
    print("scopes() : number of all the scopes")
    print("clear() : clear the scene")
    print("main() : precomputed scene")
    print("addScope(ScopeID, Px,Py,Pz,  Sx,Sy,Sz) : create a scope in Position ox,py,pz and Size sx,sy,sz")
    print("addCube(ScopeID, px,py,pz, sx,sy,sz)  addCyl(px,py,pz, sx,sy,sz")
    print("     scope.addCube(Position, Size) scope.addCyl(Position, Size) : to add cube and cylinder")
    print("translateScope(ScopeID, tx,ty,tz) : to translate the scope ")
    print("     scope.translateScope(tx,ty,tz) : to translate the scope ")
    print("scaleScope(ScopeID, sx,sy,sz) : to scale the scope ")
    print("     scope.scaleScope(sx,sy,sz) : to sclae the scope ")
