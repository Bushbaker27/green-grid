# Green Grid 

![image](https://user-images.githubusercontent.com/71279551/215338292-5f203d98-0ea0-45f1-a38b-6b057160dfca.png)

## Inspiration
According to farms.com, autonomous tractor usage in the United States is at 35%.  The technology for autonomous tractors should be improved to include environmental sustainability and help increase profitability for local farmers. Provided the most recent studies done by the USDA Economic Research Service showing that 12%-13% percent of farmers live below the poverty line, we felt inspired to create an application that not only is better for the environment but can also benefit local farmers who are dependent on their crops. 
## What it does
Our project utilizes pygame simple user-interface to provide crop options to farmers and the software would plant the best companion. This integrated software would be used in current tractor software to detect where the tractor is at a certain point in time and be able to autonomously move/plant freely. 
## How we built it
We setup a database in JSON containing 16 crops and their respectful crop companions. Development tools used throughout the project includes Python, Twilio, and Flask. For the UI, we used pygame to display length/width entries, crop options, and the farmland along with the tractor.
## Challenges we ran into
The path to the finish line was met with quite a few road bumps. The first challenge we ran into was finding the information for crop companions. Intercropping is not as universal as monocropping making the search for data exhausting. After doing research, we found a credible website that listed a few crops and their respectful crop companions. We then faced a simple, yet tedious to solve the issue of scaling. On some screens, the buttons and fields were not scaled correctly to fit. After a few short grueling hours, we finally solved it and moved on to our next road bump. Figuring out how to communicate with Twilio's micro-service was our next puzzle to solve. Luckily, Twilio has a up-to-date documentation, which assisted a good amount in learning the micro-service and incorporating it into our application. Finally,
## Accomplishments that we're proud of
As a group, we overcame a lot of obstacles and we feel accomplished with our final product. Successfully integrating Twilio into our project is a huge accomplishment, this now sets a roadmap for the future for better application development. Solving the sorting problem for optimal crop placement, required the minds of everyone in this group. With this came a lot of tests, a lot of successes, and a lot of failures. In the end, we finally figured out how to get the best crop companion(s) for each crop. Along with this, our ability as a group to tackle problems on the frontend and backend is something we all feel proud of.
## What we learned
We acquired a great amount of knowledge in pygame, Twilio, Flask, version control, and threading. A great team with great people really pushed this project to the finish line. All in all, after 24 hours, we had a great experience at SpartaHacks 8 and faced a lot of interesting challenges.
## What's next for Green Grid
Creating a great application to push the ideas of intercropping further and assist farmers in a technological world, we want to test our Green Grid software on an Arduino board to simulate a tractor.
