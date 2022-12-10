## Simulation Metadata

---


- Virus: Sniffles
- Mortality Rate: 12%
- Basic Reproduction: 50%
- Population Size: 1000
- Vaccination Percentage: 10%
- Initial Infected: 50
## Simulation Log
---
```diff
@@ Simulation Initial State @@
+ Alive: 1000
+ Vaccinated: 100
+ Saved by Immunity: 0
! Infected: 50
- Dead: 0
```
```diff
@@ Step 1 @@
+ Alive: 998
+ Vaccinated: 149
+ Saved by Immunity: 600
! Infected: 781
- Dead: 2
```
```diff
@@ Step 2 @@
+ Alive: 915
+ Vaccinated: 847
+ Saved by Immunity: 41073
! Infected: 68
- Dead: 85
```
```diff
@@ Step 3 @@
+ Alive: 908
+ Vaccinated: 908
+ Saved by Immunity: 6555
! Infected: 0
- Dead: 92
```
```diff
@@ Simulation End State @@
! Total Interactions: 89900
+ Alive: 908
+ Vaccinated: 908
+ Saved by Immunity: 48228
- Dead: 92
```
