import rhinoscriptsyntax as rs
import Rhino
import System
import scriptcontext as sc
import math
import random

from math import sin
from math import cos
from math import radians
from math import tan
from math import pi
from math import sqrt
import time



def Parking_Layout(Layout):

    if Layout == 90:
        length = 18
        width = 9
        length_driveway = 24
    
    if Layout == 60:
        length = 10.4
        width = 20.1
        length_driveway = 14.5
    
    if Layout == 45:
        length = 12.7
        width = 19
        length_driveway = 12
    
    if Layout == 30:
        length = 18
        width = 16.8
        length_driveway = 12
    
    angle = radians(90 - Layout)
    
    #parking layout pts
    p1 = rs.AddPoint(0,0,0)
    p2 = rs.AddPoint(length,0-width*tan(angle),0)
    p3 = rs.AddPoint(length,width-width*tan(angle),0)
    p4 = rs.AddPoint(length,width*2-width*tan(angle),0)
    p5 = rs.AddPoint(0,width*2,0)
    p6 = rs.AddPoint(0,width,0)
    p7 = rs.AddPoint(length+length_driveway,0-width*tan(angle),0)
    p8 = rs.AddPoint(length*2+length_driveway,0,0)
    p9 = rs.AddPoint(length*2+length_driveway,width,0)
    p10 = rs.AddPoint(length*2+length_driveway,width*2,0)
    p11 = rs.AddPoint(length+length_driveway,width*2-width*tan(angle))
    p12 = rs.AddPoint(length+length_driveway,width-width*tan(angle))
    
    
    List_Parking = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]
    Line_ParkingLine = rs.AddPolyline([p1,p2,p3,p6,p1])
    Line_ParkingLine2 = rs.AddPolyline([p6,p3,p4,p5,p6])
    Line_ParkingLine3 = rs.AddPolyline([p7,p8,p9,p12,p7])
    Line_ParkingLine4 = rs.AddPolyline([p12,p9,p10,p11,p12])
    
    List_Parking.append(Line_ParkingLine)
    List_Parking.append(Line_ParkingLine2)
    List_Parking.append(Line_ParkingLine3)
    List_Parking.append(Line_ParkingLine4)
    
    Line_HousingPlatform = rs.AddPolyline([p1,p2,p4,p5,p1])
    Line_HousingPlatform2 = rs.AddPolyline([p7,p8,p10,p11,p7])
    
    List_Parking.append(Line_HousingPlatform)
    List_Parking.append(Line_HousingPlatform2)
    
    return List_Parking

def Driveway_Layout(Layout):
    
    if Layout == 90:
        length = 18
        width = 9
        length_driveway = 24
    
    if Layout == 60:
        length = 10.4
        width = 20.1
        length_driveway = 14.5
    
    if Layout == 45:
        length = 12.7
        width = 19
        length_driveway = 12
    
    if Layout == 30:
        length = 18
        width = 16.8
        length_driveway = 12
    
    angle = radians(90 - Layout)
    
    
    List_Driveway = []
    
    #parking layout pts
    pt_driveway1 = rs.AddPoint(length,0-width*tan(angle))
    pt_driveway2 = rs.AddPoint(length+(length_driveway/2),0-width*tan(angle))
    pt_driveway3 = rs.AddPoint(length+length_driveway,0-width*tan(angle))
    pt_driveway4 = rs.AddPoint(length+length_driveway,width-width*tan(angle))
    pt_driveway5 = rs.AddPoint(length+length_driveway,width*2-width*tan(angle))
    pt_driveway6 = rs.AddPoint(length+(length_driveway/2),width*2-width*tan(angle))
    pt_driveway7 = rs.AddPoint(length,width*2-width*tan(angle))
    pt_driveway8 = rs.AddPoint(length,width-width*tan(angle))
    pt_drivewayC = rs.AddPoint(length+(length_driveway/2),width-width*tan(angle))
    
    
    List_Driveway = [pt_driveway1,pt_driveway2,pt_driveway3,pt_driveway4,pt_driveway5,pt_driveway6,pt_driveway7,pt_driveway8,pt_drivewayC]
    
    Line_drivewayLB = rs.AddPolyline([pt_driveway1,pt_driveway2,pt_drivewayC,pt_driveway8,pt_driveway1])
    List_Driveway.append(Line_drivewayLB)
    Line_drivewayRB = rs.AddPolyline([pt_driveway2,pt_driveway3,pt_driveway4,pt_drivewayC,pt_driveway2])
    List_Driveway.append(Line_drivewayRB)
    Line_drivewayRT = rs.AddPolyline([pt_drivewayC,pt_driveway4,pt_driveway5,pt_driveway6,pt_drivewayC])
    List_Driveway.append(Line_drivewayRT)
    Line_drivewayLT = rs.AddPolyline([pt_driveway8,pt_drivewayC,pt_driveway6,pt_driveway7,pt_driveway8])
    List_Driveway.append(Line_drivewayLT)
    Line_drivewayLH = rs.AddPolyline([pt_driveway1,pt_driveway2,pt_driveway6,pt_driveway7,pt_driveway1])
    List_Driveway.append(Line_drivewayLH)
    Line_drivewayRH = rs.AddPolyline([pt_driveway2,pt_driveway3,pt_driveway5,pt_driveway6,pt_driveway2])
    List_Driveway.append(Line_drivewayRH)


    return List_Driveway

