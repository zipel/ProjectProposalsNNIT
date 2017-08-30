# Improving direction detection of Bluetooth beacons for the visual impaired


## Background

It is challenging for the visual impaired to find their way, e.g. in buildings. Although some electronic systems may help finding the approximate location of things, the precision is typically not good enough to locate e.g. a precise door or object. This is especially true indoors, where GPS is not working well. Both outdoors and indoors, it is difficult to guide a person within the last meters, in particular regarding the precise direction (e.g. “to your left”, or “in front of you”). So far, some dedicated hardware has sometimes been used to help visual impaired with way finding, but it is typically expensive, does not scale well, and requires transporting additional hardware. Bluetooth beacons (e.g., iBeacon) work quite well off-the-shelve, but the default detection typically does not provide any direction clue.
This activity is a follow-up of a 2015 student project (GuideBelt: Bluetooth-based Indoor Navigation System for the Visually Impaired, by Abdulrashid Mohammed, Maytham Fahmi, and Tanase Comboeanu), and is done in collaboration with Alexandra Institute [http://alexandra.dk/dk/aktuelt/nyheder/2015/nu-kan-blinde-finde-vej-med-audiobeacons].
This time, the ambition is to use solely the smartphone abilities (e.g. internal sensors) and take advantage of the natural shielding effect of the human body, to provide a user interface with better directional clues.

## Project idea

1.	Get familiar with the background
	* Read previous work;
2.	Test the existing software and hardware components available;
3.	Build an Android (or iOS) app dedicated to BLE scanning, which can:

	a.	Detect Bluetooth beacons in the vicinity and return their signal strength (RSSI);
	
	b.	Use the internal sensors of the telephone (e.g. compass/gyro/accelerometer) to detect movements (when the user rotates, in particular);
	
	c.	Add an algorithm with some data processing to update a model guessing in which direction the beacons are;
	
	d.	Experiment with various input/output modalities (e.g. sound, vibrations) and improve accordingly the user interface (graphical and audio) of the mobile app to better convey proximity information, also for visual impaired users (but not exclusively);
	
4.	Test the results with ITU students, then with visual impaired users;
	* You will get guidance to collect data in a rigorous way;
5.	Compare with other solutions and suggest future improvements;
6.	Co-author a scientific publication of the results.

## Technology

- Android [https://developers.google.com/beacons/]; 

- Bluetooth Low Energy [Robin Heydon, Bluetooth Low Energy: The Developer’s Handbook, ISBN:978-0-13-288836-3]; 

- Bluetooth beacons [e.g. http://developer.radiusnetworks.com]; 

- RFduino [http://www.rfduino.com];

## Supervisor(s)

Sebastian Büttrich <sebastian@itu.dk>;

Alexandre Alapetite (Alexandra Institute, 5B04).
