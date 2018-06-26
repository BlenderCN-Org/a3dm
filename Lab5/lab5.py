import bpy
import numpy as np
from enum import Enum
import random
import math
from mathutils import Matrix


scopeCounter = 0
Scopes = []
ActiveScope = 0


def rule( num = 0, ScopeID = ActiveScope):
    #randomness
    val = random.randint(0,9)
    print("random value",val)

    global Scopes
    if(ScopeID > (len(Scopes) - 1) ):
        print("scope ", ScopeID, " not created yet --> addScope(Position, Size)")
        return

    #rule 0
    if(num == 0):

        for shape in Scopes[ScopeID].Shapes :
            val = random.randint(0,9)
            if(val < 3):
                print("randomnes decided NO")
                return

            if(shape.Size[2] >= 3):
                if(shape.Size[2] < 5 ):
                    shape.subdivide_r("z", (2,0.2,2))
                elif (shape.Size[2] >= 5):
                    shape.subdivide_r("z", (2,0.2,2,2,2))



#get the number of scopes created
def scopes():
    print(len(Scopes))


#defining shapes types
class ShapeType(Enum):
    NONE = 0
    CUBE = 1
    CYL = 2

#class that define the shape
class Shape(object):
    id = ""
    Type = ShapeType.NONE
    Pos = []
    Size = []
    meshObj = bpy.ops.object.add()

    #scope informations
    ScopeID = ""

    def __init__(self, id, Type, Pos, Size, S):
        self.id = id
        self.Type = Type
        self.Pos = Pos
        self.Size = Size
        self.ScopeID = S

        if(self.Type == ShapeType.CUBE):
            #adding cube
            bpy.ops.mesh.primitive_cube_add()
            self.meshObj = bpy.context.object
            self.meshObj.name = 'cube'

        elif(self.Type == ShapeType.CYL):
            #adding cylinder
            bpy.ops.mesh.primitive_cylinder_add()
            self.meshObj = bpy.context.object
            self.meshObj.name = 'cyl'

        else:
            print("not identified shape ")
            return
        self.update()

    #update the position and size when there are some changes
    def update(self):
        global Scopes
        P = Scopes[self.ScopeID].P
        # bpy.ops.transform.resize(value=(self.Size[0], self.Size[1], self.Size[2]))
        self.meshObj.scale = (self.Size[0], self.Size[1], self.Size[2])
        self.meshObj.location = (self.Pos[0] + P[0], self.Pos[1] + P[1], self.Pos[2] + P[2])
        print("update position of ", self.id,"  in position :", self.Pos, "  and with size", self.Size)

    #translate the object
    def translate(self, tx, ty, tz):
        self.Pos[0] = self.Pos[0] + tx
        self.Pos[1] = self.Pos[1] + ty
        self.Pos[2] = self.Pos[2] + tz
        self.update()

    #resize the object
    def resize(self, sx, sy, sz):
        self.Size = (sx,sy,sz)
        self.update()

    #scale object functions
    def scale_x(self, sx):
        self.Size[0] = self.Size[0]*sx
        self.update()
    def scale_y(self, sy):
        self.Size[1] = self.Size[1]*sy
        self.update()
    def scale_z(self, sz):
        self.Size[2] = self.Size[2]*sz
        #to keep object on the ground
        self.Pos[2] = self.Pos[2]*sz
        self.update()
    def scale(self, sx, sy, sz):
        self.scale_x(sx)
        self.scale_y(sy)
        self.scale_z(sz)
        self.update()

    #rotate object
    def rotate(self, rx,ry,rz):
        self.meshObj.rotation_euler = (radians(rx), radians(ry), radians(rz))

    #subdivide
    def subdivide(self, coord, listDiv ):
        if(self.Type == ShapeType.NONE ):
            return
        global Scopes
        numDiv = len(listDiv)
        #remove old object
        for o in bpy.data.objects:
            o.select = False
        self.meshObj.select = True
        bpy.ops.object.delete()
        #not allowing to split cylinder in direction different then z
        if(self.Type == ShapeType.CYL):
            if(coord != "z"):
                print(" can't split the cylinder in this dimension")
                return
        #variables for the loop
        p = listDiv[i]
        s2 = 0
        for i in range(numDiv):
            s = listDiv[i]
            if(i != numDiv-1):
                s2 = listDiv[i+1]
            else:
                s2 = 0
            print("size ", s)
            print("position given ", p, " on coordinate", coord , " , original position :",self.Pos)
            if(coord == "x"):
                if(self.Type == ShapeType.CUBE):
                    Scopes[self.ScopeID].addCube( (self.Pos[0] + p, self.Pos[1], self.Pos[2]), ( s, self.Size[1], self.Size[2]))
                elif(self.Type == ShapeType.CYL):
                    Scopes[self.ScopeID].addCyl( (self.Pos[0] + p , self.Pos[1], self.Pos[2]), ( s, self.Size[1], self.Size[2]))
            if(coord == "y"):
                if(self.Type == ShapeType.CUBE):
                    Scopes[self.ScopeID].addCube( (self.Pos[0], self.Pos[1] + p, self.Pos[2]), (self.Size[0], s, self.Size[2]))
                elif(self.Type == ShapeType.CYL):
                    Scopes[self.ScopeID].addCyl( (self.Pos[0], self.Pos[1] + p, self.Pos[2]), (self.Size[0], s, self.Size[2]))
            if(coord == "z"):
                if(self.Type == ShapeType.CUBE):
                    Scopes[self.ScopeID].addCube( (self.Pos[0], self.Pos[1], p), (self.Size[0], self.Size[1], s))
                elif(self.Type == ShapeType.CYL):
                    Scopes[self.ScopeID].addCyl( (self.Pos[0], self.Pos[1], self.Pos[2] + p), (self.Size[0], self.Size[1], s))
            p = p + s + s2
        self.Type = ShapeType.NONE


    def subdivide_r(self, coord, listDiv ):
        if(self.Type == ShapeType.NONE ):
            return
        global Scopes
        numDiv = len(listDiv)
        #remove old object
        for o in bpy.data.objects:
            o.select = False
        self.meshObj.select = True
        bpy.ops.object.delete()
        #not allowing to split cylinder in direction different then z
        if(self.Type == ShapeType.CYL):
            if(coord != "z"):
                print(" can't split the cylinder in this dimension")
                return
        #variables for the loop
        totDiv = 0
        for i in range(numDiv):
            totDiv = totDiv + listDiv[i]
        p = 0
        s2 = 0
        for i in range(numDiv):
            s = listDiv[i]
            if(i != numDiv-1):
                s2 = listDiv[i+1]
            else:
                s2 = 0
            print("position given ", p, " on coordinate", coord , " , original position :",self.Pos)
            if(coord == "x"):
                s = (self.Size[1]/totDiv)*s
                s2 = (self.Size[1]/totDiv)*s2
                if(self.Type == ShapeType.CUBE):
                    Scopes[self.ScopeID].addCube( (self.Pos[0] + p, self.Pos[1], self.Pos[2]), ( s, self.Size[1], self.Size[2]))
                elif(self.Type == ShapeType.CYL):
                    Scopes[self.ScopeID].addCyl( (self.Pos[0] + p , self.Pos[1], self.Pos[2]), ( s, self.Size[1], self.Size[2]))
            if(coord == "y"):
                s = (self.Size[1]/totDiv)*s
                s2 = (self.Size[1]/totDiv)*s2
                if(self.Type == ShapeType.CUBE):
                    Scopes[self.ScopeID].addCube( (self.Pos[0], self.Pos[1] + p, self.Pos[2]), (self.Size[0], s, self.Size[2]))
                elif(self.Type == ShapeType.CYL):
                    Scopes[self.ScopeID].addCyl( (self.Pos[0], self.Pos[1] + p, self.Pos[2]), (self.Size[0], s, self.Size[2]))
            if(coord == "z"):
                s = (self.Size[2]/totDiv)*s
                s2 = (self.Size[2]/totDiv)*s2
                if(self.Type == ShapeType.CUBE):
                    Scopes[self.ScopeID].addCube( (self.Pos[0], self.Pos[1], self.Pos[2] + p), (self.Size[0], self.Size[1], s))
                elif(self.Type == ShapeType.CYL):
                    Scopes[self.ScopeID].addCyl( (self.Pos[0], self.Pos[1], self.Pos[2] + p), (self.Size[0], self.Size[1], s))
            p = p + s + s2

        self.Type = ShapeType.NONE


    def info(self):
        print("**** Shape ", self.Type)
        print("     con id : ", id)
        print("     posizione relativa : ", Pos[0], Pos[1], Pos[2], "  posizione assoluta: ", Pos[0] + P[0], Pos[1] + P[1], Pos[2] + P[2])
        print("     dimensione : ",Size[0], Size[1], Size[2])


