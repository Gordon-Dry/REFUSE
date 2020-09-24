#!/bin/python

import matplotlib.pyplot as plt
import numpy as np

# For literature comparison we always want to base ourselves on real life LM+LOx combination
# The point is to figure out the dry-wet mass ratio for LM from literature that typically considers all propellants together
# So we assume that the tanks for LM and LOx are equal, but that LM is far less dense, and calculate from that the dry-wet ratio of LM tanks
density_LM = 0.42561 # kg/L
density_lox = 1.141 # kg/L

# In KSP:
# Oxidizer has a density of 0.005 metric tonnes/5L, or 0.001 metric tonnes/L, or 1 kg/L
# LqdMethane has a density of 0.00042561 metric tonnes/L, or 0.04256 kg/L
# (CryoTanks engines run in a ratio of 15:1 units, so 15 liter of LqdMethane for every 5 liters of Oxidizer)

# Oxider can be many things, for example:
# LOx: then all the mass is oxygen
# N2O4: then 4*16/(2*14+4*16) = 69.6% is oxygen

# LOx would make the most sense for LM, but this is KSP, and Oxidizer doesn't boiloff
# Note that all cited resources will use LOx, so the plotting will always talk about LOx, because we are interested in the LM part of the tanks
# Mass ratio when Oxidizer is LOx: (1*5)/(0.07085*15) = 4.705
# Mass ratio when Oxidizer is N2O4: (1*5)/(0.07085*15*0.696) = 6.760
# Density wise neither of two match 1 kg/L, LOx being the least dense of them all
# And choosing either of these two extreme answers is a bit weird, because 4.705 is extremely fuel rich, not applied typically at all, but 6.670 is for state of the art engines
# If we look at the actual density LOx has the lowest density of all the oxidizers
# KSP probably made a bit a random choice given the rounded number

# The fun thing is this whole consideration doesn't matter
# Because we are only interesting in the dry-mass of LM tanks for a real rocket
# A real rocket tank runs at a predefined ratio for that given engine design
# Thus includes a predefined ratio of LM and LOx in its tanks, thus also the combined dry-wet mass ratio
# This will tell us what a decent load-bearing tank is like (the shuttle external tank is not part of the main structure)

# The Arianne H-173 stage has a dry-wet ratio of 6.86% (see https://www.nasa.gov/pdf/382034main_018%20-%2020090706.05.Analysis_of_Propellant_Tank_Masses.pdf)
# It uses a Vulcain 2 engine, with a fuel to oxidizer ratio of 6.7 (http://www.astronautix.com/v/vulcain2.html)

mass_ratio_lox_LM = 6.7 # this is dependent on how fuel rich the engine is burning, according to H2 + O2 -> H2O you would get 8, but then you have "hot-oxygen" problems and no cooling of nozzle by fuel
desired_combined_dry_wet_ratio = 0.0686
volume_LM = 1
volume_lox = mass_ratio_lox_LM * (density_LM/density_lox)
volume_ratio_lox_LM = volume_lox/volume_LM

print('Volume LM per liter of fuel {}'.format(volume_LM))
print('Volume lox per liter of fuel {}'.format(volume_lox))

# dry-wet ratio: tank mass/(tank mass + propellant mass)
mass_per_liter_of_LM_tank = np.linspace(0.001, 0.1, 1000)
mass_of_lox_tank_per_liter_of_LM = mass_per_liter_of_LM_tank * volume_ratio_lox_LM
mass_of_combined_fuel_tanks = mass_per_liter_of_LM_tank + mass_of_lox_tank_per_liter_of_LM

mass_of_lox_per_liter_of_LM = density_lox * volume_ratio_lox_LM
mass_of_combined_fuel_per_liter_of_LM = mass_of_lox_per_liter_of_LM + density_LM

print('Mass of one liter of LM {}'.format(density_LM))
print('Mass of corresponding amount of LOx {}'.format(mass_of_lox_per_liter_of_LM))
print('Combined mass per one liter of LM {}'.format(mass_of_combined_fuel_per_liter_of_LM))

dry_wet_ratio_LM = mass_per_liter_of_LM_tank/(mass_per_liter_of_LM_tank + density_LM)
dry_wet_ratio_lox = mass_of_lox_tank_per_liter_of_LM/(mass_of_lox_tank_per_liter_of_LM + mass_of_lox_per_liter_of_LM)
dry_wet_ratio_combined = mass_of_combined_fuel_tanks/(mass_of_combined_fuel_tanks + mass_of_combined_fuel_per_liter_of_LM)

first_index_where_dry_wet_ratio_combined_exceeds_desired_value = np.where(dry_wet_ratio_combined > desired_combined_dry_wet_ratio)[0][0]
print('Dry-wet ratio mass ratio of LM tank {} at a combined ratio {}'.format(dry_wet_ratio_LM[first_index_where_dry_wet_ratio_combined_exceeds_desired_value],
                                                                                dry_wet_ratio_combined[first_index_where_dry_wet_ratio_combined_exceeds_desired_value]))
print('Dry-wet ratio mass ratio of LOx tank {} at a combined ratio {}, note that Oxidizer is not garuanteed to be LOx, and this only applies to a rocket running a fuel to oxidizer ratio of {}, so applicability is limited'.format(
                                                                                dry_wet_ratio_lox[first_index_where_dry_wet_ratio_combined_exceeds_desired_value],
                                                                                dry_wet_ratio_combined[first_index_where_dry_wet_ratio_combined_exceeds_desired_value],
                                                                                mass_ratio_lox_LM))

ax = plt.axes()
ax.semilogy(mass_per_liter_of_LM_tank, dry_wet_ratio_LM * 100, label='LM')
ax.semilogy(mass_per_liter_of_LM_tank, dry_wet_ratio_lox * 100, label='lox')
ax.semilogy(mass_per_liter_of_LM_tank, dry_wet_ratio_combined * 100, label='LM+lox')
ax.set(xlabel='mass of tank per liter of LM in kg',
       ylabel='dry-wet ratio of tank (percentage)')
ax.legend()
ax.grid(True, which='both')
ax.set_title('Dry-wet mass ratios for LM and LOx tanks')
plt.show()