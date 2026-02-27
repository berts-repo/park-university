# Unit 2: Notes

This unit covers using the Google Cloud Platform. This is not an educational version, but the full strength industrial version. The good news is that you are learning on a tool that is directly used in industry. The bad news is that there is a lot of functionality, which can be overwhelming at first, especially since your Park Google account is not configured to work with this service.

Getting Credits to use Google Cloud Platform 

Google provides students with $50 of credit to use its cloud environment. However, these have to be requested by your instructor and the process of redeeming your credit is a little convoluted and tricky. The general process is as follows:

Instructor will send you link to a form that you fill out with your name and PARK email address. Your address must end in @park.edu for this to work.

After filling out the form, you’ll get an email from Google to your PARK email address. DO NOT OPEN the email.

Forward the email to your regular Gmail account.

Log out of your PARK Gmail/Google account. Don’t just switch accounts, make sure you are logged out. This process won’t work if it uses your Park account.

Using Chrome, log in to your regular Gmail account, read the forwarded email, and click on the link, then paste the coupon code from the email into the text box to redeem. Your page will refresh showing you a $50 credit for Operating Systems Administration

Click Accept & Continue.

Create a project. If you aren’t already directed to create a new project, click on the hamburger menu, then Home. You will end up at the console home page.

In the area that is circled, you should see “Create a new Project” instead, so click on that. Specify a project name using your own name, CS369, and the term, like “Ada Lovelace CS369 F1 2018”

If instead of a project, you get an error like:

 

then you redeemed your coupon while logged in to your Park gmail account and now have extra work to do. See the document ( [link: https://canvas.park.edu/courses/72082/files/9774601?verifier=T8YIWgwvq2YVos6cEuObEmmZ9T3X1MK5RwbONb9N&wrap=1] GCP_G_Suite_Workaround.pdf)

You will also want to do two more steps, give your instructor access to your project, and set a budget.

Give your instructor access privileges.

Click the hamburger menu, the IAM & admin, then the +Add button

Enter your instructor’s gmail account, with role of Editor, then save. Do not blindly enter  [link: mailto:cs373johncigas@gmail.com] cs373johncigas@gmail.com as shown in the example. 

Set a budget and budget alerts

Click on hamburger menu, Billing, Budgets and Alerts, click Create Budget button

Pick a budget name

Set the specified amount as $10 (this is a monthly budget)

Under Set Threshold Rules, click Add Item button

Add 1% item, and Save

The reason for the 1% is so you can see if budget alerts are working before you actually have a problem. You can ignore the actual alert at the 1% level.

That’s it for the setup. You only have to do this setup one time. After that, you will just use your regular Gmail account to log into and manage your GCP resources.

Google Cloud Console (the starting place for your cloud account)

and

Google Cloud Shell (a separate virtual machine with a command line interface)
