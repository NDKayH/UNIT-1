# Project Unit 1

## Criterion A: Planning

### Problem Definition
My client, the staff and faculty of a boarding school, have various different padlocks for the buildings across campus which are locked every night at 23:00. These buildings, containing mostly classrooms, were broken into by three students two and a half weeks ago, and after an investigation the school concluded that a data breach had occurred where a password for one of the buildings was shared and students were able to hang out very late at night. The school has opted for several future prevention methods; the first one is to change all the passwords of each and every lock on the school campus to much more complicated ones. However, they realize that because of how difficult these new passwords might be to remember, the people responsible for locking up the buildings might write down passwords on paper, which is quite insecure, and they believe a breach could happen again. To prevent this, the school is also looking for a password storage application that contains a database of all passwords. 


### Proposal Solution
This project aims to fix the recent security incident by implementing an encrypted password storage and management system that ensures that only authorized faculty and student lockup-crew members can access and use building passwords. This solution will help prevent unauthorized access and reduce the risk of another data breach by ensuring that passwords are managed effectively and securely.

#### **Objectives**

1. **Enhanced Security**: To avoid unauthorized access, complicated building passwords should be stored securely.
2. **User-Friendly Management**: Give authorized staff members access to a user-friendly system so they can generate, view, and manage passwords without having to commit them to memory.
3. **Controlled Access**: Put in place a system that makes that passwords may only be accessed and updated by authorized personnel.
4. **Data Integrity**: In order to avoid any breaches even in the event that access to the storage file is stolen, make sure that all password entries are encrypted.


### **Design Proposal for Secure Password Management System**

#### **System Features**

1. **Password Management Application**: 
   - The main application will serve as a password manager that allows authorized staff to:
   - **Add** new building passwords.
   - **Delete** old or outdated passwords.
   - **View** encrypted passwords securely.
   - **Modify** existing passwords when changes are needed.
2. **Encryption and Decryption**: 
   - To guarantee data secrecy, every password will be encrypted using a simple but powerful encryption technique.
   - An ROT13-based encryption method will be used by the system to shift numerical characters, making them incomprehensible to unauthorized users.
   - This encryption makes sure that the passwords stay safe and unreadable even in the event that an unauthorized person gains access to the storage file.
3. **Secure Storage**: 
   - The password database will be a file called `passwords.csv` that contains the passwords.
   - An encrypted password and a building identification (such as a room number) will be included with each entry.
   - While the encryption protects data security, the .csv format makes easy archiving and retrieval possible.
4. **Calculator Integration**: 
   - The system will include a simple calculator interface that staff members can utilize on a regular basis. A concealed "master code" will allow staff members to access the password management interface while keeping unauthorized users out of the system. 
5. **Access Control via Secret Code**: 
   - The password management system is accessed by a distinct master code `lockup_92135467`, which only authorized staff can use to switch from the calculator interface to the password management system.


#### **System Architecture**
   - **User Interface**: The application utilizes a console or terminal and is text-based. The program is used by staff members using menu-driven instructions.
   - **Data Storage**: A `passwords.csv` file is used to store passwords, guaranteeing their secure storage and allowing authorized staff to access them when required.
   - **Encryption Module**: This module manages the encryption logic that transforms plain text passwords into safe, encrypted strings and back again when needed. It does this by handling both encryption and decryption functions.


#### **Workflow and Usage Scenarios**

1. **Daily Operations**:
   - Staff use a basic calculator application interface to access the system on a regular basis.
   - When it comes time to handle building passwords, authorized personnel can access the password manager by entering the secret master code, `lockup_92135467`
2. **Password Management**:
   - **Adding Passwords**: Staff can enter a password and the building's identification. Prior to storing the password, the system encrypts it.
   - **Deleting Passwords**: Employees can remove outdated passwords by providing the building identification when deleting a password.
   - **Viewing Passwords**: When needed, authorized staff members can safely read encrypted passwords by decrypting them within the program.
3. **Data Protection**:
   - The passwords are protected even in the event that this file is viewed without authority thanks to the encrypted password data contained in `passwords.csv`.
   - Sensitive data is protected while it is in transit and at rest thanks to the encryption process.


#### **Technical Details**

1. **Encryption Method**: 
   - Makes use of a modified ROT13 encryption method that shifts numerical characters.
   - Because non-alphabetic characters (such numerals and symbols) don't change, the password difficulty is maintained.
2. **Programming Language**:
   - Python is used for its simplicity and ease of implementation, allowing non-technical staff to interact with the application effortlessly.
3. **Storage File Format**:
   - .csv is chosen for its readability, simplicity, and ease of access, even if opened outside the application.


#### **Benefits**
   - **Security**: Even in the event that the .csv file is compromised, encrypted storage reduces the possibility of unwanted access.
   - **Convenience**: Employees just need to know one password to access the entire building, which lowers the possibility of misplacing paper passwords or sharing them insecurely.
   - **Flexibility**: As needed, the system can be extended or changed to accommodate new features, such password expiration policies or more advanced encryption techniques.


### Success Criteria 
1. The calculator should accept user input to perform basic operations (addition, subtraction, multiplication, division).
2. The calculator can handle typical errors (e.g., division by zero) and give appropriate feedback.
3. If the user enters the secret code `"open123"`, the program will change modes and act as a password manager.
4. In password manager mode, the user should be able to perform CRUD operations (Create, Replace, Update, Delete):
   * Add a password (for example, for a website).
   * View the stored passwords (only if they re-enter the secret code).