#class scope as container of shapes
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

    def addCube(self, Pos, Size):
        id = len(self.Shapes)
        cube = Shape(id, ShapeType.CUBE, Pos, Size, self.id)
        self.Shapes.append(cube)
        print("added cube to Shape, the scope :", self.id, " has numShapes: ", len(self.Shapes) )

    def addCyl(self, Pos, Size):
        id = len(self.Shapes)
        cyl = Shape(id, ShapeType.CYL, Pos, Size, self.id)
        self.Shapes.append(cyl)
        print("added cylinder to Shape, the scope :", self.id, " has numShapes: ", len(self.Shapes) )

    def resizeScope(self, sx, sy, sz):
        for s in self.Shapes:
            if(self.Type != ShapeType.NONE):
                s.resize(sx/self.S[0],sy/self.S[1],sz/self.S[2])
        sel.S = (sx,sy,sz)

    def translateScope(self,tx,ty,tz):
        x = self.P[0] + tx
        y = self.P[1] + ty
        z = self.P[2] + tz
        self.P = (x,y,z)
        for s in self.Shapes:
            if(self.Type != ShapeType.NONE):
                s.update()

    def scaleScope(self, sx, sy, sz):
        x = self.S[0]*sx
        y = self.S[1]*sy
        z = self.S[2]*sz
        self.S = (x,y,z)
        for s in self.Shapes:
            if(self.Type != ShapeType.NONE):
                s.scale(sx,sy,sz)

    def subdivideScope(self, coord, listDiv):
        for s in self.Shapes:
            if(self.Type != ShapeType.NONE):
                s.subdivide(coord, listDiv)

    def subdivideScope_r(self, coord, listDiv):
        for s in self.Shapes:
            if(self.Type != ShapeType.NONE):
                s.subdivide_r(coord, listDiv)


    def info(self):
        print("**** scope ", self.id )
        print("     posizione = ", self.P)
        print("     scaling = ", self.S)
        print("     x ax = ", self.x)
        print("     y ax = ", self.y)
        print("     z ax = ", self.z)
        print("     numero di shapes : ", len(self.Shapes))

