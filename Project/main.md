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

4. **Storage File Format**:
   - .csv is chosen for its readability, simplicity, and ease of access, even if opened outside the application.


#### **Benefits**
   - **Security**: Even in the event that the .csv file is compromised, encrypted storage reduces the possibility of unwanted access.
   - **Convenience**: Employees just need to know one password to access the entire building, which lowers the possibility of misplacing paper passwords or sharing them insecurely.
   - **Flexibility**: As needed, the system can be extended or changed to accommodate new features, such password expiration policies or more advanced encryption techniques.


### Success Criteria 
1. The calculator should accept user input to perform basic operations (addition, subtraction, multiplication, division).
1. The calculator can handle typical errors (e.g., division by zero) and give appropriate feedback.
1. If the user enters the secret code `"open123"`, the program will change modes and act as a password manager.
1. In password manager mode, the user should be able to perform CRUD operations (Create, Replace, Update, Delete):
   * Add a password (for example, for a website).
   * View the stored passwords (only if they re-enter the secret code).
1. Save passwords permanently and securely
1. Use the terminal to interact with the user.

# Criterion B: Design
### System Diagram

### Flow diagrams for algorithms
![flow](https://github.com/user-attachments/assets/93f4a0fb-66b8-4993-9b3d-b0b47deaeb82)
**Fig. 1** This is the flow diagram for the algorithm used to search in the data file...

### Data storage

### Sketches of the application (wireframe diagrams)

### Test plan

## Record of Tasks
| Task | Planned Action              | Planned Outcome                                                 | Estimated Time | Target Completion | Criterion |
|------|-----------------------------|-----------------------------------------------------------------|----------------|-------------------|-----------|
|      | 1st Meeting with the client | Obtained a problem definition, understand what the situation is | 10 min         | Sep 7             | A         |
|      |                             |                                                                 |                |                   | A         |
|      |                             |                                                                 |                |                   |           |
