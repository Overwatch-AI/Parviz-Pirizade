## Step 3 – Retrieval & Answer Evaluation

- **Model used for /query**: models/gemini-2.5-pro
- **Number of evaluated questions**: 20
- **Answer accuracy**: 85.0%
- **Page-reference accuracy**: 24.7%

### Q1

- **Question**: I'm calculating our takeoff weight for a dry runway. We're at 2,000 feet pressure altitude, and the OAT is 50°C. What's the climb limit weight ?
- **Labelled answer**: Based on the data for a dry runway at 2,000 feet pressure altitude with an OAT of 50°C, the Climb Limit Weight is 52,200 kg.
- **Model answer**: Based on the "Takeoff Field & Climb Limit Weights - Dry Runway" table for 2000 FT pressure altitude, the climb limit weight at an OAT of 50°C is **52,200 kg**.
- **Labelled pages**: 83
- **Returned pages**: 82, 83, 85, 86
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.50
### Q2

- **Question**: We're doing a Flaps 15 takeoff. Remind me, what is the first flap selection we make during retraction, and at what speed?
- **Labelled answer**: For a Flaps 15 takeoff, the first flap selection during retraction is Flaps 5, which you select at V2 + 15 knots.
- **Model answer**: Based on the Takeoff Flap Retraction Speed Schedule, for a Flaps 15 takeoff, the first flap selection you make during retraction is **Flaps 5**, and you select it at **V2 + 15** knots.
- **Labelled pages**: 41
- **Returned pages**: 41, 45, 46, 54, 101, 102
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 1.67
### Q3

- **Question**: We're planning a Flaps 40 landing on a wet runway at a 1,000-foot pressure altitude airport. If the wind-corrected field length is 1,600 meters, what is our field limit weight?
- **Labelled answer**: For a Flaps 40 landing on a wet runway at 1,000 feet pressure altitude with a 1,600-meter wind-corrected field length, the field limit weight is 55,800 kg
- **Model answer**: Based on the provided context, for a landing on a wet runway at a 1,000-foot pressure altitude with a wind-corrected field length of 1,600 meters, the field limit weight is **55,800 kg**.
- **Labelled pages**: 99
- **Returned pages**: 82, 83, 85, 86, 99, 102
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 1.67
### Q4

- **Question**: Reviewing the standard takeoff profile: After we're airborne and get a positive rate of climb, what is the first action we take?
- **Labelled answer**: After getting a positive rate of climb, the first action is to call for "GEAR UP". This is shown in both the "Takeoff Procedure" table and the "Takeoff" flight pattern diagram.
- **Model answer**: Based on the provided context, after a positive rate of climb is indicated, the first action is to raise the landing gear.

Specifically, the Takeoff Procedure outlines the following steps:
*   **Pilot Flying (PF):** When a positive rate of climb is indicated, calls “GEAR UP.”
*   **Pilot Not Flying (PNF):** Verifies the positive rate of climb and positions the landing gear lever to UP.
- **Labelled pages**: 39, 51
- **Returned pages**: 37, 39, 40, 51
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 5.00
### Q5

- **Question**: Looking at the panel scan responsibilities for when the aircraft is stationary, who is responsible for the forward aisle stand?
- **Labelled answer**: Based on the "Panel Scan Diagram" for when the airplane is not moving under its own power, the Captain is responsible for the forward aisle stand (the area labeled with the number 6).
- **Model answer**: Based on the provided context, the responsibility for the forward aisle stand (also known as the FMS/CDU area) is divided between the Captain and the First Officer.

*   **The Captain** is responsible for the left CDU/FMS unit.
*   **The First Officer** is responsible for the right CDU/FMS unit.

Both pilots are responsible for verifying their own route entries, performance data, and configuration on their respective units.
- **Labelled pages**: 6
- **Returned pages**: 6, 7
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 5.00
### Q6

