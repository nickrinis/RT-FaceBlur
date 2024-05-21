<h1 align="center">RT_FaceBlur</h1>
<p align="justify"><strong>The programme captures live feed from the system it's running on, blurring in the process all the faces detected using openCV. It's based around Access Control through the usage of DataFrames and depending on the clearance level the current user has before logging in, the programme will behave differently and at the end record any actions taken while it was running. </strong>
<br/>
<h2>About</h2>
This project was part of my thesis on the collection of personal information through the use of CCTV. The grade counted towards my diploma. A lot of thanks to my tutor <a href="https://www.linkedin.com/in/georgios-lioudakis-6b37286/" target="_blank">Giorgos Lioudakis</a> who guided me through the whole process. The project has been updated since submission.

<h2>Installation</h2>

1. Download this project as zip and extract it.
2. Download Python and the necessary libraries (OpenCV, Pandas, Tkinter, etc.).
3. Run RT_FaceBlur.py through your IDE of choice.

Alternatively:
1. Clone the repository: git clone https://github.com/nickrinis/RT-FaceBlur.git
2. Navigate to the project directory: cd RT-FaceBlur
3. Run the main Python script: python RT-FaceBlur.py

<h2>Usage</h2>
When it starts running the programme will request login credentials.
Already existing credentials can be found in the 'Database_Generator.py' file under the 'generate_data()' function.

For all scenarios, the programme will detect faces from the live feed and blur them.
- Clearance 0: The user doesn't have any additional functionality and can only observe the blurred feed until he decides to exit.
- Clearance 1: The user can lift the restrictions by pressing the button "-", however only for 30 seconds before the blurring resumes.
- Clearance 2: The user can lift the restrictions indefinitely.
Upon pressing "`" the programme will stop running and generate a log file detailing all the actions taken by the users.

<h2>Credits</h2>

RT_FaceBlur relies on the following libraries and tools:
- Cv2
- Pandas
- Tkinter
- Logging
- Keyboard
- Other standard Python libraries


<h2>Contact</h2>
If you have any questions or feedback, please contact me at [nickmarinis12@hotmail.gr](mailto:nickmarinis12@hotmail.gr).

<h2>Copyright</h2>
This project is licensed under the terms of the MIT license.
