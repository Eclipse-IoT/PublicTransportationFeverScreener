
# Contactless Fever-Screening in Public Transportation

An RFID bus-pass reader with an IR thermal imager for mass fever detection in a public transportation or digital building setting.
(v 1.0.0 Mar 3, 2021)

## Use Cases

#### What is the problem?
> “In light of the global outbreak of the coronavirus (COVID-19), which is now officially a pandemic, society is deeply concerned about the spread of infection and seeking tools to help slow and ultimately stop the spread of the virus” [1]

“Advancements in transportation coupled with the growth and movement of human populations enable efficient transport of infectious diseases almost anywhere in the world within 24 hours” [2]. However, shutting down public transportation services is difficult to do as many people heavily rely on it.  “Public transportation is an essential service that helps to keep communities functioning. Limiting the availability of public transit disproportionately affects segments of the population that rely on it to get to school or work or to access essential goods or services”[3]. Because of this, many transit staff and young and/or lower income passengers who rely on public transportation on a daily basis, have no choice but to face a disproportionately higher risk of COVID-19 exposure [3]. This is why having implemented measures to mitigate these risks are essential, such as the use of PPE (personal protective equipment), physical distancing, constant disinfection/sanitization, and advising passengers to stay at home if they feel any symptoms [3]. 

Unfortunately, physical distancing may prove difficult to do when large numbers of people are forced to crowd the same vehicle, and self-reports are subjective and may be unreliable [2], [3]. Because of this, there is a clear need for a more effective passenger symptom screening tool.

#### What is the solution?
“Infrared thermal detection systems (ITDS) offer a potentially useful alternative to contact thermometry. This technology was used for fever screening at hospitals, airports, and other mass transit sites during the severe acute respiratory syndrome and influenza A pandemic (H1N1) 2009 outbreaks” [2]. “In settings such as travel sites (e.g., airports) and the workplace, ITDS could provide an objective means for the mass detection of fever as part of a comprehensive public health screening strategy because ITDS had greater accuracy than self-reports” [2]. 

The proposed solution consists of a simple IR thermal sensor collecting temperature data on the passenger and RFID scanner to act as a contactless payment method for a bus pass. The user must tap their pass for the fare, and immediately after scan their face for a temperature check. If the thermal sensor does not detect a fever, the passenger is allowed to board the vehicle/enter the station. If the sensor does detect a fever, the passenger will be identified as a potential COVID-19 risk, and will be escorted for further screening. 

#### *Why is this important?*

Transit staff and frequent passengers have no choice but to rely on public transportation, and since maintaining a physical distance may be difficult on a crowded vehicle, identifying COVID-19 carriers through this contactless screening method may prove extremely beneficial in mitigating their risk of transmission. 