- **Question**: For a standard visual pattern, what three actions must be completed prior to turning base?
- **Labelled answer**: According to the "Visual Traffic Pattern" diagram, the three actions to complete prior to turning base are:
Gear down
Flaps 15 (landing flaps for 1 engine)
Arm speedbrake
- **Model answer**: Based on the provided context, the three actions that must be completed prior to turning base in a visual traffic pattern are:

1.  **Extend the gear** (Gear down).
2.  **Set Flaps 15** (noted as landing flaps for a one-engine scenario).
3.  **Arm the speedbrake**.

The documents also mention to "Start descent as required" during this phase.
- **Labelled pages**: 56
- **Returned pages**: 39, 45, 47, 55, 56
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.00
### Q7

- **Question**: When the Pilot Not Flying (PNF) makes CDU entries during flight, what must the Pilot Flying (PF) do prior to execution
- **Labelled answer**: The Pilot Flying must verify the entries prior to execution.
- **Model answer**: Based on the context provided, when the Pilot Not Flying (PNF) makes CDU entries during flight, the Pilot Flying (PF) must verify the entries prior to execution.
- **Labelled pages**: 5
- **Returned pages**: 3, 5, 40, 43, 45, 46
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 1.67
### Q8

- **Question**: I see an amber "STAIRS OPER" light illuminated on the forward attendant panel; what does that light indicate?
- **Labelled answer**: That amber STAIRS OPER (Operating) light indicates that the airstair is in transit (i.e., currently extending or retracting).
- **Model answer**: Based on the provided context, an illuminated amber "STAIRS OPER" light indicates that the airstair is in transit.
- **Labelled pages**: 126
- **Returned pages**: 115, 117, 123, 126, 134
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.00
### Q9

- **Question**: We've just completed the engine start. What is the correct configuration for the ISOLATION VALVE switch during the After Start Procedure?
- **Labelled answer**: During the After Start Procedure, the ISOLATION VALVE switch should be set to AUTO.
- **Model answer**: Based on the provided context, during the After Start Procedure, the ISOLATION VALVE switch should be set to **AUTO**.
- **Labelled pages**: 35
- **Returned pages**: 17, 32, 33, 35, 49
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.00
### Q10

- **Question**: During the Descent and Approach procedure, what action is taken with the AUTO BRAKE select switch , and what is the Pilot Flying's final action regarding the autobrake system during the Landing Roll procedure?
- **Labelled answer**: Here are the autobrake actions for those two phases of flight:
Descent and Approach Procedure
During the Descent and Approach Procedure, you set the AUTO BRAKE select switch to the desired brake setting.

Landing Roll Procedure
The Pilot Flying's final action regarding the autobrake system is to disarm the autobrake prior to reaching taxi speed.
- **Model answer**: Based on the context provided:

*   **During the Descent and Approach procedure:** The AUTO BRAKE select switch is set to the desired brake setting by both the Pilot Flying and the Pilot Not Flying.

*   **During the Landing Roll procedure:** The Pilot Flying's final action regarding the autobrake system is to disarm the autobrake prior to taxi speed and continue with manual braking as required.
- **Labelled pages**: 43, 47
- **Returned pages**: 43, 45, 47
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 6.67
### Q11

- **Question**: We need to hold at 10,000 feet, and our weight is 60,000 kg. What is the expected total fuel flow in kilograms per hour?
- **Labelled answer**: The expected total fuel flow for holding at 10,000 feet with a weight of 60,000 kg is 2100 kilograms per hour (KG/HR). It is important to note that the fuel flow value provided in this table already includes a 5% additional fuel allowance for holding in a racetrack pattern
- **Model answer**: I don't know. The provided context contains tables for "Trip Fuel and Time Required" and "Short Trip Fuel and Time," but it does not include the "Holding Planning" table which would have the fuel flow information for holding at specific altitudes and weights.
- **Labelled pages**: 93
- **Returned pages**: 77, 91, 92, 93
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 2.50
### Q12

- **Question**: I'm looking at the exterior light switches on the overhead panel. What is the function of the TAXI Light switch?
- **Labelled answer**: The TAXI Light switch controls the taxi light, which is mounted on the nose wheel strut.

OFF: The nose wheel well taxi light is extinguished.

