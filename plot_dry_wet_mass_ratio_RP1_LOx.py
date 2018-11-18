#!/bin/python

import matplotlib.pyplot as plt
import numpy as np

# For literature comparison we always want to base ourselves on real life rp1+LOx combination
# The point is to figure out the dry-wet mass ratio for rp1 from literature that typically considers all propellants together
density_rp1 = 0.820 # kg/L
density_lox = 1.141 # kg/L

mass_ratio_lox_rp1 = 2.56 # this is dependent on how fuel rich the engine is burning
desired_combined_dry_wet_ratio = 0.027
volume_rp1 = 1
volume_lox = mass_ratio_lox_rp1 * (density_rp1/density_lox)
volume_ratio_lox_rp1 = volume_lox/volume_rp1

print('Volume rp1 per liter of fuel {}'.format(volume_rp1))
print('Volume lox per liter of fuel {}'.format(volume_lox))

# dry-wet ratio: tank mass/(tank mass + propellant mass)
mass_per_liter_of_rp1_tank = np.linspace(0.001, 0.1, 1000)
mass_of_lox_tank_per_liter_of_rp1 = mass_per_liter_of_rp1_tank * volume_ratio_lox_rp1
mass_of_combined_fuel_tanks = mass_per_liter_of_rp1_tank + mass_of_lox_tank_per_liter_of_rp1

mass_of_lox_per_liter_of_rp1 = density_lox * volume_ratio_lox_rp1
mass_of_combined_fuel_per_liter_of_rp1 = mass_of_lox_per_liter_of_rp1 + density_rp1

print('Mass of one liter of rp1 {}'.format(density_rp1))
print('Mass of corresponding amount of LOx {}'.format(mass_of_lox_per_liter_of_rp1))
print('Combined mass per one liter of rp1 {}'.format(mass_of_combined_fuel_per_liter_of_rp1))

dry_wet_ratio_rp1 = mass_per_liter_of_rp1_tank/(mass_per_liter_of_rp1_tank + density_rp1)
dry_wet_ratio_lox = mass_of_lox_tank_per_liter_of_rp1/(mass_of_lox_tank_per_liter_of_rp1 + mass_of_lox_per_liter_of_rp1)
dry_wet_ratio_combined = mass_of_combined_fuel_tanks/(mass_of_combined_fuel_tanks + mass_of_combined_fuel_per_liter_of_rp1)

first_index_where_dry_wet_ratio_combined_exceeds_desired_value = np.where(dry_wet_ratio_combined > desired_combined_dry_wet_ratio)[0][0]
print('Dry-wet ratio mass ratio of rp1 tank {}% at a combined ratio {}%'.format(dry_wet_ratio_rp1[first_index_where_dry_wet_ratio_combined_exceeds_desired_value],
                                                                                dry_wet_ratio_combined[first_index_where_dry_wet_ratio_combined_exceeds_desired_value]))
print('Dry-wet ratio mass ratio of LOx tank {}% at a combined ratio {}%, note that this only applies to a rocket running a fuel to oxidizer ratio of {}, so applicability is limited'.format(
                                                                                dry_wet_ratio_lox[first_index_where_dry_wet_ratio_combined_exceeds_desired_value],
                                                                                dry_wet_ratio_combined[first_index_where_dry_wet_ratio_combined_exceeds_desired_value],
                                                                                mass_ratio_lox_rp1))

ax = plt.axes()
ax.semilogy(mass_per_liter_of_rp1_tank, dry_wet_ratio_rp1 * 100, label='rp1')
ax.semilogy(mass_per_liter_of_rp1_tank, dry_wet_ratio_lox * 100, label='lox')
ax.semilogy(mass_per_liter_of_rp1_tank, dry_wet_ratio_combined * 100, label='rp1+lox')
ax.set(xlabel='mass of tank per liter of rp1 in kg',
       ylabel='dry-wet ratio of tank (percentage)')
ax.legend()
ax.grid(True, which='both')
ax.set_title('Dry-wet mass ratios for rp1 and LOx tanks')
plt.show()