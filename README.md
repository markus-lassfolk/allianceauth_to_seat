# allianceauth_to_seat
This is an EVE Online tool to pull API keys from the Alliance Auth application database to the SeAT database. Alliance Auth is located here https://github.com/R4stl1n/allianceauth and SeAT is located here https://github.com/eve-seat/seat. 

Alliance Auth provides wonderful tools, allowing your members to submit API keys and get immediate access to Jabber/Forums/Comms. It also allows for characters with blue standings to alliance to gain limited access.

A simple (or stupid) EVE API Too (SeAT) is a very, very complete tool allowing complete API inspection for both characters and corporations. It is a significant improvement over tools like JackKnife for looking through characters' API keys, and is invaluable in its ability to keep track of corporate assets and towers.

My tool does a lazy grab of the MySQL database for Alliance Auth keys and SeAT keys and submits them to the SeAT API after checking they aren't already there with the database. Submitted API keys can then be organized using the People group manager, keeping track of mains and alts (SeAT functionality, not mine.).

Special thanks to qu1ckkkk and Raynaldo Rivera (R4stl1n on github) for their work, I have done very little.

# Future
I need to rewrite this a bit to use SeAT's API better. It has support for GET and DELETE and this could improve syncing greatly, without requiring a call to SeAT's database directly.