ON: The nose wheel well taxi light is illuminated.
- **Model answer**: Based on the provided context, the function of the TAXI Light Switch is as follows:

*   **OFF**: Extinguishes the nose wheel taxi light.
*   **ON**: Illuminates the nose wheel taxi light.
- **Labelled pages**: 112, 131
- **Returned pages**: 112, 113, 115, 117, 130, 134
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 1.67
### Q13

- **Question**: where exactly are the Logo Lights located on the airframe?
- **Labelled answer**: Based on the manual, the Logo Lights are located on the top of each horizontal stabilizer surface.

They are positioned to point light onto both sides of the vertical stabilizer.
- **Model answer**: Based on the context provided, the Logo Lights are located on the top of each horizontal stabilizer surface. Their purpose is to illuminate both sides of the vertical stabilizer.
- **Labelled pages**: 131
- **Returned pages**: 113, 130, 132, 138
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 0.00
### Q14

- **Question**: I'm preparing for a Flaps 15 go-around. If our weight-adjusted gradient is 4% and our speed is VREF+20, what is the gradient adjustment for speed?
- **Labelled answer**: Based on the "ENGINE INOP Go-Around Climb Gradient Flaps 15" table, the gradient adjustment for speed when flying at VREF+20 with a weight-adjusted go-around gradient of 4% is 0.28%
- **Model answer**: Based on the "Gradient Adjustment for Speed (%)" table, for a speed of VREF+20 and a weight-adjusted go-around gradient of 4%, the gradient adjustment for speed is **0.28%**.
- **Labelled pages**: 101
- **Returned pages**: 41, 75, 99, 101, 107
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.00
### Q15

- **Question**: I'm holding the BCF (Halon) fire extinguisher. After I pull the ring pin, what is the action required to discharge the agent?
- **Labelled answer**: After pulling the ring pin, you must press the top lever to discharge the agent.

The manual also recommends aiming at the base of the fire from a distance of six feet.
- **Model answer**: Based on the provided context, after you pull the ringed safety pin, you need to **press the top lever** to discharge the agent.

The instructions also specify to first aim at the base of the fire from a distance of six feet before pressing the lever.
- **Labelled pages**: 146
- **Returned pages**: 10, 132, 145
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 0.00
### Q16

- **Question**: I'm calculating my takeoff performance. The available runway is 2,000 meters with a 1.0% uphill slope. Factoring in a 10-knot tailwind, what is the final slope and wind-corrected field length I should use?
- **Labelled answer**: Here is the two-step calculation based on the "Takeoff Field Corrections - Dry Runway" tables:

Step 1: Slope Correction

Using the "Slope Corrections" table, find the row for FIELD LENGTH AVAILABLE (M) of 2000.

Find the column for RUNWAY SLOPE (%) of 1.0 (uphill).

The intersection gives a Slope Corrected Field Length of 1,760 meters.

Step 2: Wind Correction

Using the "Wind Corrections" table, you must use the 1,760-meter value from Step 1 as your input. This requires interpolation between the 1600m and 1800m rows.

Find the column for a 10-knot tailwind (the "10" column).

The value for a 1600m corrected length is 1680.

The value for a 1800m corrected length is 1880.

Interpolating for your 1,760m length gives a final value of 1,840 meters.

The final slope and wind-corrected field length you should use is 1,840 meters.
- **Model answer**: Based on the provided documents, the calculation requires a two-step process: first, find the slope-corrected field length, and then use that value to find the final wind-corrected field length. Since the runway condition (dry or wet) was not specified, here are the calculations for both scenarios.

### Scenario 1: Dry Runway

1.  **Slope Correction:**
    *   Using the "Slope Corrections – Dry Runway" table, find the row for an available field length of **2000 m**.
    *   In that row, find the value under the **1.0** column for a +1.0% slope.
    *   The slope-corrected field length is **1840 meters**.

