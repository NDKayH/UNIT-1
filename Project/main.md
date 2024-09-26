# Project Unit 1

## Criterion A: Planning

### Problem Definition
My client, the staff and faculty of a boarding school, have various different padlocks for the buildings across campus which are locked every night at 23:00. These buildings, containing mostly classrooms, were broken into by three students two and a half weeks ago, and after an investigation the school concluded that a data breach had occurred where a password for one of the buildings was shared and students were able to hang out very late at night. The school has opted for several future prevention methods; the first one is to change all the passwords of each and every lock on the school campus to much more complicated ones. However, they realize that because of how difficult these new passwords might be to remember, the people responsible for locking up the buildings might write down passwords on paper, which is quite insecure, and they believe a breach could happen again. To prevent this, the school is also looking for a password storage application that contains a database of all passwords. 

### Proposal Solution

The boarding school staff and faculty have identified a need for a secure, centralized password management solution to safeguard the passwords used to lock various buildings across campus. This project aims to address the recent security breach by providing an encrypted password storage and management system that ensures only authorized personnel can access and use building passwords. This solution will help prevent unauthorized access and mitigate the risk of another data breach, ensuring that complex passwords can be managed efficiently and securely.

#### **Objectives**

1. **Enhanced Security**: Secure storage of complex building passwords to prevent unauthorized access.
2. **User-Friendly Management**: Provide an intuitive system for authorized personnel to create, view, and manage passwords without the need to remember them.
3. **Controlled Access**: Implement a mechanism to ensure only authorized staff can access and update passwords.
4. **Data Integrity**: Ensure that all password entries are encrypted, preventing potential breaches even if access to the storage file is compromised.

### **Design Proposal for Secure Password Management System**

#### **System Features**

1. **Password Management Application**: 
   - The main application will serve as a password manager that allows authorized staff to:
     - **Add** new building passwords.
     - **Delete** old or outdated passwords.
     - **View** encrypted passwords securely.
     - **Modify** existing passwords when changes are needed.

2. **Encryption and Decryption**: 
   - All passwords will be encrypted using a basic yet effective encryption algorithm to ensure data confidentiality.
   - The system will implement a ROT13-based encryption technique that shifts alphabetic characters, rendering them unreadable to unauthorized users.
   - This encryption ensures that even if an unauthorized person accesses the storage file, the passwords remain secure and unreadable.

3. **Secure Storage**: 
   - Passwords will be stored in a `passwords.csv` file that functions as the password database.
   - Each entry will consist of a building identifier (e.g., room number) and the encrypted password.
   - The CSV format ensures easy storage and retrieval, while the encryption ensures data remains secure.

4. **Calculator Integration**: 
   - The system will have a basic calculator interface for routine use by staff, with a secret "master code" that switches to the password management interface, ensuring authorized access to the password manager is hidden from unauthorized users.

5. **Access Control via Secret Code**: 
   - A unique master code (`lockup_92135467`) serves as a gateway to the password management system, allowing only authorized personnel to switch from the calculator interface to the password management system.

#### **System Architecture**

- **User Interface**: The application interface is text-based and runs on a console or terminal. Staff interact with the application through menu-driven prompts.
- **Data Storage**: The password storage is handled via a `passwords.csv` file, ensuring that passwords are stored securely and can be accessed by authorized staff when needed.
- **Encryption Module**: The encryption logic handles both encryption and decryption functions to convert plain text passwords into secure, encrypted strings and back when needed.
  
#### **Workflow and Usage Scenarios**

1. **Daily Operations**:
   - Staff access the system through a simple calculator application interface, which they use regularly.
   - When the time comes to manage building passwords, authorized staff input the secret master code (`lockup_92135467`) to access the password manager.

2. **Password Management**:
   - **Adding Passwords**: Staff can input the building identifier and a password. The system encrypts the password before storing it.
   - **Deleting Passwords**: Staff can delete passwords by specifying the building identifier, ensuring obsolete passwords are removed.
   - **Viewing Passwords**: Encrypted passwords can be decrypted within the application, allowing authorized staff to view them securely when necessary.

3. **Data Protection**:
   - The encrypted password data stored in `passwords.csv` ensures that even if this file is accessed without authorization, the passwords remain protected.
   - The encryption technique ensures that sensitive data is secure both in transit and at rest.

#### **Technical Details**

1. **Encryption Method**: 
   - Utilizes a modified ROT13 encryption technique that shifts alphabetic characters while retaining any uppercase/lowercase structure.
   - Non-alphabetic characters (e.g., numbers, symbols) remain unchanged, ensuring the password complexity is preserved.

2. **Programming Language**: Python is used for its simplicity and ease of implementation, allowing non-technical staff to interact with the application effortlessly.

3. **Storage File Format**: CSV is chosen for its readability, simplicity, and ease of access, even if opened outside the application.

#### **Benefits**

- **Security**: Encrypted storage minimizes the risk of unauthorized access, even if the CSV file is compromised.
- **Convenience**: Staff have a single point of access for all building passwords, reducing the risk of losing passwords on paper or sharing them in an insecure manner.
- **Flexibility**: The system can be expanded or modified to support additional features, such as password expiration policies or more sophisticated encryption methods, as needed.

#### **Future Considerations**

- Implement a more advanced encryption technique if the school requires an additional layer of security.
- Introduce a user authentication mechanism for added security, ensuring that only authorized staff can access and modify the password database.
- Explore integrating the system with a mobile app or web-based interface for easier access.

### Success Criteria 
1. The calculator should accept user input to perform basic operations (addition, subtraction, multiplication, division).
1. The calculator can handle typical errors (e.g., division by zero) and give appropriate feedback.
1. If the user enters the secret code ("open123"), the program will change modes and act as a password manager.
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
