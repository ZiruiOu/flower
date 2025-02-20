Contribute on GitHub
====================

This guide is for people who want to get involved with Flower, but who are not used to contributing to GitHub projects.

If you're familiar with how contributing on GitHub works, you can directly checkout our 
`getting started guide for contributors <https://flower.dev/docs/getting-started-for-contributors.html>`_ 
and examples of `good first contributions <https://flower.dev/docs/good-first-contributions.html>`_.


Setting up the repository
-------------------------

1. **Create a GitHub account and setup Git**
    Git is a distributed version control tool. This allows for an entire codebase's history to be stored and every developer's machine.
    It is a software that will need to be installed on your local machine, you can follow this `guide <https://docs.github.com/en/get-started/quickstart/set-up-git>`_ to set it up.

    GitHub, itself, is a code hosting platform for version control and collaboration. It allows for everyone to collaborate and work from anywhere on remote repositories.

    If you haven't already, you will need to create an account on `GitHub <https://github.com/signup>`_. 

    The idea behind the generic Git and GitHub workflow boils down to this: 
    you download code from a remote repository on GitHub, make changes locally and keep track of them using Git and then you upload your new history back to GitHub.

2. **Forking the Flower repository**
    A fork is a personal copy of a GitHub repository. To create one for Flower, you must navigate to https://github.com/adap/flower (while connected to your GitHub account)
    and click the ``Fork`` button situated on the top right of the page.

    .. image:: _static/fork_button.png
    
    You can change the name if you want, but this is not necessary as this version of Flower will be yours and will sit inside your own account (i.e., in your own list of repositories).
    Once created, you should see on the top left corner that you are looking at your own version of Flower.

    .. image:: _static/fork_link.png

3. **Cloning your forked repository**
    The next step is to download the forked repository on your machine to be able to make changes to it.
    On your forked repository page, you should first click on the ``Code`` button on the right, 
    this will give you the ability to copy the HTTPS link of the repository.

    .. image:: _static/cloning_fork.png

    Once you copied the \<URL\>, you can open a terminal on your machine, navigate to the place you want to download the repository to and type:

    .. code-block:: shell 

        $ git clone <URL>

    This will create a ``flower/`` (or the name of your fork if you renamed it) folder in the current working directory.

4. **Add origin**
    You can then go into the repository folder:

    .. code-block:: shell

        $ cd flower

    And here we will need to add an origin to our repository. The origin is the \<URL\> of the remote fork repository.
    To obtain it, we can do as previously mentioned by going to our fork repository on our GitHub account and copying the link.

    .. image:: _static/cloning_fork.png
    
    Once the \<URL\> is copied, we can type the following command in our terminal:

    .. code-block:: shell

        $ git remote add origin <URL>

    
5. **Add upstream**
    Now we will add an upstream address to our repository.
    Still in the same directroy, we must run the following command:

    .. code-block:: shell

        $ git remote add upstream https://github.com/adap/flower.git

    The following diagram visually explains what we did in the previous steps:

    .. image:: _static/github_schema.png 

    The upstream is the GitHub remote address of the parent repository (in this case Flower), 
    i.e. the one we eventually want to contribute to and therefore need an up-to-date history of. 
    The origin is just the GitHub remote address of the forked repository we created, i.e. the copy (fork) in our own account.

    To make sure our local version of the fork is up-to-date with the latest changes from the Flower repository,
    we can execute the following command:

    .. code-block:: shell

        $ git pull upstream main


Setting up the coding environment
---------------------------------

