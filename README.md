Backend
==============

### To setup local dev/testing Environment

Over the time we received a lot of feedback on how the productivity of individual contributor increases if we they do not have to deal with systems and environment stuff (Dependency packages, confilicts due to multiple package manangers across multiple projects etc). So,we made a virtual box using Vagrant which has all the right dependency packages of the packages that are required for smooth development, testing and local deployment of Backend. In other words, all instructions mentioned in the docs for getting started will run smoothly.

1.  Install Vagrant: Download link can be found at https://www.vagrantup.com/downloads.html

2. Download the Vagrant package.box file: Can be found here https://s3-us-west-2.amazonaws.com/feedmedia/package.box

3. Follow the instrucitons to login to virtual box

  `$ vagrant box add testbox package.box` (First time only)

  `$ vagrant init testbox` (First time only)

  `$ vagrant up`

  `$ vagrant ssh`
  
  `$ git config --global user.name "Your Name"` (First time only)

  `$ git config --global user.email youremail@xxx.com` (First time only)
  

4. Once you are inside the virtual box, you can proceed with the instructions avalable at  https://github.com/RoboBrainCode/Docs/blob/master/README.md
5. Once you finish develpment and testing, you can issue `vagrant shutdown` to exit the virtual environment. You can always comeback by using step 3. 



### Graph Structure
1. Nodes have either the label :Concept or :Media. If they have :Media, they will also have a :Image, :Video or :Text label depending on what media type they represent.
2. Edges store the source_url, source_text and keywords (an array of strings) properties. Each edge is labeled by its edge type. For example, an edge representing the spatially_distributed_as relationship will have the :SPATIALLY_DISTRIBUTED_AS label.
3. Nodes store the handle name without the #. eg. {handle: 'shoe'}
4. :Media nodes referred to in the source_text with a #$ will have the word following #$ as the handle name. eg. #$image -> {handle: 'image'}
5. :Media nodes NOT referred to in the source_text will have the file name of the media as the handle name and the full url path of the media as mediapath. eg. 'aaa/bbb/shoe.jpg' -> {handle: 'shoe.jpg', mediapath: 'aaa/bbb/shoe.jpg'}

### Setting up submodules
Once you pull or clone the Backend repo, you need to do:

1. `cd Backend/`

2. `git submodule init`

3. `git submodule update`


Any time a change to any of the submodules is pushed to the Backend repo, you
need to do `git submodule update`.

### Setup Django with MongoDB
* Follow the URL

http://django-mongodb-engine.readthedocs.org/en/latest/topics/setup.html

* Execute the following commands:

1. sudo pip install git+https://github.com/django-nonrel/django@nonrel-1.5

2. sudo pip install git+https://github.com/django-nonrel/djangotoolbox

3. sudo pip install git+https://github.com/django-nonrel/mongodb-engine

4. sudo pip install djangorestframework


This will also install Django for you, further any Django project created will use MongoDB (and not the default sqlite3).

### Possible errors
* You might get an error (not necessarily) that DJANGO_SETTINGS_MODULE is not set. If this happens then follow the link

http://2buntu.com/articles/1451/installing-django-and-mongodb-in-your-virtualenv/

PS: There is no needs to setup virtualenv.

### Update viewer feeds

The script inside directory UpdateViewerFeeds runs as a cron job and balances the frontend feeds. Giving equal importance to all the projects. The script import the settings file mentioned in manage.py. So if you change the settings filename in manage.py, then accordingly modify the updateViewerFeed.py file. 