def Platform_Layout(Lines,Height):
    Vector_Platformheight = rs.VectorCreate([0,0,Height],[0,0,0])
    Line_Platform = rs.CopyObjects(Lines,Vector_Platformheight)
    return Line_Platform

def Structure_Platform (PlatformLine,Rotation,ScalePoint,height):
    
    list_parkingplatform =[]
    LoftSet = []
    list_parkingplatform.append(PlatformLine)

    for i in range(height):
        
        Scalefactor = math.sqrt(math.pow(1,2)-math.pow(i/(height),2))
        
        if i < 7*height/8:
            Scale = Scalefactor
        else:
            Scale = 1
        ScalePolygon = rs.ScaleObject(list_parkingplatform[-1],ScalePoint,(Scale,Scale,1),True)
        RotatePolygon = rs.RotateObject(ScalePolygon,ScalePoint,Rotation,(0,0,1))
        RotatePolygon = rs.MoveObject(RotatePolygon,(0,0,-1))
        list_parkingplatform.append(RotatePolygon)
        
        
    Top = rs.AddPlanarSrf(list_parkingplatform[0])
    LoftSet.append(Top)
    
    for i in range (0,len(list_parkingplatform)-1):
    
        LoftList = []
        LoftList.append(list_parkingplatform[i])
        LoftList.append(list_parkingplatform[i+1])
        Loft = rs.AddLoftSrf(LoftList,None,None,2)
        LoftSet.append(Loft)
    
    Bot = rs.AddPlanarSrf(list_parkingplatform[-1])
    LoftSet.append(Bot)
    
    
    
    R = random.randint(0,255)
    R1 = random.randint(0,255)
    G = random.randint(0,255)
    G1 = random.randint(0,255)
    B = random.randint(0,255)
    B1 = random.randint(0,255)
    
    ColorVal = []
    Colors = []
    Col = 0
    ColorInterval = 255/len(LoftSet)
    
    for i in range(len(LoftSet)):
        Col += ColorInterval/255
        ColorVal.append(Col)
        Color = LinearColor(R,G,B,R1,G1,B1,ColorVal[i])
        Colors.append(Color)
        Mat = rs.AddMaterialToObject(LoftSet[i])
        rs.ObjectColor(LoftSet[i],Colors[i])
        rs.MaterialColor(Mat,Colors[i])
        
    return LoftSet

def LinearColor(R,G,B,R2,G2,B2,ColorPercentage):
    
    #This function defines linear color gradient by treating R,G,B as coordinates on a 3D line.
    #The base color that will be altered by the percentage should be entered in the second R2,G2,B2 valu
    
    Rdiff = R2 - R
    Gdiff = G2 - G
    Bdiff = B2 - B


    t = ColorPercentage


    R3 = float(R + Rdiff*t)
    G3 = float(G + Gdiff*t)
    B3 = float(B + Bdiff*t)



    return (R3,G3,B3)