5. Save passwords permanently and securely
6. Use the terminal to interact with the user.

# Criterion B: Design
### System Diagram
<img width="904" alt="Screenshot 2024-09-27 at 1 54 58" src="https://github.com/user-attachments/assets/05f35b57-8e73-44b6-8294-f763d36a2de3">
**Fig. 1** This is the sytem diagram for the application and it's surrounding support and enviroment


### Flow diagrams for algorithms
img
fig 2

### Data storage

### Sketches of the application (wireframe diagrams)

### Test plan

| Test No. | Type of Test | Area Tested          | Outcome of Test                                                                                                           | Time Estimate | Target Completion Date | Criterion |
|----------|--------------|----------------------|---------------------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1        | Unit testing | The calculator       | Confirm that the calculator is functional and                                                                             | 10 mins       | Sep 12                 | B         |
| 2        | Unit testing | The Password Manager | Confirm that the password manager and all it's functions work properly and as intended                                    | 10 mins       | Sep 14                 | B         |
| 3        | Unit Testing | Encryption           | Confirm that the ROT13-derived encryption is able to effectively scramble passwords saved within the `passwords.csv` file | 10 mins       | Sep 25                 | B         |
## Records of Tasks

| Task | Planned Action                                                                                                      | Planned Outcome                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Estimated Time | Target Completion | Criterion |
|------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-------------------|-----------|
| 1    | 1st Meeting with the client                                                                                         | Obtained a problem definition and the client's needs, understand what the situation is                                                                                                                                                                                                                                                                                                                                                                                                                 | 10 min         | Sep 6             | A         |
| 2    | Come up with plan and problem definiton                                                                             | Have a clear problem definition and a plan for development (also prefferably written on GitHub)                                                                                                                                                                                                                                                                                                                                                                                                        | 25 mins        | Sep 6             | A         |
| 3    | Come to an agreement with the client in regards to the problem definition and the successs criteria                 | Write a list of the success criteria (prefferably in GitHub) which will guide me through the proposal and future development                                                                                                                                                                                                                                                                                                                                                                           | 10 mins        | Sep 6             | A         |
| 4    | Come up with a solution proposal to present to the client                                                           | Write a clear solution proposal on how specifically I will deal with the problem using a product that will safisfy both the client and me, the developer                                                                                                                                                                                                                                                                                                                                               | 15 mins        | Sep 10            | A         |
| 5    | Create a system diagram for the solution proposal                                                                   | To have created a clear, direct visual representation of the hardware and software requirements for my solution proposal                                                                                                                                                                                                                                                                                                                                                                               | 20 mins        | Sep 11            | B         |
| 6    | Create a flow diagram for the solution proposal                                                                     | To have created a clear flow diagram for my calculator and secret password-manager product, complete with a plan for every possible situation that could occur when the application is in use                                                                                                                                                                                                                                                                                                          | 35 mins        | Sep 11            | B         |
| 7    | Create a functional calculator                                                                                      | To have completed the code for a functional calculator (preferably all within one function) which can complete basic operations such as +, -, * & /                                                                                                                                                                                                                                                                                                                                                    | 40 mins        | Sep 12            | B         |
| 8    | Write the code for the secret access function within the calculator                                                 | To have written the code for a working secret-code-system that allows a user to input a secret code into to the calculator which it will regocnize, allowing it to switch to a secret menu for the password manager                                                                                                                                                                                                                                                                                    | 20 mins        | Sep 16            | B         |
| 9    | Write the code for the menu within the secret password manager                                                      | To have written the code for the menu in the secret password manager that includes the ability for the user to choose between the options to add, delete and view passwords, and also exit the secret section back into the calculator                                                                                                                                                                                                                                                                 | 20 mins        | Sep 18            | B         |
| 10   | Write the code for each of the functions of the password manager                                                    | To have written the code in for each function of the secret password manager (preferably all in one function), including the ability to add a password (which includes the ability to associate a password with a 'title', or in this case a building/room) and conversely delete a password (which should be done by inputting the specific password using the associated title), along with the ability to view the password saved within a separate .csv file which is attached to the program file | 120 mins       | Sep 20            | B         |
| 11   | Write the code for the encryption of the passwords                                                                  | To have written the code for functional encryption of the passwords saved on the potentially insecure .csv file (all in one function), and to have created a separate function that decrypts the password whenever the 'View All Passwords' option is selected                                                                                                                                                                                                                                         | 60 mins        | Sep 22            | B         |
| 12   | Meet up with the client show progress, present the MVP (minimum viable product a.k.a. a prototype) and get feedback | Show the client the progress made in regards to the program and the code, and receive meaningful feedback on the product that can be taken into account before its official release                                                                                                                                                                                                                                                                                                                    | 10 mins        | Sep 25            | A, B      |
| 13   | Improve the program using the feedback provided                                                                     | Complete adjustments based on the constructive feedback received and ensure that the product is working                                                                                                                                                                                                                                                                                                                                                                                                | 60 mins        | Sep 26            | B         |
| 14   | Write the record of tasks                                                                                           | to have recorded (on GitHub) the sequence of actions a developer must follow in order to efficiently and quickly complete a project that is comparable in terms of both time and/or idea                                                                                                                                                                                                                                                                                                               | 30 mins        | Sep 26            | B         |