This can be achieved by following this `getting started guide for contributors`_ (note that you won't need to clone the repository).
Once you are able to write code and test it, you can finally start making changes!


Making changes
--------------

Before making any changes make sure you are up-to-date with your repository:

.. code-block:: shell

    $ git pull origin main

And with Flower's repository:

.. code-block:: shell

    $ git pull upstream main

1. **Create a new branch**
    To make the history cleaner and easier to work with, it is good practice to 
    create a new branch for each feature/project that needs to be implemented.
    
    To do so, just run the following command inside the repository's directory:

    .. code-block:: shell

        $ git switch -c <branch_name>

2. **Make changes**
    Write great code and create wonderful changes using your favorite editor!

3. **Test and format your code**
    Don't forget to test and format your code! Otherwise your code won't be able to be merged into the Flower repository.
    This is done so the codebase stays consistent and easy to understand.

    To do so, we have written a few scripts that you can execute:

    .. code-block:: shell

        $ ./dev/format.sh # to format your code
        $ ./dev/test.sh # to test that your code can be accepted
        $ ./baselines/dev/format.sh # same as above but for code added to baselines
        $ ./baselines/dev/test.sh # same as above but for code added to baselines
    
4. **Stage changes**
    Before creating a commit that will update your history, you must specify to Git which files it needs to take into account.

    This can be done with:

    .. code-block:: shell

        $ git add <path_of_file_to_stage_for_commit>

    To check which files have been modified compared to the last version (last commit) and to see which files are staged for commit,
    you can use the :code:`git status` command.

5. **Commit changes**
    Once you have added all the files you wanted to commit using :code:`git add`, you can finally create your commit using this command:

    .. code-block:: shell

        $ git commit -m "<commit_message>"

    The \<commit_message\> is there to explain to others what the commit does. It should be written in an imperative style and be concise.
    An example would be :code:`git commit -m "Add images to README"`.

6. **Push the changes to the fork**
    Once we have committed our changes, we have effectively updated our local history, but GitHub has no way of knowing this unless we push
    our changes to our origin's remote address:

    .. code-block:: shell

        $ git push -u origin <branch_name>

    Once this is done, you will see on the GitHub that your forked repo was updated with the changes you have made.


Creating and merging a pull request (PR)
----------------------------------------

1. **Create the PR**
    Once you have pushed changes, on the GitHub webpage of your repository you should see the following message:

    .. image:: _static/compare_and_pr.png

    Otherwise you can always find this option in the ``Branches`` page.

    Once you click the ``Compare & pull request`` button, you should see something similar to this:

    .. image:: _static/creating_pr.png
    
    At the top you have an explanation of which branch will be merged where:

    .. image:: _static/merging_branch.png
    
    In this example you can see that the request is to merge the branch ``doc-fixes`` from my forked repository to branch ``main`` from the Flower repository.

    The input box in the middle is there for you to describe what your PR does and to link it to existing issues. 
    We have placed comments (that won't be rendered once the PR is opened) to guide you through the process.

    It is important to follow the instructions described in comments. For instance, in order to not break how our changelog system works,
    you should read the information above the ``Changelog entry`` section carefully.
    You can also checkout some examples and details in the :ref:`changelogentry` appendix.

    At the bottom you will find the button to open the PR. This will notify reviewers that a new PR has been opened and 
    that they should look over it to merge or to request changes.

    If your PR is not yet ready for review, and you don't want to notify anyone, you have the option to create a draft pull request:

    .. image:: _static/draft_pr.png

2. **Making new changes**
    Once the PR has been opened (as draft or not), you can still push new commits to it the same way we did before, by making changes to the branch associated with the PR.

3. **Review the PR**
    Once the PR has been opened or once the draft PR has been marked as ready, a review from code owners will be automatically requested:

    .. image:: _static/opened_pr.png

    Code owners will then look into the code, ask questions, request changes or validate the PR.

    Merging will be blocked if there are ongoing requested changes.

    .. image:: _static/changes_requested.png
    
    To resolve them, just push the necessary changes to the branch associated with the PR:

    .. image:: _static/make_changes.png

    And resolve the conversation:

    .. image:: _static/resolve_conv.png

    Once all the conversations have been resolved, you can re-request a review.


4. **Once the PR is merged**
    If all the automatic tests have passed and reviewers have no more changes to request, they can approve the PR and merge it.

    .. image:: _static/merging_pr.png

    Once it is merged, you can delete the branch on GitHub (a button should appear to do so) and also delete it locally by doing:

    .. code-block:: shell

        $ git switch main
        $ git branch -D <branch_name>

    Then you should update your forked repository by doing:

    .. code-block:: shell

        $ git pull upstream main # to update the local repository
        $ git push origin main # to push the changes to the remote repository


Example of first contribution
-----------------------------

Problem
*******

For our documentation, we’ve started to use the `Diàtaxis framework <https://diataxis.fr/>`_.

Our “How to” guides should have titles that continue the sencence “How to …”, for example, “How to upgrade to Flower 1.0”.

Most of our guides do not follow this new format yet, and changing their title is (unfortunately) more involved than one might think.

This issue is about changing the title of a doc from present continious to present simple.

Let's take the example of “Saving Progress” which we changed to “Save Progress”. Does this pass our check?

Before: ”How to saving progress” ❌

After: ”How to save progress” ✅

Solution
********

This is a tiny change, but it’ll allow us to test your end-to-end setup. After cloning and setting up the Flower repo, here’s what you should do:

- Find the source file in ``doc/source``
- Make the change in the ``.rst`` file (beware, the dashes under the title should be the same length as the title itself)
- Build the docs and check the result: `<https://flower.dev/docs/writing-documentation.html#edit-an-existing-page>`_

Rename file
:::::::::::

You might have noticed that the file name still reflects the old wording. 
If we just change the file, then we break all existing links to it - it is **very important** to avoid that, breaking links can harm our search engine ranking.

Here’s how to change the file name:

- Change the file name to ``save-progress.rst``
- Add a redirect rule to ``doc/source/conf.py``

This will cause a redirect from ``saving-progress.html`` to ``save-progress.html``, old links will continue to work.

Apply changes in the index file
:::::::::::::::::::::::::::::::

For the lateral navigation bar to work properly, it is very important to update the ``index.rst`` file as well. 
This is where we define the whole arborescence of the navbar.

- Find and modify the file name in ``index.rst``

Open PR
:::::::

- Commit the changes (commit messages are always imperative: “Do something”, in this case “Change …”)
- Push the changes to your fork
- Open a PR (as shown above)
- Wait for it to be approved!
- Congrats! 🥳 You're now officially a Flower contributor!


How to write a good PR title
----------------------------

A well-crafted PR title helps team members quickly understand the purpose and scope of the changes being proposed. Here's a guide to help you write a good GitHub PR title:

1. Be Clear and Concise: Provide a clear summary of the changes in a concise manner.
1. Use Actionable Verbs: Start with verbs like "Add," "Update," or "Fix" to indicate the purpose.
1. Include Relevant Information: Mention the affected feature or module for context.
1. Keep it Short: Avoid lengthy titles for easy readability.
1. Use Proper Capitalization and Punctuation: Follow grammar rules for clarity.

Let's start with a few examples for titles that should be avoided because they do not provide meaningful information:

* Implement Algorithm
* Database
* Add my_new_file.py to codebase
* Improve code in module
* Change SomeModule

Here are a few positive examples which provide helpful information without repeating how they do it, as that is already visible in the "Files changed" section of the PR:

* Update docs banner to mention Flower Summit 2023
* Remove unnecessary XGBoost dependency
* Remove redundant attributes in strategies subclassing FedAvg
* Add CI job to deploy the staging system when the ``main`` branch changes
* Add new amazing library which will be used to improve the simulation engine


Next steps
----------

Once you have made your first PR, and want to contribute more, be sure to check out the following :

- `Good first contributions <https://flower.dev/docs/framework/contributor-ref-good-first-contributions.html>`_, where you should particularly look into the :code:`baselines` contributions.


Appendix
--------

.. _changelogentry:

Changelog entry
***************

When opening a new PR, inside its description, there should be a ``Changelog entry`` header.

Above this header you should see the following comment that explains how to write your changelog entry:

    Inside the following 'Changelog entry' section, 
    you should put the description of your changes that will be added to the changelog alongside your PR title.

    If the section is completely empty (without any token), 
    the changelog will just contain the title of the PR for the changelog entry, without any description. 

    If the 'Changelog entry' section is removed entirely, 
    it will categorize the PR as "General improvement" and add it to the changelog accordingly. 

    If the section contains some text other than tokens, it will use it to add a description to the change. 

    If the section contains one of the following tokens it will ignore any other text and put the PR under the corresponding section of the changelog:

    <general> is for classifying a PR as a general improvement.

    <skip> is to not add the PR to the changelog

    <baselines> is to add a general baselines change to the PR

    <examples> is to add a general examples change to the PR

    <sdk> is to add a general sdk change to the PR

    <simulations> is to add a general simulations change to the PR

    Note that only one token should be used.

Its content must have a specific format. We will break down what each possibility does:

- If the ``### Changelog entry`` section is removed, the following text will be added to the changelog::

    - **General improvements** ([#PR_NUMBER](https://github.com/adap/flower/pull/PR_NUMBER))

- If the ``### Changelog entry`` section contains nothing but exists, the following text will be added to the changelog::

    - **PR TITLE** ([#PR_NUMBER](https://github.com/adap/flower/pull/PR_NUMBER))

- If the ``### Changelog entry`` section contains a description (and no token), the following text will be added to the changelog::

    - **PR TITLE** ([#PR_NUMBER](https://github.com/adap/flower/pull/PR_NUMBER))

        DESCRIPTION FROM THE CHANGELOG ENTRY

- If the ``### Changelog entry`` section contains ``<skip>``, nothing will change in the changelog.

- If the ``### Changelog entry`` section contains ``<general>``, the following text will be added to the changelog::

    - **General improvements** ([#PR_NUMBER](https://github.com/adap/flower/pull/PR_NUMBER))

- If the ``### Changelog entry`` section contains ``<baselines>``, the following text will be added to the changelog::

    - **General updates to Flower Baselines** ([#PR_NUMBER](https://github.com/adap/flower/pull/PR_NUMBER))

- If the ``### Changelog entry`` section contains ``<examples>``, the following text will be added to the changelog::

    - **General updates to Flower Examples** ([#PR_NUMBER](https://github.com/adap/flower/pull/PR_NUMBER))

- If the ``### Changelog entry`` section contains ``<sdk>``, the following text will be added to the changelog::

    - **General updates to Flower SDKs** ([#PR_NUMBER](https://github.com/adap/flower/pull/PR_NUMBER))

- If the ``### Changelog entry`` section contains ``<simulations>``, the following text will be added to the changelog::

    - **General updates to Flower Simulations** ([#PR_NUMBER](https://github.com/adap/flower/pull/PR_NUMBER))

Note that only one token must be provided, otherwise, only the first action (in the order listed above), will be performed.
