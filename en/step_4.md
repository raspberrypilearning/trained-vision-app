## Make your model

This project has two parts to it: first you build a model on Teachable Machine, and then you use that model in an application you'll build on your computer. Teachable Machine is a tool made by Google that creates machine learning models in your browser. You'll create a model to recognise images, but it can also create models that recognise sounds, or body poses.

### Create a model with classes
Before you can start training a model, you need to decide how many different classes of image your model will be able to recognise. You'll have to provide training data for each of these classes, so don't pick too large a number. Maybe start with fewer than five classes, and add more — if you need to — once you have those ones working.

--- collapse ---
---
title: Create a Teachable Machine model
---

To get started, open the [Teachable Machine image model training page](https://teachablemachine.withgoogle.com/train/image){:target="_blank"} in a new tab in your browser.

![Teachable Machine training page](images/tm_start_screen.png)

This is an untrained model, with two classes, so it will be able to recognise two things. You should use the pencil beside each class name to rename them, so they describe the things they'll recognise.

--- /collapse ---

--- collapse ---
---
title: Add more classes to your model
---

You can add additional classes if you want your model to be able to recoginse more than two things. Click the **Add a class** button to add a third class to your model.

![The "Add a class" button in Teachable Machine](images/tm_add_class.png)

--- /collapse ---

--- collapse ---
---
title: Save your model
---
Once you've changed something in your model, you'll be able to save it. You can do this by using the menu in the top-left corner of the Teachable Machine window. Open it, and click on the 'Save project to Drive' option. Note that you will need to be logged into a Google account to do this.

![The Teachable Machine menu, with 'Save project to Drive' highlighted](images/tm_save_to_drive.png)

--- /collapse ---

### Train your model
To train the model you've created, you'll need to provide it with data for each of its classes. Teachable Machine allows you to do this either by recording data using your computer's webcam, or by uploading images from your computer or Google Drive.

When providing training images for your model, there are some things you should consider:

 + Try to ensure that either the only thing that changes between your training images is the thing you want the model to focus on — say a specific hand gesture, or whether someone is wearing a hat, or that the training images come from a wide variety of contexts. What you should avoid is a situation where the images for one class have, for example, a blue wall in the background, while the images for another class are all taken outdoors in a park. The model may incorrectly learn blue wall or green grass as the clues to identify the classes, rather than the specific features you are trying to teach it.
 + For similar reasons, if you're trying to teach the model to recognise a gesture, or something about a person's appearance — if they're wearing a hat, their hair colour, etc., then you should make sure you either use the same person for all of your training data or, ideally, use a wide variety of people in the training data for every class. Models that are trained on a single gender, racial group, age group, or any other group of people that are visually similar, are weaker than those trained on groups of people that are visually distinct. Likewise, if you are teaching the computer to recognise if someone is wearing a hat, it will learn better if shown many hats in different colours. The general rule is to try to expose the computer to the class you are trying to teach it in as many contexts as you can think of — within the limits of what's safe and practical for you to do!

You will have to provide images for each of the classes in your model separately. This does mean that you can record images for one class with your webcam while uploading existing images for another class, if you have a collection of such images available.

--- collapse ---
---
title: Record images using your computer's camera
---
If you are using a Raspberry Pi with a camera, once you have [set up the camera](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera) it will function as a webcam.

Click on the **Webcam** button for the class you want to train to show the webcam controls.

You will see the class expand to show a preview from your computer's camera (you may need to grant the Teachable Machine website permission to access your camera) and a **Hold to Record** button.

![A 'rock' class has been expanded. On the left-hand size is the webcam section and Hold to Record button. On the right-hand side is 'Add image samples'.](images/tm_webcam_images.png)

By clicking on the cog beside the **Hold to Record** button, you can set Teachable Machine to record a clip with a short delay instead, which may be useful if you need both hands to make a gesture, hold an object, etc.

![A short video clip of someone recording the 'paper' gesture from a game of 'rock, paper, scissors'](images/training.gif)

Make sure to record at least 300 image samples, which should only take a few minutes. Recording extra samples will improve the quality of your model, so if you have time to record over 1,000 samples, you should do so.

--- /collapse ---

--- collapse ---
---
title: Upload existing images
---

Click on the **Upload** button for the class you want to train to show the upload controls. You'll see an option to upload images from your computer, or to use images stored in your Google Drive. 

Choose whichever matches the location in which you've stored your images, and then use the dialogue that opens to select and upload the images that match the class.

--- /collapse ---

Once you have data recorded, it's time to train your model.

--- collapse ---
---
title: Train your model
---
Train the model by clicking the **Train Model** button. That was easy!

![Train Model button](images/tm_train_model.png)

The training will take a short time, during which you can watch Teachable Machine count the epochs it's running through. **You need to leave your browser open on the Teachable Machine tab, or the model will stop training.** 

--- /collapse ---

--- collapse ---
---
title: Test your model
---
Spend some time testing your model's preview, to see if it usually predicts things correctly. If you've trained it to recognise something you can put in front of your computer's camera, then you can put different people in front of the camera, make different poses, or whatever you need to test it that way. If your model is trained for something you can't put in front of the camera easily, then you can upload some image files — making sure that those files were not part of the training data used for the model — and have your model classify them to test it.

![The preview control, with the 'File' option selected](images/tm_upload_preview.png)

--- /collapse ---

### Export your model
Once your model works well enough — it will never be right all the time, but being right most of the time is pretty good — it's time to export the model so you can use it as part of your program.

--- collapse ---
---
title: Export your model to use in your own program
---

Click the **Export Model** button in the 'Preview' section.

![Export Model button](images/tm_export_model.png)

In the screen that appears, select the 'Tensorflow' tab and, make sure that 'Model conversion type' is set to 'Keras', and click the **Download my model** button.

![Tensorflow tab](images/tm_download_model.png)

**Make sure you remember where you save the model, you'll need it in a few minutes!**

--- /collapse ---
