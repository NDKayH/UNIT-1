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

### Flow diagrams for algorithms
![flow](https://github.com/user-attachments/assets/93f4a0fb-66b8-4993-9b3d-b0b47deaeb82)
**Fig. 1** This is the flow diagram for the algorithm used to search in the data file...

### Data storage

### Sketches of the application (wireframe diagrams)

### Test plan

| Test NO | Type of test        | Area tested                                                                                    | Outcome of test                                                                                                                                                                                                                           | Time estimate | Target completion date | Criterion |
|---------|---------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Unit testing        | Advice on whether to buy or sell the coin, based on the coin value and the shift of the value. | Confirm that the program can fetch live data from the internet regarding the value of the coin, put that data into a csv file and then compare the current value with the value of the coin from a previous log in with the help of a csv | 10min         | Sep 18                 | B         |
| 2       | Unit testing        | Login and registration system                                                                  | Confirm that the user is able to sign in with the existing username and password pair that is saved in a csv file. Confirm that the user can create a new account with a new username and password                                        | 10min         | Sep 19                 | B         |
| 3       | Unit testing        | Graph of the portfolio value and the history of transactions.                                  | Confirm that the user can enter/withdraw and check the account balance as well as that the data can be graphed and displayed.                                                                                                             | 10min         | Sep 19                 | B         |
| 4       | Unit testing        | Login and sign up csv files                                                                    | Confirm that the data is stored correctly, "users2.csv" file can be read and appended thus also making sure that the program can check for correct account data. Confirm that the username is unique.                                     | 15min         | Sep 20                 | B         |
| 5       | Unit testing        | Balance check                                                                                  | Confirm that the balance is calculated correctly and then added to the "atm.csv" file and can be later displayed to the client on demand.                                                                                                 | 15min         | Sep 20                 | B         |
| 6       | Unit testing        | Menu check                                                                                     | Confirm that the menu has all the needed options and they can be interacted with, when demanded the code takes the user to the chosen menu option.                                                                                        | 15min         | Sep 20                 | B         |
| 7       | Unit testing        | Data fetch                                                                                     | Confirm that the code updates frequently and fetches the correct numbers and ads to the "doge_value.csv" file.                                                                                                                            | 15min         | Sep 23                 | B         |
| 8       | Integration testing | Login and registration system                                                                  | Confirm that the registration and login functions work well with one another.                                                                                                                                                             | 10min         | Sep 24                 | B         |
| 9       | Integration testing | Data fecth                                                                                     | Confirm that the data fetch functions work well with one another.                                                                                                                                                                         | 10min         | Sep 26                 | B         |
| 10      | System testing      | General                                                                                        | Confirm that the system flows smoothly with the use of the menu option.                                                                                                                                                                   | 15min         | Sep 26                 | B         |
| 11      | Userbility Testing  | General                                                                                        | Confirm that the system is friendly and easy to understand for the users                                                                                                                                                                  | 15min         | Sep 29                 | B         |

## Records of Tasks

| Task No | Planned Action                                                                                                            | Planned Outcome                                                                                                                                                                                                                                                                                                                                                                                   | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Meeting with the client                                                                                                   | Talk with the client to discuss their needs and what they expect from the program as well as think of solutions to the problem                                                                                                                                                                                                                                                                    | 10min         | Sep 13                 | A         |
| 2       | Come up with the problem definition                                                                                       | Write a clear problem definition on GitHub                                                                                                                                                                                                                                                                                                                                                        | 15min         | Sep 13                 | A         |
| 3       | Come to an agreement with the client regarding the success criteria                                                       | Write a clear list of the success criteria for a measurable outcome and that the problem is resolved                                                                                                                                                                                                                                                                                              | 10min         | Sep 13                 | A         |
| 4       | Come up with a proposed solution for the client                                                                           | Write a solution on how to deal with the problem given by the product that suits both the client and developer                                                                                                                                                                                                                                                                                    | 15min         | Sep 13                 | A         |
| 5       | Create system diagram                                                                                                     | To have a clear idea of the hardware and software requirements for the proposed solution                                                                                                                                                                                                                                                                                                          | 10min         | Sep 13                 | B         |
| 6       | Create a login system                                                                                                     | To have a flow diagram and the code for the login system                                                                                                                                                                                                                                                                                                                                          | 30min         | Sep 14                 | B, C      |
| 7       | Create the menu options with "Deposit", "Withdraw", "Balance", "Graph"                                                    | When login or signup is complete the client is met with the main menu where the client can choose between the 4 mentioned options                                                                                                                                                                                                                                                                 | 120min        | Sep 19                 | C         |
| 8       | Create a code that takes live data of DogeCoin value from internet and updates it with each login along with a suggestion | When selecting an option "Suggestion" in the main menu the client can see the current value of the coin as well as the value of the coin at the previous log in. These 2 values are compared and based on the result a business suggestion on whether to buy or sell the cryptocoin.                                                                                                              | 90min         | Sep 21                 | C         |
| 9       | Add "Suggestion", "Description" and "Exit" options to the menu                                                            | Adding 3 new options to the menu code, "Suggestion", "Description" and "Exit". "Suggestion" has the values of the coin as well as the business advice, "Description" includes the selected cryptocurrency's description including year of release, creator, basic description, inspiration behind creation, and worth. "Exit" offers an easy way to finish your actions in the electronic ledger. | 60min         | Sep 23                 | C         |
| 10      | Add a signup system to login                                                                                              | An offer is made to the client to either create an account along with a password or if the client's account with a set password already exists, log in to the account. The account details are registered and stored in a csv file.                                                                                                                                                               | 45min         | Sep 27                 | C         |
| 11      | Add an option to continue after the actions in another menu option is done                                                | After the client has completed the intended action within a menu option, the code offers to go to another menu option instead of exiting the code.                                                                                                                                                                                                                                                | 15min         | Sep 27                 | C         |
| 12      | Meet up with client to show progress and get feedback                                                                     | Show the client the progress with the code to gather the satisfaction result and listen to possible improvements that the client wants to be made                                                                                                                                                                                                                                                 | 25min         | Sep 29                 | A, B, C   |
| 13      | Write the description of the coin and citations                                                                           | Write the selected cryptocurrency's description including year of release, creator, basic description, inspiration behind creation, and worth in the success criteria.                                                                                                                                                                                                                            | 10min         | Oct 3                  | A         |
| 14      | Write the justification of the tools/structure of your solution and tools used                                            | Write the justification for the choice of crypto coin, code language, and tools used while coding.                                                                                                                                                                                                                                                                                                | 30min         | Oct 3                  | A, C      |
| 15      | Create flow charts for the code along with a description                                                                  | Draw flowcharts on important and difficult parts of the code and upload the image along with a description to GitHub.                                                                                                                                                                                                                                                                             | 120min        | Oct 4                  | B         |
| 16      | Write description for important code fragments                                                                            | Write the description of basic but the most important lines of code for others to understand it                                                                                                                                                                                                                                                                                                   | 60min         | Oct 4                  | C         |
| 17      | Write test plan                                                                                                           | On GitHub, record the procedures of steps a developer should take to test a program and the expected outcome of each test                                                                                                                                                                                                                                                                         | 60min         | Oct 4                  | B         |
| 18      | Write record of tasks                                                                                                     | On GitHub, record the procedures of steps a developer should take in order to successfully and in time complete a similar project in terms of time or idea.                                                                                                                                                                                                                                       | 60min         | Oct 4                  | B         |
| 19      | Add colour to code   
