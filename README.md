# Fraud Pruning in ATM Using QR Code

We are aware that the current technology under implementation to withdraw money is that we use an ATM card in which the data is incorporated in the magnetic stripe, and the user must enter a four-digit secure PIN for transactions. This method is prone to many frauds such as ATM card skimming, reply attack, shoulder surfing, and video recording with hidden cameras, which occur at ATM terminals. This project work proposes a novel approach for fraud pruning at ATM terminals by eliminating the need for ATM cards making them contactless and secure. In this new way of authentication, the complete process is contactless, and this avoids the spread of contagious viruses such as COVID19 pandemic situation. The proposed methodology uses mobile, to which after authentication, a unique code will be sent by the server and the same is used to generate the QR code. The generated QR code needs to be scanned through the ATM. A hardware model for ATM machine has been designed and QR code was used successfully to collect the amount entered in the mobile phone from the model.

## Dedicated Website for the methodology:
### MOBILE
Mobile devices or smartphone is a crucial component in the proposed methodology. Mobile provides an interface for the user to interact with our mechanism. The user will have to browse our web page to initially set up their account. This can be done by following the sequence of signup, login, and register themselves.

The basic pin will be provided to the user by the Bank upon enrolling in the facility, using which the user will have to signup, log in, and register. All the above steps are very simple where the user is asked very basic details regarding themselves. The signup is the very first setup where the user provides details like their name and email id. He/she is allowed to set their username and password. Using the above credentials, the user will now have to log in.

Once the user has Logged in successfully, He/she will now have to register their account for the cardless and contactless transaction facility. In this step, the user can reset his security pin as per their need over the current pin i.e., the Basic pin. Now the user is completely ready to access his account right in his hand via mobile phone. The user can Withdraw the money being cardless and without making any physical contact with the ATM, and the user can also check his current balance via our webpage.

Another important role of mobile is to display the QR code. The generation of QR codes is done when the user will have to withdraws the amount. The user will have to choose “Withdraw” on our webpage via mobile to initiate the cardless transaction. Followed by which he/she must enter the sum of withdrawal and security pin, now to process the transaction, after authentication at the server end a UUID is received which is converted into QR Code and is displayed on the mobile screen. The generated QR Code is active for 90 seconds from the time of generation. The user can now scan the generated QR Code via the camera attached to ATM and collect the money.

The choice of displaying QR code on mobile screen reduce fraud activity by not allowing the fraudsters to access sensitive information in QR code, over displaying the QR code on the ATM screen.

### SERVER
The Server is the third and last component of the proposed methodology. It serves as the hub of authentication and c. It incorporates the Database, thus holding information about the user account and the transactions.

In this proposal, a dedicated Laptop is used as a server. A local network is established by connecting the ATM and Mobile to the IP address of the laptop resembling a server. Through this network, the Mobile and ATM communicate through the server for Pin and UUID validation.
When the user registers their account via their smartphone on our webpage, The data is stored as a table in the database held on the server. The server utilizes the data stored at this instance to authenticate the security pin of the user, by comparing the entered secure pin and existing secure pin i.e., the pin which was set by the user at the time of account registration. This process is termed has Pin Authentication or Pin Validation.
In the process of Pin authentication, if the comparison result is successful i.e., both the PINS matched a UUID will be generated at the Server. This UUID is stored in the database of the server and then sent to the user which is displayed on the mobile screen as a QR code.

When the user scans the QR Code at the ATM terminal, The QR code is converted into UUID by the ATM and is sent to the server for UUID authentication.
UUID authentication is a very crucial step in the proposed methodology where the UUID generated and stored at the server is validated by comparing it with the UUID obtained by scanning the QR code.
The server generates an Acknowledgment based on the UUID authentication and the same is sent to the ATM. ATM decides on dispatching the amount based on the Acknowledgement received.