def Housing_Platform (PlatformLine,Type_HousingRoof,Rotation,height):
    
    list_parkingplatform =[]
    LoftSet = []
    list_parkingplatform.append(PlatformLine)
    Point_RoofCenter = rs.GetPoint("Please select point for center of roof",Point_BaseWalkway1)

    for i in range(height):
        
        Scalefactor = math.sqrt(math.pow(1,2)-math.pow(i/(height),2))
        
        if Type_HousingRoof == "Gable":
            Scale = (1,Scalefactor,1)
        if Type_HousingRoof == "Hip":
            Scale = (Scalefactor,Scalefactor,1)
        
        if i > 3*height/4:
            Sclae = (1,1,1)
        
        ScalePolygon = rs.ScaleObject(list_parkingplatform[-1],Point_RoofCenter,Scale,True)
        RotatePolygon = rs.RotateObject(ScalePolygon,Point_RoofCenter,Rotation,(0,0,1))
        RotatePolygon = rs.MoveObject(RotatePolygon,(0,0,1))
        list_parkingplatform.append(RotatePolygon)
        
        
    Top = rs.AddPlanarSrf(list_parkingplatform[0])
    LoftSet.append(Top)
    
    for i in range (0,len(list_parkingplatform)-1):
    
        LoftList = []
        LoftList.append(list_parkingplatform[i])
        LoftList.append(list_parkingplatform[i+1])
        Loft = rs.AddLoftSrf(LoftList,None,None,2)
        LoftSet.append(Loft)
    
    Bot = rs.AddPlanarSrf(list_parkingplatform[-1])
    LoftSet.append(Bot)
    
    
    
    R = random.randint(0,255)
    R1 = random.randint(0,255)
    G = random.randint(0,255)
    G1 = random.randint(0,255)
    B = random.randint(0,255)
    B1 = random.randint(0,255)
    
    ColorVal = []
    Colors = []
    Col = 0
    ColorInterval = 255/len(LoftSet)
    
    for i in range(len(LoftSet)):
        Col += ColorInterval/255
        ColorVal.append(Col)
        Color = LinearColor(R,G,B,R1,G1,B1,ColorVal[i])
        Colors.append(Color)
        Mat = rs.AddMaterialToObject(LoftSet[i])
        rs.ObjectColor(LoftSet[i],Colors[i])
        rs.MaterialColor(Mat,Colors[i])
        
    return LoftSet

def Move_Allobjects (Layout):
    
    
    if Layout == 90:
        length = 18
        width = 9
        length_driveway = 24
    
    if Layout == 60:
        length = 10.4
        width = 20.1
        length_driveway = 14.5
    
    if Layout == 45:
        length = 12.7
        width = 19
        length_driveway = 12
    
    if Layout == 30:
        length = 18
        width = 16.8
        length_driveway = 12
    
    Vector_Parkingwidth = rs.VectorCreate((0,width*2,0),(0,0,0))
    Objects_All = rs.ObjectsByType(0,False,0)
    Objects_Moved = rs.MoveObjects(Objects_All,Vector_Parkingwidth)






Layout = rs.GetInteger("Please seletct parking layout you are using (90,60,45,30)",90)
iteration = 0


