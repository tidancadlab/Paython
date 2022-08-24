Radius_of_Curvature = int(360)
Pipe_OD = float(0.2191)
PI_Value = float(3.1428571428571429)
Mud_Density = float(1200)
# Modulus of Elasticity for steel
E = float(210000000000)
Buoyancy_of_steel_pipe_in_down_hole = PI_Value / 4 * Pipe_OD * Pipe_OD * Mud_Density
Pipe_Thik = float(.0064)
# Moment of Inertia (I) Unit m4 (I = float(0.000024))
I = 0.0491071428571429 * Pipe_Thik * Pipe_Thik
Pipe_ND = Pipe_OD - Pipe_Thik
Pipe_Steel_Volume = PI_Value * Pipe_ND
Pipe_wight_air = 1 * Pipe_Thik * Pipe_Steel_Volume * 7850
Coating_thik = float(3)
Coating_Wight = I * Pipe_OD * Coating_thik * 0.930267713605456
Actual_Wt_of_pipe = Pipe_wight_air + Coating_Wight
# Total Wt. of steel pipe in Down-Hole (Wpipeb)
Wpipeb = -Buoyancy_of_steel_pipe_in_down_hole + Actual_Wt_of_pipe
Wpipen_in_Nm = Wpipeb * 9.80665
Section_Length = float(48)
# Buoyancy Force = Friction factor in bentonite hole X (Buoyancy Factor)X(Length  of the pipe)
BF = Section_Length * Wpipen_in_Nm * 0.360

print("Buoyancy of steel pipe in down-hole : " + str(Buoyancy_of_steel_pipe_in_down_hole))
print("Moment of Inertia : " + str(I))
print("Pipe Weight in Air Kg/Meter : " + str(Pipe_wight_air))
print("Coating Weight Kg/Meter : " + str(Coating_Wight))
print("Buoyancy of steel pipe in down hole : " + str(Wpipen_in_Nm))
print("Buoyancy Force : " + str(BF))