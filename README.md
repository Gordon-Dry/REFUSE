# REFUSE
REalistic Fuels SimplifiEd

## Goals
* REFUSE is aimed at usage in conjunction with Real Solar System (or alternative) that has an low orbit velocity of 7800 m/s.
* It sits on a midpoint inbetween:
    * SMURFF: scaling with stock fuels
    * RealFuels: a very large number of fuels, including engine re-ignition and throttle limits
* This midpoint allows stock-like complexity, while still being able to discuss and tweak actually existing propellant classes
* It's supposed give people of an impression of what is possible today in terms of performance, without pulling the non-stock engine modules that RealFuels uses

## Non-goals
* Supporting a realistic progression through a carreer game, for example:
    * Improving dry-wet ratios of tanks as materials improve
    * Improving TWR ratios of engines as materials and fluid dynamic simulations become available (including required processing power)
    * Supporting hypergolic fuels or any other fuel mixture that is no longer used on boosters
    * Supporting hydrogen-oxygen ratios that are not state-of-the-art (i.e. more fuel rich engines with less capable regenerative cooling systems)
* Supporting toxic RCS fuels, such as hydrazine
* Supporting fuel classes that offer no gameplay value

## Currently supported propellant classes
* Kerolox, otherwise known as Kerosene + LqdOxygen, or RP-1 + LqOxygen
    * De-facto standard fuel, applied to almost all engines and also to bi-propellant RCS systems
* Hydrolox, otherwise known as LqdHydrogen + LqdOxygen, or LH2 + LqdOxygen, applied to any engine running with LqdHydrogen
    * Very high ISP engines, usually needs mods like CryoTanks and CryoEngines
    * LH2 is a low density fuel, which results in high dry-wet mass ratios
* HTP, otherwise known as High-test Peroxide, or hydrogen peroxide, applied to any mono-propellant RCS or engine

## Propellant classes currently left unmodified
* SolidFuel, performance is fairly realistic as well, and the resource situation in CommunityResourcePack is not clear
    * The polymers such as PBAN (Polybutadiene acrylonitrile) are available, but no sign of the actual fuels such APCP (Ammonium perchlorate composite propellant) are not

## Possible future propellant classes
* Methalox, otherwise known as LqdMethane + LqdOxygen, interesting for refueling on planets with CO2 rich atmosphere

## Dependencies
* ModuleManager
* CommunityResourcePack

## Intended to be compatible with
* Stock tanks
* B9 tanks
* Procedural tanks