while iteration != "No":
    
    List_Parking = Parking_Layout(Layout)
    List_Driveway = Driveway_Layout(Layout)
    
    #Building Housing Module#
    
    # List_Parking = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,parkingline1,parkingline2,parkingline3,parkingline4,Line_HousingPlatform,Line_HousingPlatform2]
    # List_Driveway = [pt_dway1, pt_dway2, pt_dway3, pt_dway4, pt_dway5, pt_dway6, pt_dway7, pt_dway8, pt_dwayC, Line_drivewyLB, Line_drivewyRB, Line_drivewyRT, Line_drivewyLT, Line_drivewyLH, Line_drivewyRH]

    Height_Housing = rs.GetInteger("Housing Platform height",20)
    Point_BaseHousing = List_Parking[5]
    Point_ColumnCenter = rs.GetPoint("Please select point for center of column",Point_BaseHousing)
    Rotation = rs.GetInteger("Please provide number for rotation",1)
    Lines_Parking = [List_Parking[16]]
    Lines_Housing = Platform_Layout(Lines_Parking,Height_Housing)
    ###Structure_Platform (PlatformLine,Rotation,ScalePoint,height)###
    Module_Housing = Structure_Platform(Lines_Housing,Rotation,Point_ColumnCenter,Height_Housing)
    Lines_Parking2 = [List_Parking[17]]
    Lines_Housing2 = Platform_Layout(Lines_Parking2,Height_Housing)
    Point_ColumnCenter2 = rs.GetPoint("Please select point for center of column",Point_BaseHousing)
    Module_Housing = Structure_Platform(Lines_Housing2,Rotation,Point_ColumnCenter2,Height_Housing)
    
    
    #Building Walkway#
    
    Height_Driveway = rs.GetInteger("Driveway Platform Height",20)
    
    strPromptSide = "Please select type of structure for walkway"
    strOptionsSide = ["Arch","Vault"]
    Type_Walkway = rs.GetString(strPromptSide,strOptionsSide[1],strOptionsSide)
    
    List_WalkwayModule = []
    
    if Type_Walkway == "Arch":
        Lines_Driveway1 = List_Driveway[13]
        Lines_Driveway2 = List_Driveway[14]
        Lines_Walkway1 = Platform_Layout(Lines_Driveway1,Height_Driveway)
        Lines_Walkway2 = Platform_Layout(Lines_Driveway2,Height_Driveway)
        
        Point_BaseWalkway1 = List_Driveway[7]
        Point_ColumnCenter1 = rs.GetPoint("Please select point for center of column",Point_BaseWalkway1)
        Module_Walkway1 = Structure_Platform(Lines_Walkway1,Rotation,Point_ColumnCenter1,Height_Driveway)
        List_WalkwayModule.append(Module_Walkway1)
        Point_BaseWalkway2 = List_Driveway[3]
        Point_ColumnCenter2 = rs.GetPoint("Please select point for center of column",Point_BaseWalkway2)
        Module_Walkway2 = Structure_Platform(Lines_Walkway2,Rotation,Point_ColumnCenter2,Height_Driveway)
        List_WalkwayModule.append(Module_Walkway2)
    
    if Type_Walkway == "Vault":
        Lines_Driveway1 = List_Driveway[9]
        Lines_Driveway2 = List_Driveway[10]
        Lines_Driveway3 = List_Driveway[11]
        Lines_Driveway4 = List_Driveway[12]
        Lines_Walkway1 = Platform_Layout(Lines_Driveway1,Height_Driveway)
        Lines_Walkway2 = Platform_Layout(Lines_Driveway2,Height_Driveway)
        Lines_Walkway3 = Platform_Layout(Lines_Driveway3,Height_Driveway)
        Lines_Walkway4 = Platform_Layout(Lines_Driveway4,Height_Driveway)
        
        Point_BaseWalkway1 = List_Driveway[0]
        Point_ColumnCenter1 = rs.GetPoint("Please select point for center of column",Point_BaseWalkway1)
        Module_Walkway1 = Structure_Platform(Lines_Walkway1,Rotation,Point_ColumnCenter1,Height_Driveway)
        List_WalkwayModule.append(Module_Walkway1)
        Point_BaseWalkway2 = List_Driveway[2]
        Point_ColumnCenter2 = rs.GetPoint("Please select point for center of column",Point_BaseWalkway2)
        Module_Walkway2 = Structure_Platform(Lines_Walkway2,-Rotation,Point_ColumnCenter2,Height_Driveway)
        List_WalkwayModule.append(Module_Walkway2)
        Point_BaseWalkway3 = List_Driveway[4]
        Point_ColumnCenter3 = rs.GetPoint("Please select point for center of column",Point_BaseWalkway3)
        Module_Walkway3 = Structure_Platform(Lines_Walkway3,Rotation,Point_ColumnCenter3,Height_Driveway)
        List_WalkwayModule.append(Module_Walkway3)
        Point_BaseWalkway4 = List_Driveway[6]
        Point_ColumnCenter4 = rs.GetPoint("Please select point for center of column",Point_BaseWalkway4)
        Module_Walkway4 = Structure_Platform(Lines_Walkway4,-Rotation,Point_ColumnCenter4,Height_Driveway)
        List_WalkwayModule.append(Module_Walkway4)
        
    
    #Building Housing Module#
    
    strPromptHousing = "Do you want to generate housing units?"
    strOptionsHousing = ["Yes","No"]
    Type_HousingBuild = rs.GetString(strPromptHousing,strOptionsHousing[1],strOptionsHousing)
    
    
    
    if Type_HousingBuild == "Yes":
        
        strPromptRoof = "What shape of roof do you want to use?"
        strOptionsRoof = ["Gable","Hip"]
        Type_HousingRoof = rs.GetString(strPromptRoof,strOptionsRoof[1],strOptionsRoof)
        Height_Housing = rs.GetInteger("Height of the house",20)
        
        Housing_Platform (Lines_Housing,Type_HousingRoof,-Rotation/2,Height_Housing)
        
        Type_HousingRoof2 = rs.GetString(strPromptRoof,strOptionsRoof[1],strOptionsRoof)
        Height_Housing2 = rs.GetInteger("Height of the house",20)
        
        Housing_Platform (Lines_Housing2,Type_HousingRoof2,-Rotation/2,Height_Housing2)
    
    strPromptModule = "Do you want to keep making modules?"
    strOptionsModule = ["Yes","No"]
    Type_Module = rs.GetString(strPromptModule,strOptionsModule[1],strOptionsModule)
    
    if Type_Module == "Yes":
        Move_Allobjects (Layout)
    if Type_Module == "No":
        iteration = "No"