def addScope(px=0,py=0,pz=0, sx=3,sy=3,sz=3):
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

def translateScope(tx, ty, tz, ScopeID=ActiveScope):
    global Scopes
    if(ScopeID > (len(Scopes) - 1) ):
        print("scope ", ScopeID, " not created yet --> addScope(Position, Size)")
        return
    Scopes[ScopeID].translateScope(tx,ty,tz)

def scaleScope(sx, sy, sz, ScopeID=ActiveScope):
    global Scopes
    if(ScopeID > (len(Scopes) - 1) ):
        print("scope ", ScopeID, " not created yet --> addScope(Position, Size)")
        return
    Scopes[ScopeID].scaleScope(sx,sy,sz)

def subdivide(ShapeID, coord, listDiv, ScopeID=ActiveScope):
    print("subdivide scope , ", ScopeID)
    global Scopes
    if(ScopeID > (len(Scopes) - 1) ):
        print("scope ", ScopeID, " not created yet --> addScope(Position, Size)")
        return
    print("subdivide scope , ", ScopeID)
    Scopes[ScopeID].Shapes[ShapeID].subdivide(coord, listDiv)
    # for s in Scopes[ScopeID].Shapes:
    #     print("trying to subdivide the shape ",s)
    #     s.subdivide(coord, listDiv)

def subdivide_r(ShapeID, coord, listDiv, ScopeID=ActiveScope):
    print("subdivide scope , ", ScopeID)
    global Scopes
    if(ScopeID > (len(Scopes) - 1) ):
        print("scope ", ScopeID, " not created yet --> addScope(Position, Size)")
        return
    print("subdivide scope , ", ScopeID)
    Scopes[ScopeID].Shapes[ShapeID].subdivide_r(coord, listDiv)

def addCube(px=0, py=0, pz=1, sx=1, sy=1, sz=1, ScopeID=ActiveScope):
    global Scopes
    if(ScopeID > (len(Scopes) - 1) ):
        print("scope ", ScopeID, " not created yet --> addScope(Position, Size)")
        return
    pos = (px,py,pz)
    size = (sx,sy,sz)
    Scopes[ScopeID].addCube(pos,size)

def addCyl(px=0, py=0, pz=1, sx=1, sy=1, sz=1, ScopeID=ActiveScope):
    global Scopes
    if(ScopeID > (len(Scopes) - 1) ):
        print("scope ", ScopeID, " not created yet --> addScope(Position, Size)")
        return
    pos = (px,py,pz)
    size = (sx,sy,sz)
    Scopes[ScopeID].addCyl(pos,size)



#is not a real pop but select a scope to use, and in the case return it too
def pop( ScopeID):
    if(ScopeID > (len(Scopes) - 1) ):
        print("scope ", ScopeID, " not created yet --> addScope(Position, Size)")
    else:
        global ActiveScope
        ActiveScope = ScopeID
        print("pop: active scope :",ScopeID)
        return Scopes[ScopeID]

def status():
    for s in range(len(Scopes)):
        Scopes[s].info()



def main():
    clear()
    scope = addScope(0,0,0, 3,3,3)
    scope.addCube((0,0,3),(3,3,3))

    pos = [0,0,2]
    size = [2,2,2]
    scope.addCube(pos,size)
    pos = [2,2,5]
    size = [1,1,5]
    scope.addCube(pos,size)
    pos = [1,1,4]
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