2.  **Wind Correction:**
    *   Using the "Wind Corrections – Dry Runway" table, find the value for a slope-corrected length of **1840 m** with a **10-knot tailwind** (the "10" column).
    *   Since 1840 m is not listed, we must interpolate between 1800 m and 2000 m.
        *   At 1800 m, the corrected length is 1880 m.
        *   At 2000 m, the corrected length is 2090 m.
    *   Interpolating for 1840 m gives a final corrected field length of **1922 meters**.

### Scenario 2: Wet Runway

1.  **Slope Correction:**
    *   Using the "Slope Corrections - Wet Runway" table, find the row for an available field length of **2000 m**.
    *   In that row, find the value under the **1.0** column for a +1.0% slope.
    *   The slope-corrected field length is **1880 meters**.

2.  **Wind Correction:**
    *   Using the "Wind Corrections - Wet Runway" table, find the value for a slope-corrected length of **1880 m** with a **10-knot tailwind** (the "10" column).
    *   Since 1880 m is not listed, we must interpolate between 1800 m and 2000 m.
        *   At 1800 m, the corrected length is 1900 m.
        *   At 2000 m, the corrected length is 2110 m.
    *   Interpolating for 1880 m gives a final corrected field length of **1984 meters**.

**In summary:**

*   For a **dry runway**, the final corrected field length is **1922 meters**.
*   For a **wet runway**, the final corrected field length is **1984 meters**.
- **Labelled pages**: 81
- **Returned pages**: 81, 83, 84, 85, 99
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 2.00
### Q17

- **Question**: I need to check the crew oxygen. There are 3 of us, and the bottle temperature gauge reads 30°C. What is the minimum required pressure in PSI for our 114 Cu. Ft. cylinder?
- **Labelled answer**: For 3 crew members at a bottle temperature of 30°C, the minimum required pressure for the 114/115 Cu. Ft. cylinder is 690 PSI.
- **Model answer**: Based on the provided table for a 114/115 Cu. Ft. cylinder, the minimum required pressure for 3 crew members at a bottle temperature of 30°C is **690 PSI**.
- **Labelled pages**: 94
- **Returned pages**: 94, 105, 140, 141, 144
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.00
### Q18

- **Question**: We're on an ILS approach. What three actions should I initiate as soon as the glideslope comes alive?
- **Labelled answer**: Based on the ILS Approach diagram and the Landing Procedure, as soon as the glideslope is "alive," you should initiate these three actions:

Call for "GEAR DOWN"

Call for "FLAPS 15"

Arm speed brake
- **Model answer**: Based on the provided context, when the glideslope becomes active ("alive"), you should initiate the following three actions:

1.  **Lower the gear** ("Gear down").
2.  **Set flaps to 15** ("Flaps 15").
3.  **Arm the speedbrake**.
- **Labelled pages**: 45, 52
- **Returned pages**: 43, 45, 46, 52
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 5.00
### Q19

- **Question**: What are the three available settings on the POSITION light switch located on the forward overhead panel?
- **Labelled answer**: Here are the three available settings on the POSITION Light switch:


STROBE & STEADY 


OFF 


STEADY
- **Model answer**: Based on the provided context, the three available settings on the POSITION light switch are:

1.  **STROBE & STEADY:** Illuminates the red and green wing-tip position lights, white trailing edge wing-tip lights, and the wing-tip and tail strobe lights.
2.  **OFF:** Extinguishes all position and strobe lights.
3.  **STEADY:** Illuminates only the steady lights (red and green wing-tip position lights and white trailing edge wing-tip lights).
- **Labelled pages**: 113
- **Returned pages**: 17, 109, 112, 113, 126
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.00
### Q20

- **Question**: Looking at the components of the passenger entry door, what is the name of the bar that secures the emergency escape slide to the aircraft floor?
- **Labelled answer**: Based on the "Passenger Entry/Galley Service Doors" diagram in the manual, the bar that secures the emergency escape slide to the floor brackets is called the GIRT BAR.
- **Model answer**: Based on the provided context, the bar that secures the emergency escape slide to the aircraft floor is called the **girt bar**.
- **Labelled pages**: 123
- **Returned pages**: 115, 116, 117, 118, 123
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 2.00
