Pipe_OD = float(0.2191)
Pipe_ID = float(0.2063)
PI_Value = float(3.1428571428571429) # 22/7
Mud_Density = float(1200)
Pipe_Thik = float(.0064)
Coating_thik = float(3)
Section_Length = float(48)
MD = float(239) # Co-efficient of Drag unit N/m2
MF = float(0.360) # Co-efficient of Friction
R = float(280) # Assumed Radius of Curvature
E = float(210000000000) # Modulus of Elasticity for steel
Dw = float(12.02) #Drill pipe weight
Wrem = float(300) #Wt of reamer
Do = float(0.0635) #Drill pipe outer dia
Di = float(0.0455) #Drill pipe id

# Buoyancy_of_steel_pipe_in_down_hole
Wb = PI_Value / 4 * Pipe_OD * Pipe_OD * Mud_Density
print("Buoyancy of steel pipe in down-hole : " + str(Wb))

# Moment of Inertia (I) Unit m4 (I = float(0.000024))
I_thik= Pipe_OD**4 - Pipe_ID**4
I = 0.0491071428571429 * I_thik
print("Moment of Inertia : " + str(I))

# Pipe Weight in Air Kg/Meter
Pipe_ND = Pipe_OD - Pipe_Thik
Pipe_Steel_Volume = PI_Value * Pipe_ND
Wt = 1 * Pipe_Thik * Pipe_Steel_Volume * 7850
print("Pipe Weight in Air Kg/Meter : " + str(Wt))

# Coating Weight Kg/Meter
Wc = PI_Value * Pipe_OD * Coating_thik * 0.930267713605456
print("Coating Weight Kg/Meter : " + str(Wc))

# Without anti buoyancy (No water filling is required at the time of pulling.)
Ww = 0

# Actual Wt of pipe = Free wt of pipe in air + Wt of water filled in the pipe + Coating Wt
Actual_Wt_of_pipe = Wt + Wc + Ww

# Total Wt. of steel pipe in Down-Hole (Wpipeb)
Wpipeb = -Wb + Actual_Wt_of_pipe
Wpipen_in_Nm = Wpipeb * 9.80665
print("Buoyancy of steel pipe in down hole : " + str(Wpipen_in_Nm))

# F1 Buoyancy Force = Friction factor in bentonite hole X (Buoyancy Factor)X(Length  of the pipe)
BU = Section_Length * Wpipen_in_Nm * 0.360
F1 = -BU
print("F1 Buoyancy Force : " + str(F1) + " N")

# Bending Moment (BM=E*I/R)
BM = E * I / R
print("Bending Moment : " + str(BM) + " N-m")

# F2 Due to Curvature
R1 = R*11*PI_Value
BFC_P1= 4*MF*BM*360
BFC_P2= R1+R1
F2 = BFC_P1/BFC_P2
print("F2 Buoyance Force Due to Curvature : " + str(F2) + " N")

# F3 Buoyancy Force Due to Cohesion ( Drag ) (md x π x Do x L)/2
F3 = MD * PI_Value * Pipe_OD * Section_Length / 2
print("F3 Buoyancy Force Due to Cohesion ( Drag ) : " + str(F3) + " N")

# F Total Pulling Force (F1+F2+F3)
F = F1+F2+F3
print("F Total Pulling Force : " + str(F) + " N")

# Considering Safety factor with Drill Pipe & Reamer Wt. = ( Pulling force+Wt. of submerged drill pipe +Wream )
TWdr = Dw*Section_Length #Total wt. of drill Rode
Wdr = TWdr+Wrem+F
print("Total wt. of drill pipe : " + str(Wdr) + " kg/m")

# Mud displacement π/4X(do² -di²)x Mud Specific gravity
Thik2 = Do**2-Di**2
MUD_Dis = 0.785714285714286 *  Mud_Density * Thik2
print("Mud displacement : " + str(MUD_Dis) + " kg/m")

# Drill pipe Apparent weight =   (Pipe weight - Mud displacement)
Dpaw_Kg = Dw-MUD_Dis
Dpaw = Dpaw_Kg*9.80665
print("Drill pipe Apparent weight : " + str(Dpaw) + " N/m")

# Total submerged drill pipe wt
W = TWdr*9.80665
Wream_N = Wrem*9.80665

# Total Wt. ( Total submerged drill pipe Wt + Wt of reamer )
Ttl_Wt = W+Wream_N
print("Total Wt. Drill Rod and Reamer : " + str(Ttl_Wt) + " N")

# Hence total pulling force on the pipe is = (F+W+Wream)
TPF = F+W+Wream_N
print("Hence total pulling force on the pipe is : " + str(TPF) + " N")

PThik3 = Pipe_OD**2-Pipe_ID**2
Cs = 0.785714285714285* PThik3 * 1000000

# Tensile stress
Ts = F/Cs
print("Tensile stress : " + str(Ts) + " N/mm2")
